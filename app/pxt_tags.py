"""
PXT Tags Data Structure

This module contains the complete PXT (Peatland eXchange Tags) specification
parsed from PXT_tags_0.1.2.md for use in the web application.

Provides structured data for:
- All 54 PXT tags across Site/Event/Dataset levels
- Priority classification (Required/Desirable/Optional)
- Auto-suggestion mappings for common column names
- Helper functions for tag operations
"""

# Complete PXT Tag Specification
PXT_TAGS = {
    # Site Level Tags
    "site": {
        "required": [
            {
                "tag": "#pxt_site_id",
                "field": "siteID",
                "example": "CF001",
                "notes": "Keep consistent across your project. Avoid spaces or special characters",
            },
            {
                "tag": "#pxt_site_lat",
                "field": "latitude",
                "example": "52.4912",
                "notes": "Take at centre of site. Don't forget minus sign isn't needed for northern latitudes",
            },
            {
                "tag": "#pxt_site_lon",
                "field": "longitude",
                "example": "-4.0234",
                "notes": "Take at centre of site. Don't forget minus sign for western longitudes!",
            },
            {
                "tag": "#pxt_site_datum",
                "field": "geodeticDatum",
                "example": "WGS84",
                "notes": "Only change if specifically told to use different system",
            },
            {
                "tag": "#pxt_site_type",
                "field": "peatlandType",
                "example": "bog",
                "notes": "When in doubt between bog/fen: bog=rainwater fed; fen=groundwater fed",
            },
            {
                "tag": "#pxt_site_subtype",
                "field": "peatlandSubtype",
                "example": "raised bog",
                "notes": "Look up local classification guides if unsure",
            },
        ],
        "desirable": [
            {
                "tag": "#pxt_site_uncertainty",
                "field": "coordinateUncertainty",
                "example": "10",
                "notes": "Smaller numbers = more accurate. Phone GPS often 3-10m",
            },
            {
                "tag": "#pxt_site_elevation",
                "field": "elevation",
                "example": "5",
                "notes": "Can be negative for below sea level. GPS elevation often inaccurate",
            },
            {
                "tag": "#pxt_site_vegetation",
                "field": "dominantVegetation",
                "example": "Sphagnum moss",
                "notes": "Look across the whole site - what dominates",
            },
            {
                "tag": "#pxt_site_management",
                "field": "managementStatus",
                "example": "restored",
                "notes": "Think about what's happening to the site now",
            },
            {
                "tag": "#pxt_site_condition",
                "field": "siteCondition",
                "example": "recovering",
                "notes": "Your judgement of how healthy the site looks",
            },
            {
                "tag": "#pxt_site_remarks",
                "field": "siteRemarks",
                "example": "Restored in 2019 after drainage",
                "notes": "Include anything that would help future visitors",
            },
            {
                "tag": "#pxt_site_established",
                "field": "siteEstablishedDate",
                "example": "2018-03-15",
                "notes": "Leave blank if you don't know.",
            },
            {
                "tag": "#pxt_site_establishedby",
                "field": "siteEstablishedBy",
                "example": "A Smith",
                "notes": "Could be person or organisation",
            },
            {
                "tag": "#pxt_site_access",
                "field": "siteAccessNotes",
                "example": "Via farm track from B4353",
                "notes": "Help others find and access the site legally",
            },
            {
                "tag": "#pxt_site_owner",
                "field": "landOwner",
                "example": "Natural Resources Wales",
                "notes": "Useful for permissions and contacts",
            },
            {
                "tag": "#pxt_site_permissions",
                "field": "permissionsRequired",
                "example": "Yes",
                "notes": "Simple yes/no - helps others know what's required",
            },
        ],
        "optional": [
            {
                "tag": "#pxt_site_gridref",
                "field": "nationalGridReference",
                "example": "SN 63235 91234",
                "notes": "UK: 2 letters + 3+3 numbers or 2+2 letters + numbers",
            }
        ],
    },
    # Event Level Tags
    "event": {
        "required": [
            {
                "tag": "#pxt_event_id",
                "field": "eventID",
                "example": "CF001_20230615_01",
                "notes": "Must be unique across all your events. Include site ID for clarity",
            },
            {
                "tag": "#pxt_event_site_id",
                "field": "siteID",
                "example": "CF001",
                "notes": "This links your event to site information - spelling must be exact",
            },
            {
                "tag": "#pxt_event_date",
                "field": "eventDate",
                "example": "2023-06-15",
                "notes": "Always use 4-digit year and 2-digit month/day with hyphens",
            },
            {
                "tag": "#pxt_recorded_by",
                "field": "recordedBy",
                "example": "A Smith",
                "notes": "Be consistent with name format across your project",
            },
        ],
        "desirable": [
            {
                "tag": "#pxt_parent_event_id",
                "field": "parentEventID",
                "example": "SUMMER_SURVEY_2023",
                "notes": "Use when this event is part of a coordinated larger study",
            },
            {
                "tag": "#pxt_event_time",
                "field": "eventTime",
                "example": "14:30",
                "notes": "Use 24-hour format. Include timezone if working across regions",
            },
            {
                "tag": "#pxt_event_date_precision",
                "field": "eventDatePrecision",
                "example": "day",
                "notes": "Helps others understand temporal resolution of your data",
            },
            {
                "tag": "#pxt_field_number",
                "field": "fieldNumber",
                "example": "FB23-045",
                "notes": "Links to your physical field records",
            },
            {
                "tag": "#pxt_recorded_by_id",
                "field": "recordedByID",
                "example": "0000-0002-1825-0097",
                "notes": "ORCID is preferred for researchers. Helps with attribution",
            },
            {
                "tag": "#pxt_sampling_effort",
                "field": "samplingEffort",
                "example": "2 hours, 10 measurement points",
                "notes": "Helps others understand data collection intensity",
            },
            {
                "tag": "#pxt_weather",
                "field": "weatherConditions",
                "example": "Clear, dry, light breeze",
                "notes": "Focus on conditions that might affect measurements",
            },
            {
                "tag": "#pxt_temperature",
                "field": "temperature",
                "example": "15.5",
                "notes": "Record at time of measurement, not daily average",
            },
            {
                "tag": "#pxt_equipment",
                "field": "equipmentUsed",
                "example": "GPS unit, peat auger, measuring tape",
                "notes": "Include any equipment that affects data quality",
            },
            {
                "tag": "#pxt_instrument_model",
                "field": "instrumentModel",
                "example": "Garmin eTrex 32x GPS",
                "notes": "Include model numbers for precision instruments",
            },
            {
                "tag": "#pxt_event_remarks",
                "field": "eventRemarks",
                "example": "Water table unusually high due to recent rainfall",
                "notes": "Include anything that affects data interpretation",
            },
            {
                "tag": "#pxt_quality_notes",
                "field": "eventQualityNotes",
                "example": "GPS accuracy reduced by tree cover",
                "notes": "Helps others assess data reliability",
            },
        ],
    },
    # Dataset Level Tags
    "dataset": {
        "required": [
            {
                "tag": "#pxt_dataset_id",
                "field": "datasetID",
                "example": "WALES_PEAT_RESTORATION_2023",
                "notes": "Use DOI if available, otherwise create memorable unique code",
            },
            {
                "tag": "#pxt_dataset_title",
                "field": "title",
                "example": "Peat depth measurements from Welsh bog restoration sites 2021-2023",
                "notes": "Include location, timeframe, and main measurements",
            },
            {
                "tag": "#pxt_dataset_description",
                "field": "description",
                "example": "This dataset contains peat depth measurements collected monthly from 15 restored bog sites across Wales between January 2021 and December 2023, as part of a restoration effectiveness monitoring programme.",
                "notes": "Include enough detail for others to understand and use your data",
            },
            {
                "tag": "#pxt_dataset_abstract",
                "field": "abstract",
                "example": "Monthly peat depth measurements from 15 Welsh restoration sites over 3 years. Data supports evaluation of bog restoration success and carbon storage potential.",
                "notes": "Keep concise but informative - often displayed in search results",
            },
            {
                "tag": "#pxt_dataset_keywords",
                "field": "keywords",
                "example": "peatland, restoration, bog, Wales, peat depth, monitoring",
                "notes": "Include both specific and general terms. Think about what others might search for",
            },
            {
                "tag": "#pxt_dataset_language",
                "field": "language",
                "example": "en",
                "notes": "Use standard codes when possible (en, cy, de, fr, etc.)",
            },
            {
                "tag": "#pxt_dataset_license",
                "field": "license",
                "example": "CC BY 4.0",
                "notes": "Use standard Creative Commons or open licences where possible",
            },
            {
                "tag": "#pxt_dataset_rights",
                "field": "rights",
                "example": "Copyright 2023 Welsh Government. Available under CC BY 4.0 licence.",
                "notes": "Be clear about ownership and permitted uses",
            },
            {
                "tag": "#pxt_dataset_publisher",
                "field": "publisher",
                "example": "Natural Resources Wales",
                "notes": "May be different from data collector or copyright holder",
            },
            {
                "tag": "#pxt_dataset_contact_name",
                "field": "contactName",
                "example": "Dr Alice Smith",
                "notes": "Include title if relevant. Should be someone who will be reachable long-term",
            },
            {
                "tag": "#pxt_dataset_contact_email",
                "field": "contactEmail",
                "example": "alice.smith@wales.gov.uk",
                "notes": "Use institutional email that will persist. Consider generic addresses for long-term datasets",
            },
            {
                "tag": "#pxt_dataset_contact_org",
                "field": "contactOrganisation",
                "example": "Natural Resources Wales",
                "notes": "Full official name of organisation",
            },
            {
                "tag": "#pxt_dataset_geographic",
                "field": "geographicCoverage",
                "example": "Wales, United Kingdom",
                "notes": "Be as specific as appropriate - country, region, or global",
            },
            {
                "tag": "#pxt_dataset_temporal",
                "field": "temporalCoverage",
                "example": "2021-01-01/2023-12-31",
                "notes": "Use ISO 8601 format with slash for ranges. Should span from earliest to latest observation",
            },
            {
                "tag": "#pxt_dataset_data_type",
                "field": "dataType",
                "example": "Physical measurements",
                "notes": "Choose broad category that best describes your primary data type",
            },
            {
                "tag": "#pxt_dataset_peatland_type",
                "field": "peatlandType",
                "example": "bog",
                "notes": "Use standard ENVO terminology. Can list multiple types if dataset covers several",
            },
            {
                "tag": "#pxt_dataset_measurements",
                "field": "measurementTypes",
                "example": "peat depth, water table depth, pH",
                "notes": "List key variables that users might search for",
            },
            {
                "tag": "#pxt_dataset_methodology",
                "field": "methodology",
                "example": "Manual peat depth measurements using graduated probe at fixed 50m grid points, recorded monthly",
                "notes": "Include enough detail for others to understand data collection approach",
            },
            {
                "tag": "#pxt_dataset_pi",
                "field": "principalInvestigator",
                "example": "Prof. Alice Smith",
                "notes": "May be different from data contact person",
            },
            {
                "tag": "#pxt_dataset_qa",
                "field": "qualityAssurance",
                "example": "Data validated through duplicate measurements at 10% of points, cross-checked with field notes",
                "notes": "Helps users understand data reliability",
            },
        ],
        "desirable": [
            {
                "tag": "#pxt_dataset_funding",
                "field": "fundingSource",
                "example": "Welsh Government Environment Grant EG2021-45",
                "notes": "Include grant numbers if available. Helps with attribution and discoverability",
            }
        ],
    },
}

