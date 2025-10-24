# PXT Web App - Workshop Demonstration Development Plan

## Overview

This document outlines the plan to build a demonstration version of the PXT Web App for a workshop presentation in approximately one month. The focus is on creating a working prototype that demonstrates the core PXT tagging concept without building a full production system.

## Workshop Demo Version - Scope Definition

### **What We will Build (Core Demo Features):**

1. **Simple file upload interface**
   - Web page where researchers can upload CSV files
   - Basic file validation (CSV format, size limits)
   - Clear upload status feedback

2. **Column mapping interface**
   - Display uploaded CSV columns
   - Dropdown menus to apply PXT tags to each column
   - Three-level tag organization (Site, Event, Dataset)
   - Visual indication of Required vs Desirable vs Optional fields

3. **Basic validation display**
   - Show which Required PXT fields are missing
   - Highlight completed vs incomplete sections
   - Simple status indicators (red/amber/green)

4. **Export functionality**
   - Download button for CSV with PXT tags embedded in headers
   - Preserve original data while adding standardized tags
   - Clear file naming convention

5. **Professional presentation interface**
   - Clean, modern web design suitable for workshop demonstration
   - Clear navigation and user feedback
   - Responsive design that works on projection screens

### **What We WON'T Build (Future Development):**
- User accounts or authentication systems
- Complex data transformations or calculations
- Multiple file format support (Excel, JSON, etc.)
- Cloud storage integrations (Google Drive, OneDrive, etc.)
- Advanced validation rules or data quality checking
- Permanent data storage or session persistence
- Multi-user collaboration features
- API integrations with external systems

## Development Timeline

### **Week 1: Foundation (Basic Infrastructure)**
**Goal**: Working file upload and CSV processing
**Time Commitment**: 2-3 hours
**Deliverables**:
- Project structure setup (folders, basic files)
- Python Flask application framework
- HTML upload page with file selection
- CSV reading and basic data display
- Test with sample peatland dataset

**Key Tasks**:
- Set up development environment
- Create basic Flask routes (upload, display)
- Implement CSV parsing with pandas
- Test file upload workflow
- Create simple data preview table

### **Week 2: PXT Tagging Interface (Core Feature)**
**Goal**: Column-to-tag mapping functionality
**Time Commitment**: 2-3 hours
**Deliverables**:
- Interactive column mapping interface
- PXT tag dropdown menus organized by level
- Field priority indicators (Required/Desirable/Optional)
- Tag selection persistence during session

**Key Tasks**:
- Build column display with tag selection dropdowns
- Implement PXT tag hierarchy (Site/Event/Dataset levels)
- Create visual indicators for field priority
- Add JavaScript for interactive tag selection
- Test with various CSV column structures

### **Week 3: Validation & Export (Complete Workflow)**
**Goal**: End-to-end functionality with validation
**Time Commitment**: 2-3 hours
**Deliverables**:
- Validation system for Required fields
- CSV export with embedded PXT tags
- User feedback for missing or invalid tags
- Complete upload-to-download workflow

**Key Tasks**:
- Implement Required field validation logic
- Build CSV export with PXT tag headers
- Add validation status display (missing fields)
- Create download functionality
- Test complete workflow with multiple datasets

### **Week 4: Workshop Preparation (Polish & Demo Materials)**
**Goal**: Workshop-ready demonstration
**Time Commitment**: 2-3 hours
**Deliverables**:
- Polished user interface suitable for presentation
- Demo dataset with peatland research examples
- User guide or quick-start documentation
- Presentation materials highlighting key features

**Key Tasks**:
- Improve visual design and user experience
- Create realistic demo dataset for workshop
- Write brief user documentation
- Prepare talking points for demonstration
- Final testing and bug fixes

## Technical Approach

### **Technology Stack (Simple Version)**
- **Frontend**: HTML + CSS + Basic JavaScript
- **Backend**: Python + Flask framework
- **Data Processing**: Pandas library for CSV handling
- **Storage**: No database - session-based processing only
- **Deployment**: Local development server (suitable for workshop demo)

### **Development Approach**
- **Baby Steps**: One feature at a time, fully tested before moving to next
- **Minimal Viable Demo**: Focus on core workflow, skip advanced features
- **User-Centered**: Design for workshop audience (researchers and practitioners)
- **Documentation-Driven**: Document each step for reproducibility

## Success Criteria for Workshop Demo

### **Functional Requirements**
✅ Researcher can upload a CSV file containing peatland data
✅ Interface displays uploaded columns clearly
✅ User can map columns to appropriate PXT tags
✅ System shows validation status for Required fields
✅ User can download CSV with PXT tags applied
✅ Entire process completes in under 5 minutes

### **Presentation Requirements**
✅ Professional appearance suitable for research community
✅ Clear workflow that demonstrates PXT tagging value
✅ Handles typical peatland dataset structures
✅ Provides immediate visual feedback on tag application
✅ Works reliably during live demonstration

## Risk Mitigation

### **Technical Risks**
- **Large file handling**: Limit upload size for demo version
- **Browser compatibility**: Test on multiple browsers before workshop
- **CSV format variations**: Test with diverse real-world datasets

### **Timeline Risks**
- **Scope creep**: Stick strictly to defined deliverables
- **Time availability**: Plan for 2-hour minimum weekly commitment
- **Technical complexity**: Choose simplest implementation that works

## Post-Workshop Development Path

### **Immediate Next Steps** (Based on Workshop Feedback)
1. Collect user feedback and feature requests
2. Identify most critical missing functionality
3. Plan Phase 2 development priorities
4. Consider deployment options for wider testing

### **Potential Enhancements** (Future Phases)
- Advanced validation rules based on PXT specifications
- Support for Excel files and other formats
- Integration with research data repositories
- Collaborative features for team-based tagging
- Advanced transformation and data quality features

## Development Support

This plan assumes ongoing technical guidance and support for:
- Problem-solving during development
- Code review and best practice advice
- Testing strategy and validation approaches
- Workshop presentation preparation

The goal is to create a compelling demonstration that validates the PXT Web App concept while establishing a solid foundation for future development phases.
