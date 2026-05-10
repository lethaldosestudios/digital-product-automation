#!/usr/bin/env python3
"""
Quickstart - Generate all sample outputs for Etsy listings
Run this once to create all preview files and product samples
"""

import os
import sys
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from preschool_number_generator import NumberWorksheetGenerator
from homeschool_budget_generator import BudgetSpreadsheetGenerator

def main():
    print("=" * 60)
    print("DIGITAL PRODUCT AUTOMATION - QUICKSTART")
    print("Generating all sample outputs for Etsy listings...\n")

    # Create samples directory
    samples_dir = "./samples_for_etsy"
    os.makedirs(samples_dir, exist_ok=True)

    # 1. Generate Preschool Samples
    print("1. Generating preschool worksheet samples...")
    preschool_gen = NumberWorksheetGenerator("./samples_for_etsy/preschool")
    os.makedirs("./samples_for_etsy/preschool", exist_ok=True)

    # Numbers 1-3 bundle (small sample for listing)
    preschool_files = preschool_gen.generate_bundle([1, 2, 3], "SampleChild")
    print(f"   Created {len(preschool_files)} preschool files")
    for f in preschool_files:
        print(f"     - {f}")

    # 2. Generate Budget Samples
    print("\n2. Generating homeschool budget samples...")
    budget_gen = BudgetSpreadsheetGenerator("./samples_for_etsy/budgets")
    os.makedirs("./samples_for_etsy/budgets", exist_ok=True)

    budget_files = budget_gen.generate_full_homeschool_bundle("Sample Family")
    print(f"   Created {len(budget_files)} budget files")
    for f in budget_files:
        print(f"     - {f}")

    # 3. Create README for samples
    print("\n3. Creating sample README...")
    readme_content = """# Sample Files for Etsy Listings

These files demonstrate the quality and format of products you'll deliver to customers.

## Preschool Worksheets
Location: `preschool/`

- `bundle_cover_SampleChild.pdf` - Cover page shown in listing
- `number_1_tracing_SampleChild.pdf` - Example of tracing worksheet
- `find_number_1.pdf` - Example of recognition game
- `counting_1_to_10.pdf` - Example of counting practice

**For listing images:** Open these PDFs and take screenshots of individual pages.

## Budget Spreadsheets
Location: `budgets/`

- `homeschool_monthly_budget_Sample_Family.xlsx` - Main product
- `homeschool_annual_budget_Sample_Family.xlsx` - Summary view
- `curriculum_tracker_Sample_Family.xlsx` - Purchase tracking

**For listing images:** Open in Excel/Google Sheets, screenshot full tables.

---

Take screenshots of these files, upload to Canva, add text overlays like:
- "20+ Pages"
- "Instant Download"
- "Reusable"
- "Professional Design"

Then export as 2000x2000px images for Etsy.
"""
    with open(f"{samples_dir}/README.txt", 'w') as f:
        f.write(readme_content)

    print(f"   Created {samples_dir}/README.txt")

    # 4. Create product listing cheat sheet
    print("\n4. Creating listing content summary...")
    listing_summary = """
==============================================
ETSYS LISTING CONTENT QUICK REFERENCE
==============================================

PRODUCT 1: Numbers 1-10 Bundle
Price: $11.99
Title: Number Tracing Worksheets 1-10 Bundle | Preschool Math Practice | Instant Download | Homeschool Curriculum
Tags: number tracing, preschool worksheets, kindergarten math, homeschool curriculum, instant download, printable worksheets, math practice, learn numbers, preschool curriculum, number recognition, early math, homeschooling, digital download

PRODUCT 2: Numbers 11-20 Extension
Price: $9.99
Title: Number Worksheets 11-20 | Tracing & Recognition | Sequel to 1-10 Bundle | Preschool Kindergarten Math
Tags: number tracing 11-20, teen numbers, preschool math extension, kindergarten worksheets, number recognition, instant download, printable math, homeschool math, learning numbers, preschool, kindergarten, math practice, digital download

PRODUCT 3: Complete Numbers 1-20 Bundle
Price: $18.99
Title: Complete Number Tracing Bundle 1-20 | Preschool Kindergarten Math | 35+ Pages | Save 20% vs Buying Separately
Tags: number tracing 1-20, complete math bundle, preschool curriculum, kindergarten ready, homeschool math, instant download, learning numbers, printable worksheets, number recognition, math practice, preschool bundle, kindergarten bundle, digital download

PRODUCT 4: Monthly Homeschool Budget Spreadsheet
Price: $12.99
Title: Homeschool Budget Spreadsheet | Google Sheets Excel Template | Monthly Expense Tracker | Curriculum Costs
Tags: homeschool budget, spreadsheet template, Google Sheets, Excel template, expense tracker, homeschool finances, budget planning, curriculum costs, monthly budget, homeschool organization, digital planner, homeschool help, instant download

PRODUCT 5: Complete Finance Bundle
Price: $24.99
Title: Homeschool Budget Bundle | Monthly + Annual + Curriculum Tracker | Excel Google Sheets | Finance Pack
Tags: homeschool finance bundle, budget spreadsheet, curriculum tracker, Excel template, Google Sheets, homeschool organization, expense tracking, annual budget, homeschool money management, instant download, digital planner, homeschool bundle, curriculum costs

==============================================
NEXT STEPS
==============================================

1. Create Etsy seller account
2. Take screenshots of sample files in samples_for_etsy/
3. Upload images to Canva, add branding/text overlays
4. Copy-paste listings from LISTING_TEMPLATES.md
5. Set prices (use recommended or adjust ±10% after checking competitors)
6. Publish 3-5 listings to start
7. Monitor impressions daily first week

Expected first sale: 7-14 days after publishing with good SEO.

Need help? Check README.md for full documentation.
"""
    with open(f"{samples_dir}/LISTING_CHEAT_SHEET.txt", 'w') as f:
        f.write(listing_summary)

    print(f"   Created {samples_dir}/LISTING_CHEAT_SHEET.txt")

    print("\n" + "=" * 60)
    print("✅ SAMPLES GENERATED SUCCESSFULLY!")
    print("=" * 60)
    print(f"\nAll sample files are in: {samples_dir}/")
    print("\nNext actions:")
    print("1. Open the sample PDFs/Excel files to verify quality")
    print("2. Take screenshots for listing images")
    print("3. Review LISTING_TEMPLATES.md for copy-paste listings")
    print("4. Read PROJECT_STATUS.md for execution plan")
    print("\nReady to launch. 🚀\n")

if __name__ == "__main__":
    main()