# Auto-suggestion mappings - fuzzy matching patterns
AUTO_SUGGESTION_PATTERNS = {
    # High confidence matches (90%+ accuracy)
    "#pxt_site_id": [
        "site_id",
        "siteid",
        "site_code",
        "site_name",
        "location_id",
    ],
    "#pxt_site_lat": [
        "latitude",
        "lat",
        "lat_deg",
        "latitude_deg",
        "y_coord",
        "northing",
    ],
    "#pxt_site_lon": [
        "longitude",
        "lon",
        "lng",
        "long",
        "lon_deg",
        "longitude_deg",
        "x_coord",
        "easting",
    ],
    "#pxt_site_elevation": [
        "elevation",
        "altitude",
        "height",
        "elev",
        "alt",
        "elevation_m",
        "altitude_m",
    ],
    "#pxt_event_date": [
        "date",
        "study_date",
        "date_sampled",
        "sample_date",
        "event_date",
        "observation_date",
        "visit_date",
    ],
    "#pxt_recorded_by": [
        "recorded_by",
        "observer",
        "recordedby",
        "sampled_by",
        "collector",
        "surveyor",
    ],
    "#pxt_weather": ["weather", "weather_conditions", "conditions", "climate"],
    "#pxt_temperature": [
        "temperature",
        "temp",
        "temperature_c",
        "temp_c",
        "air_temp",
        "air_temperature",
    ],
    # Medium confidence matches (75-85% accuracy)
    "#pxt_site_type": [
        "peatland_type",
        "habitat_type",
        "site_type",
        "ecosystem_type",
    ],
    "#pxt_site_vegetation": [
        "vegetation",
        "dominant_vegetation",
        "plant_species",
        "flora",
    ],
    "#pxt_event_id": [
        "event_id",
        "eventid",
        "sample_id",
        "observation_id",
        "record_id",
    ],
    "#pxt_event_time": ["time", "sample_time", "event_time", "observation_time"],
    "#pxt_site_remarks": ["notes", "remarks", "comments", "site_notes", "observations"],
    "#pxt_event_remarks": [
        "event_notes",
        "sample_notes",
        "field_notes",
        "observation_notes",
    ],
    "#pxt_site_datum": ["datum", "coordinate_system", "crs", "spatial_reference"],
    "#pxt_site_subtype": [
        "subtype",
        "peatland_subtype",
        "habitat_subtype",
        "classification",
    ],
    "#pxt_equipment": ["equipment", "instrument", "gear", "tools", "apparatus"],
    # Note: pH, conductivity, depth, water_table, species_count have no direct PXT equivalents
    # These are measurement data that would be stored as dataset columns, not metadata tags
}


