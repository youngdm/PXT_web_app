# PXT Web App - Project Overview

## Vision Statement

The Peatland eXchange Tags (PXT) Web App is a data processing and standardization platform inspired by HXL Proxy, specifically designed for peatland research and monitoring data. It serves as a "recipe book" for cleaning, transforming, merging, and validating peatland datasets to ensure consistency and interoperability across research institutions, environmental monitoring programs, and conservation initiatives.

## Core Concept

PXT operates on a **three-level metadata hierarchy** with standardized tags:
- **Site Level**: Location and characteristics (`#pxt_site_*` tags)
- **Observation Event Level**: When, how, and by whom measurements were taken (`#pxt_event_*` tags)
- **Dataset Level**: Overall collection information for data discovery (`#pxt_dataset_*` tags)
- Each level has Required, Desirable (Recommended), and Optional fields
- Consistent tagging ensures data compatibility across peatland research community
- **Data Exchange Focus**: Processing and standardization tool, not a data repository

## Envisaged workflow

1. Researcher uploads CSV file
   ↓
2. PXT Web App loads data temporarily
   ↓
3. User applies PXT tags to columns
   ↓
4. System validates and transforms data
   ↓
5. User downloads standardized output
   ↓
6. Data is cleared from PXT system
   ↓
7. Researcher stores result wherever they choose

## PXT Tag Structure

The PXT standard defines 67 specific tags organized across three hierarchical levels:

### Site Level Tags (`#pxt_site_*`)
**Required Fields:**
- `#pxt_site_id`: Unique site identifier (e.g., "CF001")
- `#pxt_site_lat`: Latitude in decimal degrees (e.g., "52.4912")
- `#pxt_site_lon`: Longitude in decimal degrees (e.g., "-4.0234")
- `#pxt_site_datum`: Geodetic datum (e.g., "WGS84")
- `#pxt_site_type`: Peatland type (e.g., "bog", "fen")
- `#pxt_site_subtype`: Peatland subtype (e.g., "raised bog")

**Desirable Fields:**
- `#pxt_site_elevation`: Elevation in meters (e.g., "5")
- `#pxt_site_vegetation`: Dominant vegetation (e.g., "Sphagnum moss")
- `#pxt_site_management`: Management status (e.g., "restored")
- `#pxt_site_condition`: Site condition assessment (e.g., "recovering")

### Event Level Tags (`#pxt_event_*`)
**Required Fields:**
- `#pxt_event_id`: Unique event identifier (e.g., "CF001_20230615_01")
- `#pxt_event_site_id`: Links to site ID (e.g., "CF001")
- `#pxt_event_date`: Event date in ISO format (e.g., "2023-06-15")
- `#pxt_recorded_by`: Observer name (e.g., "A Smith")

**Desirable Fields:**
- `#pxt_event_time`: Event time in 24hr format (e.g., "14:30")
- `#pxt_weather`: Weather conditions (e.g., "Clear, dry, light breeze")
- `#pxt_equipment`: Equipment used (e.g., "GPS unit, peat auger")
- `#pxt_sampling_effort`: Sampling intensity (e.g., "2 hours, 10 measurement points")

### Dataset Level Tags (`#pxt_dataset_*`)
**Required Fields:**
- `#pxt_dataset_id`: Unique dataset identifier (e.g., "WALES_PEAT_RESTORATION_2023")
- `#pxt_dataset_title`: Descriptive title
- `#pxt_dataset_description`: Detailed description for reuse
- `#pxt_dataset_keywords`: Search keywords (e.g., "peatland, restoration, bog, Wales")
- `#pxt_dataset_contact_name`: Primary contact person (e.g., "Dr Alice Smith")
- `#pxt_dataset_temporal`: Time coverage (e.g., "2021-01-01/2023-12-31")

**Desirable Fields:**
- `#pxt_dataset_funding`: Funding source with grant numbers
- `#pxt_dataset_pi`: Principal investigator
- `#pxt_dataset_qa`: Quality assurance procedures

## Target Use Cases

### 1. Metadata Standardization
- Apply standardized PXT tags to site information (`#pxt_site_id`, `#pxt_site_lat`, `#pxt_site_lon`)
- Tag observation events consistently (`#pxt_event_id`, `#pxt_event_date`, `#pxt_recorded_by`)
- Standardize dataset descriptions (`#pxt_dataset_title`, `#pxt_dataset_abstract`, `#pxt_dataset_keywords`)
- Ensure geographic and temporal coverage metadata follows standard formats

### 2. Metadata Quality Control
- Validate Required fields are present (`#pxt_site_id`, `#pxt_event_date`, `#pxt_dataset_title`)
- Check Desirable fields for completeness (`#pxt_site_elevation`, `#pxt_event_time`, `#pxt_dataset_funding`)
- Validate coordinate formats and datum specifications (`#pxt_site_datum`)
- Ensure consistent ID linking between site and event data (`#pxt_event_site_id`)

### 3. Hierarchical Data Integration
- Link observation events to site metadata through consistent IDs
- Merge datasets using standardized site and event identifiers
- Integrate multi-temporal data from the same sites over time
- Cross-reference with controlled vocabularies for peatland types and management status

