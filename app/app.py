"""
PXT Web App - Main Application File

A simple Flask application for applying Peatland eXchange Tags (PXT) to research data.
This demonstration version handles CSV file uploads and provides a foundation for
PXT tag mapping functionality.

Workshop Demo Version - Week 1: Basic file upload and processing
"""

from flask import (
    Flask,
    request,
    render_template,
    redirect,
    url_for,
    flash,
    send_file,
    session,
)
import pandas as pd
import os
from werkzeug.utils import secure_filename
import tempfile
from pxt_tags import (
    get_all_tags,
    suggest_tag_for_column,
    validate_column_mappings,
    get_tag_info,
)

# Initialize Flask application
app = Flask(__name__)
app.secret_key = "demo_secret_key_change_for_production"  # For flash messages

# Configuration
UPLOAD_FOLDER = tempfile.gettempdir()  # Use system temp directory
ALLOWED_EXTENSIONS = {"csv"}  # Only CSV files for demo
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB limit for demo
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE


def allowed_file(filename):
    """
    Check if uploaded file has an allowed extension.

    Args:
        filename (str): Name of the uploaded file

    Returns:
        bool: True if file extension is allowed, False otherwise
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    """
    Home page - displays file upload form.

    Returns:
        Rendered HTML template for file upload
    """
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    """
    Handle file upload and basic CSV processing.

    Processes uploaded CSV file and displays basic information about the data.
    In future weeks, this will redirect to the PXT tagging interface.

    Returns:
        Redirect to results page or back to upload with error message
    """

    # Check if file was submitted
    if "file" not in request.files:
        flash("No file selected. Please choose a CSV file to upload.", "error")
        return redirect(request.url)

    file = request.files["file"]

    # Check if filename is empty
    if file.filename == "":
        flash("No file selected. Please choose a CSV file to upload.", "error")
        return redirect(request.url)

    # Process file if it passes validation
    if file and allowed_file(file.filename):
        try:
            # Secure the filename
            filename = secure_filename(file.filename)

            # Read CSV directly from upload (no permanent storage)
            df = pd.read_csv(file)

            # Basic validation
            if df.empty:
                flash(
                    "The uploaded file appears to be empty. Please check your CSV file.",
                    "error",
                )
                return redirect(url_for("index"))

            # Get basic information about the dataset
            dataset_info = {
                "filename": filename,
                "row_count": len(df),
                "column_count": len(df.columns),
                "columns": df.columns.tolist(),
                "sample_data": df.head(3).to_dict("records") if len(df) > 0 else [],
            }

            # Store data in session for tagging interface
            session["dataset_info"] = dataset_info
            session["csv_data"] = df.to_dict(
                "records"
            )  # Store actual data for export later

            flash(
                f"Successfully uploaded {filename} with {len(df)} rows and {len(df.columns)} columns.",
                "success",
            )
            return render_template("preview.html", data=dataset_info)

        except pd.errors.EmptyDataError:
            flash(
                "The uploaded file appears to be empty or invalid. Please check your CSV file.",
                "error",
            )
            return redirect(url_for("index"))
        except pd.errors.ParserError as e:
            flash(
                f"Error reading CSV file: {str(e)}. Please check the file format.",
                "error",
            )
            return redirect(url_for("index"))
        except Exception as e:
            flash(f"An unexpected error occurred: {str(e)}. Please try again.", "error")
            return redirect(url_for("index"))

    else:
        flash("Invalid file type. Please upload a CSV file (.csv extension).", "error")
        return redirect(url_for("index"))


@app.route("/tag", methods=["GET", "POST"])
def tag_data():
    """
    Handle PXT tagging interface.

    GET: Display tagging interface with auto-suggestions
    POST: Process tag mappings and proceed to validation/export
    """
    if "dataset_info" not in session:
        flash("No data found. Please upload a CSV file first.", "error")
        return redirect(url_for("index"))

    dataset_info = session["dataset_info"]

    if request.method == "GET":
        # Get all available PXT tags
        all_tags = get_all_tags()

        # Generate auto-suggestions for each column
        suggestions = {}
        for column in dataset_info["columns"]:
            suggested_tag = suggest_tag_for_column(column)
            if suggested_tag:
                suggestions[column] = suggested_tag

        return render_template(
            "tagging.html",
            data=dataset_info,
            pxt_tags=all_tags,
            suggestions=suggestions,
        )

    elif request.method == "POST":
        # Process form submission with tag mappings
        column_mappings = {}

        for column in dataset_info["columns"]:
            selected_tag = request.form.get(f"tag_{column}")
            # Include ALL columns, with empty string for untagged ones
            column_mappings[column] = selected_tag if selected_tag else ""

        # Store mappings in session
        session["column_mappings"] = column_mappings

        # Validate column mappings against dataset
        validation_results = validate_column_mappings(column_mappings)
        session["validation_results"] = validation_results

        flash(
            f"Tag mappings saved! {len(column_mappings)} columns mapped to PXT tags.",
            "success",
        )
        return redirect(url_for("validate_export"))


@app.route("/validate")
def validate_export():
    """
    Display validation results and export options.
    """
    if "dataset_info" not in session or "column_mappings" not in session:
        flash("Please complete the tagging process first.", "error")
        return redirect(url_for("index"))

    dataset_info = session["dataset_info"]
    column_mappings = session["column_mappings"]
    validation_results = session.get("validation_results", {})

    # Create enhanced mappings with tag information
    enhanced_mappings = {}
    for column, tag in column_mappings.items():
        if tag and tag.strip():
            tag_info = get_tag_info(tag)
            enhanced_mappings[column] = {
                "tag": tag,
                "priority": tag_info.get("priority", "unknown"),
                "level": tag_info.get("level", "unknown"),
            }
        else:
            enhanced_mappings[column] = {"tag": "", "priority": "", "level": ""}

    return render_template(
        "validate.html",
        data=dataset_info,
        mappings=column_mappings,
        enhanced_mappings=enhanced_mappings,
        validation=validation_results,
        pxt_tags=get_all_tags(),
    )


@app.route("/export")
def export_csv():
    """
    Export CSV file with embedded PXT tags as column headers.

    Creates a new CSV file where original column names are replaced with
    their corresponding PXT tags, preserving all original data.
    """
    if (
        "dataset_info" not in session
        or "column_mappings" not in session
        or "csv_data" not in session
    ):
        flash(
            "No data available for export. Please complete the upload and tagging process first.",
            "error",
        )
        return redirect(url_for("index"))

    try:
        # Get data from session
        dataset_info = session["dataset_info"]
        column_mappings = session["column_mappings"]
        csv_data = session["csv_data"]

        # Get original column order from dataset_info
        original_columns = dataset_info["columns"]

        # Create DataFrame from stored data with explicit column order
        df = pd.DataFrame(csv_data, columns=original_columns)

        # Create PXT tags row (preserving original column order)
        pxt_tags_row = []
        for original_column in original_columns:
            if original_column in column_mappings and column_mappings[original_column]:
                # Use PXT tag for this column
                pxt_tag = column_mappings[original_column]
                pxt_tags_row.append(pxt_tag)
            else:
                # Empty string for untagged columns
                pxt_tags_row.append("")

        # Insert PXT tags as the first data row (keeping original headers)
        df.loc[-1] = pxt_tags_row  # Insert at index -1
        df.index = df.index + 1  # Shift index
        df.sort_index(inplace=True)  # Sort by index to put -1 row at top

        # Generate export filename
        original_name = dataset_info["filename"].rsplit(".", 1)[0]  # Remove extension
        export_filename = f"{original_name}_PXT_tagged.csv"

        # Create temporary file for download
        import tempfile

        temp_file = tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv", newline=""
        )
        df.to_csv(temp_file.name, index=False)
        temp_file.close()

        # Log successful export
        flash(
            f"CSV exported successfully with {len(column_mappings)} PXT tags applied!",
            "success",
        )

        return send_file(
            temp_file.name,
            as_attachment=True,
            download_name=export_filename,
            mimetype="text/csv",
        )

    except Exception as e:
        flash(f"Error exporting CSV: {str(e)}. Please try again.", "error")
        return redirect(url_for("validate_export"))


@app.route("/about")
def about():
    """
    Information page about PXT Web App.

    Returns:
        Rendered HTML template with project information
    """
    return render_template("about.html")


# Error handlers
@app.errorhandler(413)
def too_large(e):
    """Handle file too large error."""
    flash(
        f"File is too large. Maximum file size is {MAX_FILE_SIZE // (1024 * 1024)}MB.",
        "error",
    )
    return redirect(url_for("index"))


@app.errorhandler(500)
def internal_error(e):
    """Handle internal server errors."""
    flash("An internal error occurred. Please try again.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    # Run the application in debug mode for development
    # Note: Set debug=False for production deployment

    import socket
    import os

    def is_port_available(port):
        """Check if a port is available for use."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(("127.0.0.1", port))
                return True
        except socket.error:
            return False

    # Check if we're running in Flask's reloader process
    # The reloader restarts the app, so we need to skip port checking
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        # This is the reloader process - Flask already chose the port
        # Just run without port checking
        app.run(
            debug=True, host="127.0.0.1", port=int(os.environ.get("FLASK_PORT", 5001))
        )
    else:
        # This is the main process - do port selection
        primary_port = 5000
        fallback_port = 5001  # Unassigned port, safe to use

        if is_port_available(primary_port):
            port = primary_port
            print(f"🚀 Starting PXT Web App on http://127.0.0.1:{port}")
        elif is_port_available(fallback_port):
            port = fallback_port
            print(
                f"⚠️  Port {primary_port} is busy, using fallback port {fallback_port}"
            )
            print(f"🚀 Starting PXT Web App on http://127.0.0.1:{port}")
        else:
            print(f"❌ Both ports {primary_port} and {fallback_port} are unavailable.")
            print("   Please stop other applications using these ports and try again.")
            exit(1)

        try:
            # Set environment variable so reloader knows which port to use
            os.environ["FLASK_PORT"] = str(port)
            app.run(debug=True, host="127.0.0.1", port=port)
        except Exception as e:
            print(f"❌ Failed to start Flask app: {str(e)}")
            print("   Please check that no other applications are using the port.")
            exit(1)