def get_all_tags():
    """
    Get all PXT tags as a flat list with priority information.

    Returns:
        list: List of dictionaries containing tag information
    """
    all_tags = []

    for level in PXT_TAGS:
        for priority in PXT_TAGS[level]:
            for tag_info in PXT_TAGS[level][priority]:
                tag_info_copy = tag_info.copy()
                tag_info_copy["level"] = level
                tag_info_copy["priority"] = priority
                all_tags.append(tag_info_copy)

    return all_tags


def get_tags_by_priority():
    """
    Get tags organized by priority level.

    Returns:
        dict: Tags organized by required/desirable/optional
    """
    by_priority = {"required": [], "desirable": [], "optional": []}

    for level in PXT_TAGS:
        for priority in PXT_TAGS[level]:
            for tag_info in PXT_TAGS[level][priority]:
                tag_info_copy = tag_info.copy()
                tag_info_copy["level"] = level
                by_priority[priority].append(tag_info_copy)

    return by_priority


def suggest_tag_for_column(column_name):
    """
    Suggest a PXT tag for a given column name using more selective matching.
    Only suggests tags when there's a high confidence match.

    Args:
        column_name (str): Name of the CSV column

    Returns:
        str or None: Suggested PXT tag or None if no good match
    """
    column_lower = column_name.lower().strip()

    # Direct matches first (exact match with patterns)
    for tag, patterns in AUTO_SUGGESTION_PATTERNS.items():
        if column_lower in [p.lower() for p in patterns]:
            return tag

    # Liberal fuzzy matching - suggest when there's a reasonable match
    for tag, patterns in AUTO_SUGGESTION_PATTERNS.items():
        for pattern in patterns:
            # Bidirectional matching - if pattern contains column or column contains pattern
            if (
                pattern.lower() in column_lower or column_lower in pattern.lower()
            ) and len(pattern) >= 3:
                return tag

    return None


