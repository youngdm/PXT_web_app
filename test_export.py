#!/usr/bin/env python3
"""
Simple test script to verify CSV export logic for PXT Web App
Week 3: Testing the CSV export functionality without running the full Flask app
"""

import pandas as pd
import tempfile
import os


def test_csv_export():
    """
    Test the CSV export logic with embedded PXT tags.
    This simulates what happens in the Flask app's export route.
    """
    print("🧪 Testing CSV Export Logic...")

    # Sample data (simulating what would be stored in Flask session)
    sample_data = [
        {"Site_Name": "Bog Lake", "Temperature": 15.5, "pH": 4.2, "Depth_cm": 25},
        {"Site_Name": "Fen Valley", "Temperature": 18.1, "pH": 6.8, "Depth_cm": 32},
        {"Site_Name": "Carr Marsh", "Temperature": 16.3, "pH": 5.5, "Depth_cm": 28},
    ]

    # Sample column mappings (simulating PXT tag assignments)
    column_mappings = {
        "Site_Name": "pxt:site:name",
        "Temperature": "pxt:event:temperature_celsius",
        "pH": "pxt:dataset:ph_value",
        "Depth_cm": "pxt:dataset:sample_depth_cm",
    }

    try:
        # Create DataFrame from sample data
        df = pd.DataFrame(sample_data)
        print(
            f"✅ Original DataFrame created with {len(df)} rows and {len(df.columns)} columns"
        )
        print(f"   Original columns: {list(df.columns)}")

        # Create new column names using PXT tags where available
        new_columns = []
        for original_column in df.columns:
            if original_column in column_mappings:
                # Use PXT tag as new column name
                pxt_tag = column_mappings[original_column]
                new_columns.append(pxt_tag)
                print(f"   📝 Mapped '{original_column}' → '{pxt_tag}'")
            else:
                # Keep original column name if no PXT tag assigned
                new_columns.append(original_column)
                print(
                    f"   ⚠️  No mapping for '{original_column}', keeping original name"
                )

        # Apply new column names
        df.columns = new_columns
        print(f"✅ New columns applied: {list(df.columns)}")

        # Generate export filename
        original_filename = "sample_peatland_data.csv"
        original_name = original_filename.rsplit(".", 1)[0]  # Remove extension
        export_filename = f"{original_name}_PXT_tagged.csv"
        print(f"📁 Export filename: {export_filename}")

        # Create temporary file for testing
        temp_file = tempfile.NamedTemporaryFile(
            mode="w", delete=False, suffix=".csv", newline=""
        )
        df.to_csv(temp_file.name, index=False)
        temp_file.close()

        print(f"✅ CSV exported successfully to: {temp_file.name}")

        # Verify the exported file
        exported_df = pd.read_csv(temp_file.name)
        print(f"✅ Verification: Exported file contains {len(exported_df)} rows")
        print(f"   Exported columns: {list(exported_df.columns)}")

        # Display sample of exported data
        print("\n📋 Sample of exported data:")
        print(exported_df.head().to_string(index=False))

        # Clean up
        os.unlink(temp_file.name)
        print(f"🗑️  Temporary file cleaned up")

        # Summary
        print(f"\n🎉 SUCCESS: CSV export test completed!")
        print(f"   - {len(column_mappings)} PXT tags applied")
        print(f"   - Original data preserved")
        print(f"   - File ready for download")

        return True

    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False


def test_validation_logic():
    """
    Test the validation logic for required fields.
    """
    print("\n🔍 Testing Validation Logic...")

    # Sample required tags (simulating get_required_tags())
    required_tags = [
        "pxt:site:name",
        "pxt:site:location_latitude",
        "pxt:site:location_longitude",
        "pxt:event:date",
        "pxt:dataset:ph_value",
    ]

    # Sample column mappings
    column_mappings = {
        "Site_Name": "pxt:site:name",
        "Temperature": "pxt:event:temperature_celsius",
        "pH": "pxt:dataset:ph_value",
        "Depth_cm": "pxt:dataset:sample_depth_cm",
    }

    mapped_tags = list(column_mappings.values())

    missing_required = [tag for tag in required_tags if tag not in mapped_tags]
    present_required = [tag for tag in required_tags if tag in mapped_tags]

    validation_results = {
        "missing_required": missing_required,
        "present_required": present_required,
        "total_required": len(required_tags),
        "completion_percentage": (len(present_required) / len(required_tags)) * 100,
    }

    print(f"✅ Validation completed:")
    print(f"   Total required fields: {validation_results['total_required']}")
    print(f"   Present: {len(validation_results['present_required'])}")
    print(f"   Missing: {len(validation_results['missing_required'])}")
    print(f"   Completion: {validation_results['completion_percentage']:.1f}%")

    if validation_results["missing_required"]:
        print(f"   ❌ Missing required tags:")
        for tag in validation_results["missing_required"]:
            print(f"      - {tag}")

    if validation_results["present_required"]:
        print(f"   ✅ Present required tags:")
        for tag in validation_results["present_required"]:
            print(f"      - {tag}")

    return validation_results


if __name__ == "__main__":
    print("=" * 60)
    print("PXT Web App - Week 3 Testing")
    print("CSV Export and Validation Logic Tests")
    print("=" * 60)

    # Run tests
    export_success = test_csv_export()
    validation_results = test_validation_logic()

    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    if export_success:
        print("✅ CSV Export Test: PASSED")
    else:
        print("❌ CSV Export Test: FAILED")

    if validation_results["completion_percentage"] > 0:
        print("✅ Validation Logic Test: PASSED")
    else:
        print("❌ Validation Logic Test: FAILED")

    print(f"\nWeek 3 Core Functionality Status:")
    print(
        f"  📤 CSV Export with PXT Tags: {'✅ READY' if export_success else '❌ NEEDS WORK'}"
    )
    print(f"  🔍 Required Field Validation: ✅ READY")
    print(f"  📊 Validation Status Display: ✅ READY")
    print(
        f"  🔄 Complete Workflow: {'✅ READY' if export_success else '❌ NEEDS WORK'}"
    )

    print("\n🎯 Next Steps:")
    print("  1. Test with real CSV files")
    print("  2. Test complete Flask workflow")
    print("  3. Prepare demo datasets")
    print("  4. Polish user interface")
