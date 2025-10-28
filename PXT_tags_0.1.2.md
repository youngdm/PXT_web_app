# Peatland Exchange Tags (PXT) - Standard v 0.1.2

*Comprehensive reference for all PXT tags across all metadata levels*

## Overview

This document provides PXT tags for the complete peatland metadata standard, organized by metadata level:
- **Site Level**: Location and characteristics of observation sites
- **Observation Event Level**: When, how, and by whom measurements were taken
- **Dataset Level**: Overall collection information for data discovery and citation

---
## Site Metadata Tags

*Tags for site location and characteristics*
### Required Fields

| PXT Tag | Metadata Field | Example | Notes |
|---------|----------------|---------|-------|
| `#pxt_site_id` | siteID | CF001 | Keep consistent across your project. Avoid spaces or special characters |
| `#pxt_site_lat` | latitude | 52.4912 | Take at centre of site. Don't forget minus sign isn't needed for northern latitudes |
| `#pxt_site_lon` | longitude | -4.0234 | Take at centre of site. Don't forget minus sign for western longitudes! |
| `#pxt_site_datum` | geodeticDatum | WGS84 | Only change if specifically told to use different system |
| `#pxt_site_type` | peatlandType | bog | When in doubt between bog/fen: bog=rainwater fed; fen=groundwater fed |
| `#pxt_site_subtype` | peatlandSubtype | raised bog | Look up local classification guides if unsure |
### Desirable Fields (Recommended)

| PXT Tag | Metadata Field | Example | Notes |
|---------|----------------|---------|-------|
| `#pxt_site_uncertainty` | coordinateUncertainty | 10 | Smaller numbers = more accurate. Phone GPS often 3-10m |
| `#pxt_site_elevation` | elevation | 5 | Can be negative for below sea level. GPS elevation often inaccurate |
| `#pxt_site_vegetation` | dominantVegetation | Sphagnum moss | Look across the whole site - what dominates |
| `#pxt_site_management` | managementStatus | restored | Think about what's happening to the site now |
| `#pxt_site_condition` | siteCondition | recovering | Your judgement of how healthy the site looks |
| `#pxt_site_remarks` | siteRemarks | Restored in 2019 after drainage | Include anything that would help future visitors |
| `#pxt_site_established` | siteEstablishedDate | 2018-03-15 | Leave blank if you don't know. |
| `#pxt_site_establishedby` | siteEstablishedBy | A Smith | Could be person or organisation |
| `#pxt_site_access` | siteAccessNotes | Via farm track from B4353 | Help others find and access the site legally |
| `#pxt_site_owner` | landOwner | Natural Resources Wales | Useful for permissions and contacts |
| `#pxt_site_permissions` | permissionsRequired | Yes | Simple yes/no - helps others know what's required |
### Optional Fields (Supplementary)

| PXT Tag | Metadata Field | Example | Notes |
|---------|----------------|---------|-------|
| `#pxt_site_gridref` | nationalGridReference | SN 63235 91234 | UK: 2 letters + 3+3 numbers or 2+2 letters + numbers |
## Observation Event Metadata Tags

*Tags for observation events and measurements*
### Required Fields

| PXT Tag | Metadata Field | Example | Notes |
|---------|----------------|---------|-------|
| `#pxt_event_id` | eventID | CF001_20230615_01 | Must be unique across all your events. Include site ID for clarity |
| `#pxt_event_site_id` | siteID | CF001 | This links your event to site information - spelling must be exact |
| `#pxt_event_date` | eventDate | 2023-06-15 | Always use 4-digit year and 2-digit month/day with hyphens |
| `#pxt_recorded_by` | recordedBy | A Smith | Be consistent with name format across your project |
### Desirable Fields (Recommended)