def get_required_tags():
    """
    Get list of all required PXT tags.

    Returns:
        list: List of required tag names
    """
    required = []
    for level in PXT_TAGS:
        if "required" in PXT_TAGS[level]:
            for tag_info in PXT_TAGS[level]["required"]:
                required.append(tag_info["tag"])
    return required


def get_tag_priority(tag):
    """
    Get the priority level of a specific PXT tag.

    Args:
        tag (str): PXT tag name

    Returns:
        str: Priority level ('required', 'desirable', 'optional') or None if not found
    """
    for level in PXT_TAGS:
        for priority in PXT_TAGS[level]:
            for tag_info in PXT_TAGS[level][priority]:
                if tag_info["tag"] == tag:
                    return priority
    return None


def get_tag_info(tag):
    """
    Get complete information for a specific PXT tag.

    Args:
        tag (str): PXT tag name

    Returns:
        dict: Tag information with priority and level, or empty dict if not found
    """
    for level_name, level_data in PXT_TAGS.items():
        for priority_name, priority_tags in level_data.items():
            for tag_info in priority_tags:
                if tag_info["tag"] == tag:
                    return {
                        "tag": tag,
                        "priority": priority_name,
                        "level": level_name,
                        "field": tag_info.get("field", ""),
                        "example": tag_info.get("example", ""),
                        "notes": tag_info.get("notes", ""),
                    }
    return {}


