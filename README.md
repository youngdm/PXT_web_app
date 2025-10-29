# PXT Web App - Peatland eXchange Tags

A web application for applying standardized metadata tags to peatland research data, inspired by HXL Proxy and designed specifically for the peatland research community.

## Project Overview

The Peatland eXchange Tags (PXT) Web App helps researchers standardize their peatland datasets using a comprehensive three-level metadata hierarchy:

- **Site Level**: Location and site characteristics (`#pxt_site_*` tags)
- **Event Level**: Observation and measurement details (`#pxt_event_*` tags)
- **Dataset Level**: Overall collection information (`#pxt_dataset_*` tags)

### Key Features
- ✅ **Privacy-First**: No permanent data storage - all processing is ephemeral
- ✅ **Research-Focused**: Designed for peatland researchers and practitioners
- ✅ **Standards-Based**: Implements 67 standardized PXT tags across three hierarchical levels
- ✅ **Simple Workflow**: Upload → Tag → Download → Store wherever you choose

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Basic familiarity with command line/terminal

### Installation

1. **Clone or download this project**
   ```bash
   cd PXT_web_app
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   cd app
   python app.py
   ```

4. **Open your web browser**
   - Go to: `http://127.0.0.1:5000`
   - You should see the PXT Web App upload page

### Test the Demo
1. Upload the sample file: `data/sample_peatland_data.csv`
2. Review the data preview and column structure
3. Note how this will connect to PXT tagging in future development phases

## Project Structure

```
PXT_web_app/
├── Documentation/           # Project plans and specifications
│   ├── project_overview.md       # Complete project vision and requirements
│   ├── workshop_demo_plan.md     # 4-week development timeline
│   └── week3/                    # Week 3 completion documentation
│       └── week3_completion_summary.md
├── app/                    # Main web application
│   ├── app.py                   # Flask application with complete workflow
│   ├── pxt_tags.py              # PXT tag definitions and validation logic
│   ├── templates/               # HTML pages
│   │   ├── upload.html            # File upload interface
│   │   ├── preview.html           # Data preview page  
│   │   ├── tagging.html           # PXT tag mapping interface
│   │   ├── validate.html          # Validation and export page
│   │   └── about.html             # Information page
│   └── static/                  # CSS, JavaScript, images
├── test_data/              # Sample datasets for testing
│   ├── sample_peatland_study.csv  # Comprehensive test dataset (10 sites)
│   └── quick_test.csv             # Quick test dataset (3 sites)
├── test_export.py          # Comprehensive export functionality tests
├── test_workflow.py        # End-to-end workflow validation tests
├── requirements.txt        # Python package dependencies
└── README.md              # This file
```

## Current Status: Week 3 Complete ✅

### ✅ What's Working Now (Workshop Demo v0.3)
- **Complete End-to-End Workflow**: Upload → Tag Mapping → Validation → Export
- File upload interface with drag-and-drop styling
- CSV parsing and validation with comprehensive error handling
- Data preview with detailed statistics and column analysis
- **PXT Tag Mapping Interface**: Interactive dropdowns with auto-suggestions
- **Required Field Validation**: Real-time validation with visual indicators
- **CSV Export with Embedded PXT Tags**: Download standardized datasets
- Professional presentation-ready interface suitable for workshops
- Comprehensive test suite validating all functionality

### ✅ Week 2 Features Completed
- Interactive column-to-tag mapping with dropdown menus
- Three-level PXT tag organization (Site/Event/Dataset)
- Field priority indicators (Required/Desirable/Optional)
- Auto-suggestion system for common column patterns

### ✅ Week 3 Features Completed
- Complete validation system for Required PXT fields
- CSV export with embedded PXT tags in column headers
- Professional validation interface with progress indicators
- End-to-end workflow testing and verification

### In Development (Week 4)
- **Week 4**: Final polish, demo materials, and workshop presentation preparation

### Future Enhancements
- Multiple file format support (Excel, JSON)
- Advanced validation rules and data quality checking
- Cloud storage integrations
- Collaborative tagging features
- API integrations with research repositories

