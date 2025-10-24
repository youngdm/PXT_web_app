"""
PXT Web App - Main Application File

A simple Flask application for applying Peatland eXchange Tags (PXT) to research data.
This demonstration version handles CSV file uploads and provides a foundation for
PXT tag mapping functionality.

Workshop Demo Version - Week 1: Basic file upload and processing
"""

from flask import Flask, request, render_template, redirect, url_for, flash, send_file
import pandas as pd
import os
from werkzeug.utils import secure_filename
import tempfile

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

            # For now, just show the data preview
            # In Week 2, this will redirect to the PXT tagging interface
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
    app.run(debug=True, host="127.0.0.1", port=5000)