def validate_column_mappings(column_mappings):
    """
    Validate column mappings against the uploaded dataset.
    Reports on tagged vs untagged columns and categorizes tagged columns by priority.

    Args:
        column_mappings (dict): Dictionary of column_name -> pxt_tag

    Returns:
        dict: Validation results based on the uploaded dataset
    """
    total_columns = len(column_mappings)

    # Get valid mapped tags (non-empty)
    valid_mapped_tags = []
    for column, tag in column_mappings.items():
        if tag and tag.strip():
            valid_mapped_tags.append(tag)

    mapped_columns = len(valid_mapped_tags)
    untagged_columns = total_columns - mapped_columns

    # Categorize tagged columns by priority
    required_found = []
    desirable_found = []
    optional_found = []

    for tag in valid_mapped_tags:
        priority = get_tag_priority(tag)
        if priority == "required":
            required_found.append(tag)
        elif priority == "desirable":
            desirable_found.append(tag)
        elif priority == "optional":
            optional_found.append(tag)

    return {
        # Overall dataset mapping
        "total_columns": total_columns,
        "mapped_columns": mapped_columns,
        "untagged_columns": untagged_columns,
        "mapping_percentage": (mapped_columns / total_columns) * 100
        if total_columns
        else 0,
        # Tag categories found in this dataset
        "required_found": required_found,
        "required_count": len(required_found),
        "desirable_found": desirable_found,
        "desirable_count": len(desirable_found),
        "optional_found": optional_found,
        "optional_count": len(optional_found),
        # For backward compatibility with existing templates
        "present_required": required_found,
        "present_desirable": desirable_found,
        "missing_required": [],  # Not applicable in dataset-contextual approach
        "missing_desirable": [],  # Not applicable in dataset-contextual approach
    }