### 4. Data Exchange Facilitation
- Enable seamless data transfer between research systems
- Standardize outputs for integration with existing repositories
- Support researchers' own data storage and management workflows
- Maintain data privacy by processing without permanent storage

## Core Workflow (Adapted from HXL Proxy)

### 1. Source Selection Page
**Supported Sources:**
- File upload (CSV, Excel, JSON)
- URL-based data feeds
- Integration with research data repositories
- Cloud storage connections (Google Drive, OneDrive, Dropbox)
- **No Permanent Storage**: All data processing is temporary and session-based

### 2. PXT Tagging Page
**Three-Level Metadata Tagging:**
- **Site Level Tagging**: Apply site tags (`#pxt_site_id`, `#pxt_site_lat`, `#pxt_site_lon`, `#pxt_site_type`)
- **Event Level Tagging**: Tag observation events (`#pxt_event_id`, `#pxt_event_date`, `#pxt_recorded_by`)
- **Dataset Level Tagging**: Apply collection metadata (`#pxt_dataset_title`, `#pxt_dataset_description`, `#pxt_dataset_keywords`)
- **Field Priority Indication**: Mark Required vs Desirable vs Optional fields
- **Validation Rules**: Apply format requirements (ISO dates, coordinate formats, controlled vocabularies)

### 3. Metadata Processing Pipeline
**Available Metadata Transformations:**
- **ID Generation**: Create consistent site and event IDs following PXT conventions
- **Date Standardization**: Convert dates to ISO 8601 format (`#pxt_event_date`)
- **Coordinate Validation**: Verify lat/lon formats and datum specifications (`#pxt_site_datum`)
- **Controlled Vocabulary**: Map to standard peatland types and conditions
- **Hierarchy Linking**: Ensure event-to-site ID consistency (`#pxt_event_site_id`)
- **Required Field Checking**: Flag missing Required metadata fields
- **Contact Information**: Standardize researcher and organization details
- **Geographic Coverage**: Generate coverage strings from coordinate data

### 4. Output & Export Page
**Export Options:**
- Standardized CSV with PXT tags embedded
- JSON-LD with PXT semantic annotations
- Tagged datasets ready for integration with researcher's chosen systems
- Metadata packages with tag definitions and provenance
- **Immediate Download**: No server-side storage of processed data

## Technical Requirements

### Performance Targets
- Handle datasets up to 100,000 rows efficiently
- Support real-time processing for monitoring data streams
- Maintain sub-second response times for common transformations
- **Ephemeral Processing**: All operations in memory or temporary storage

### Data Standards Compliance
- Implement PXT tagging standards for peatland data exchange
- Support FAIR data principles through consistent semantic tagging
- Maintain compatibility with existing environmental data formats
- Enable semantic web integration through PXT linked data tags

### Security & Privacy
- **No Permanent Data Storage**: All data is processed temporarily and cleared
- Secure handling of sensitive location data during processing
- Session-based processing with automatic cleanup
- Compliance with research data governance policies through non-retention

## Key Differentiators from HXL Proxy

### Peatland-Specific Tag Hierarchy
- **Three-level metadata structure**: Site → Event → Dataset relationships
- **67 standardized PXT tags**: From `#pxt_site_id` to `#pxt_dataset_qa`
- **Field priority system**: Required, Desirable, and Optional classifications
- **Domain-specific validation**: Peatland type vocabularies, coordinate systems, temporal formats

### Research Metadata Features
- **Comprehensive provenance**: Principal investigator, funding source, methodology tracking
- **Publication support**: DOI integration, citation metadata, quality assurance documentation
- **Collaborative standards**: Shared PXT tag vocabularies across research communities
- **Long-term preservation**: Contact information, institutional affiliations, access permissions

### Peatland Research Specialization
- **Site characterization**: Bog/fen classification, management status, restoration tracking
- **Multi-temporal tracking**: Event-based observations with consistent site linking
- **Research context**: Equipment, weather conditions, sampling effort documentation
- **Geographic precision**: Coordinate uncertainty, elevation, access information

### Data Exchange Architecture
- **Processing-only approach**: No database or permanent storage requirements
- **Researcher autonomy**: Users maintain control of their data storage decisions
- **Privacy by design**: Data never persists on the platform
- **Integration-ready**: Outputs designed for seamless integration with existing systems

## Expected Outcomes

### Data Quality Impact
- Reduction in data preparation time for practitioners and researchers
- Improvement in dataset exchangeability across platforms and institutions
- Increased data reuse across research projects through standardized formats
- Enhanced reproducibility of research findings via consistent metadata

### Community Building
- Growth of shared transformation recipe library
- Contribution of domain expertise from peatland research community
- Adoption as standard tool in peatland research workflows
- Integration with major research initiatives and databases

## Development Steps

1. **Requirements Gathering**: Workshops to engage the peatland community
2. **Technology Stack Selection**: Framework and infrastructure decisions (no-database approach)
3. **'Toy' App Definition**: Core features for initial release and community testing
4. **Prototype Development**: Basic PXT tagging and transformation pipeline
5. **Community Engagement**: Early adopter recruitment and feedback integration

## Repository Structure

This document serves as the foundation for the PXT Web App development. All subsequent development decisions should align with this vision while maintaining flexibility for community input and emerging requirements. The emphasis on data exchange rather than storage ensures the platform serves as a bridge between researcher systems rather than another data silo.