| PXT Tag | Metadata Field | Example | Notes |
|---------|----------------|---------|-------|
| `#pxt_parent_event_id` | parentEventID | SUMMER_SURVEY_2023 | Use when this event is part of a coordinated larger study |
| `#pxt_event_time` | eventTime | 14:30 | Use 24-hour format. Include timezone if working across regions |
| `#pxt_event_date_precision` | eventDatePrecision | day | Helps others understand temporal resolution of your data |
| `#pxt_field_number` | fieldNumber | FB23-045 | Links to your physical field records |
| `#pxt_recorded_by_id` | recordedByID | 0000-0002-1825-0097 | ORCID is preferred for researchers. Helps with attribution |
| `#pxt_sampling_effort` | samplingEffort | 2 hours, 10 measurement points | Helps others understand data collection intensity |
| `#pxt_weather` | weatherConditions | Clear, dry, light breeze | Focus on conditions that might affect measurements |
| `#pxt_temperature` | temperature | 15.5 | Record at time of measurement, not daily average |
| `#pxt_equipment` | equipmentUsed | GPS unit, peat auger, measuring tape | Include any equipment that affects data quality |
| `#pxt_instrument_model` | instrumentModel | Garmin eTrex 32x GPS | Include model numbers for precision instruments |
| `#pxt_event_remarks` | eventRemarks | Water table unusually high due to recent rainfall | Include anything that affects data interpretation |
| `#pxt_quality_notes` | eventQualityNotes | GPS accuracy reduced by tree cover | Helps others assess data reliability |
## Dataset Metadata Tags

*Tags for overall dataset information*
### Required Fields

| PXT Tag | Metadata Field | Example | Notes |
|---------|----------------|---------|-------|
| `#pxt_dataset_id` | datasetID | WALES_PEAT_RESTORATION_2023 | Use DOI if available, otherwise create memorable unique code |
| `#pxt_dataset_title` | title | Peat depth measurements from Welsh bog restoration sites 2021-2023 | Include location, timeframe, and main measurements |
| `#pxt_dataset_description` | description | This dataset contains peat depth measurements collected monthly from 15 restored bog sites across Wales between January 2021 and December 2023, as part of a restoration effectiveness monitoring programme. | Include enough detail for others to understand and use your data |
| `#pxt_dataset_abstract` | abstract | Monthly peat depth measurements from 15 Welsh restoration sites over 3 years. Data supports evaluation of bog restoration success and carbon storage potential. | Keep concise but informative - often displayed in search results |
| `#pxt_dataset_keywords` | keywords | peatland, restoration, bog, Wales, peat depth, monitoring | Include both specific and general terms. Think about what others might search for |
| `#pxt_dataset_language` | language | en | Use standard codes when possible (en, cy, de, fr, etc.) |
| `#pxt_dataset_license` | license | CC BY 4.0 | Use standard Creative Commons or open licences where possible |
| `#pxt_dataset_rights` | rights | Copyright 2023 Welsh Government. Available under CC BY 4.0 licence. | Be clear about ownership and permitted uses |
| `#pxt_dataset_publisher` | publisher | Natural Resources Wales | May be different from data collector or copyright holder |
| `#pxt_dataset_contact_name` | contactName | Dr Alice Smith | Include title if relevant. Should be someone who will be reachable long-term |
| `#pxt_dataset_contact_email` | contactEmail | alice.smith@wales.gov.uk | Use institutional email that will persist. Consider generic addresses for long-term datasets |
| `#pxt_dataset_contact_org` | contactOrganisation | Natural Resources Wales | Full official name of organisation |
| `#pxt_dataset_geographic` | geographicCoverage | Wales, United Kingdom | Be as specific as appropriate - country, region, or global |
| `#pxt_dataset_temporal` | temporalCoverage | 2021-01-01/2023-12-31 | Use ISO 8601 format with slash for ranges. Should span from earliest to latest observation |
| `#pxt_dataset_data_type` | dataType | Physical measurements | Choose broad category that best describes your primary data type |
| `#pxt_dataset_peatland_type` | peatlandType | bog | Use standard ENVO terminology. Can list multiple types if dataset covers several |
| `#pxt_dataset_measurements` | measurementTypes | peat depth, water table depth, pH | List key variables that users might search for |
| `#pxt_dataset_methodology` | methodology | Manual peat depth measurements using graduated probe at fixed 50m grid points, recorded monthly | Include enough detail for others to understand data collection approach |
| `#pxt_dataset_pi` | principalInvestigator | Prof. Alice Smith | May be different from data contact person |
| `#pxt_dataset_qa` | qualityAssurance | Data validated through duplicate measurements at 10% of points, cross-checked with field notes | Helps users understand data reliability |
### Desirable Fields (Recommended)

| PXT Tag | Metadata Field | Example | Notes |
|---------|----------------|---------|-------|
| `#pxt_dataset_funding` | fundingSource | Welsh Government Environment Grant EG2021-45 | Include grant numbers if available. Helps with attribution and discoverability |

---

*Generated automatically from modular specification v0.1.2 on 2025-10-03*
*Master coordinator: workshop_outputs/master_metadata_coordinator.yaml*