## Workshop Demonstration

This version is being developed for a workshop presentation in approximately one month. The goal is to demonstrate the core PXT tagging concept with a working prototype.

### Demo Workflow ✅ FULLY FUNCTIONAL
1. **Researcher uploads CSV** → Web interface accepts file with validation
2. **Data preview** → System shows columns, sample data, and statistics
3. **PXT tagging** → User maps columns to PXT tags via interactive dropdowns
4. **Validation** → System validates Required fields with visual feedback
5. **Export** → User downloads CSV with embedded PXT tag headers
6. **Clean up** → All data automatically removed from system (no permanent storage)

**Complete workflow tested and working under 5 minutes per dataset!**

## Collaboration

This project is designed for collaborative development:

- **Clear documentation**: Every component explained for new contributors
- **Modular structure**: Easy to work on different parts simultaneously
- **Version control friendly**: Organized file structure for team development
- **Research community focus**: Built by and for peatland researchers

### Getting Involved
1. Review the `Documentation/project_overview.md` for complete vision
2. Check `Documentation/workshop_demo_plan.md` for development timeline
3. Test the current demo with your own peatland datasets
4. Provide feedback on user experience and missing features

## PXT Tag Standard

The app implements the PXT Tag Standard v0.1.2, which defines 67 standardized tags:

### Site Level (Required Fields)
- `#pxt_site_id`: Unique site identifier
- `#pxt_site_lat`: Latitude in decimal degrees
- `#pxt_site_lon`: Longitude in decimal degrees
- `#pxt_site_datum`: Geodetic datum (e.g., WGS84)
- `#pxt_site_type`: Peatland type (bog/fen)
- `#pxt_site_subtype`: Detailed peatland classification

### Event Level (Required Fields)
- `#pxt_event_id`: Unique event identifier
- `#pxt_event_site_id`: Links to site ID
- `#pxt_event_date`: Event date (ISO format)
- `#pxt_recorded_by`: Observer name

### Dataset Level (Required Fields)
- `#pxt_dataset_id`: Unique dataset identifier
- `#pxt_dataset_title`: Descriptive title
- `#pxt_dataset_description`: Detailed description
- `#pxt_dataset_keywords`: Search keywords
- `#pxt_dataset_contact_name`: Primary contact
- `#pxt_dataset_temporal`: Time coverage

*Full specification available in project documentation*

## Privacy & Data Handling

- **No permanent storage**: All data processing is temporary and session-based
- **Automatic cleanup**: Data is cleared from system after processing
- **Local processing**: No data sent to external services
- **Research data governance compliant**: Designed for institutional policies

## Troubleshooting

### Common Issues

**"Module not found" errors**
```bash
pip install -r requirements.txt
```

**Port already in use**
```bash
# Try a different port
python app.py  # Then visit http://127.0.0.1:5001
```

**File upload fails**
- Check file size (max 16MB for demo)
- Ensure file has .csv extension
- Verify CSV has headers in first row

### Getting Help
1. Check the error message in your browser
2. Look at the terminal/console output where you ran `python app.py`
3. Review sample data format in `data/sample_peatland_data.csv`
4. Ensure all requirements are installed correctly

## Development Timeline

- **Week 1** ✅: Basic file upload and preview
- **Week 2** ✅: PXT tag application interface with interactive mapping
- **Week 3** ✅: Validation system and CSV export with embedded tags
- **Week 4**: Workshop preparation, demo materials, and final polish

**Status**: Core functionality complete! Ready for workshop demonstration.

### Week 3 Achievements
- ✅ Complete CSV export with embedded PXT tag headers  
- ✅ Required field validation with visual progress indicators
- ✅ End-to-end workflow from upload to tagged export
- ✅ Comprehensive testing suite validating all functionality
- ✅ Professional interface ready for research community presentation

## Vision

Enable seamless data exchange across the peatland research community through standardized metadata tagging, supporting FAIR data principles while respecting researcher data sovereignty.

---

**PXT Web App** - Workshop Demonstration Version
Built for the peatland research community | No data stored permanently
