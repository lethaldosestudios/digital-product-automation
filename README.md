# Digital Product Automation Project - SLABS Innovation

**Status:** Phase 2 Complete - MVP Generators Built | Ready for Phase 3 (Etsy Setup)

**Project Goal:** Launch automated digital product store on Etsy selling preschool worksheets and homeschool budget spreadsheets with zero manual fulfillment.

**Timeline:** First listing ready immediately (this package). Etsy account setup → live listings → first sale within 2-3 weeks.

---

## What's Included

### 1. Preschool Number Worksheet Generator (`preschool_number_generator.py`)

Generates PDF worksheets for numbers 1-20:
- Number tracing practice (guided + independent)
- "Find the number" recognition games
- Counting practice sheets
- Customizable with child's name
- Full bundles with covers and tips

**Dependencies:** `fpdf2` (`pip install fpdf2`)

**Example output:** `output_worksheets/` (12+ pages per bundle)

### 2. Homeschool Budget Spreadsheet Generator (`homeschool_budget_generator.py`)

Generates Excel/Google Sheets budget templates:
- Monthly budget with homeschool-specific categories
- Annual budget overview with monthly breakdowns
- Curriculum purchase tracker
- Pre-built formulas, no Excel skills needed

**Dependencies:** `openpyxl` (`pip install openpyxl`)

**Example output:** `output_budgets/` (3 files per bundle)

### 3. Automation Server (`automation_server.py`)

Unified entry point for order processing:
- `generate_preschool_order()` - customizes PDFs on demand
- `generate_budget_order()` - creates spreadsheets with family name
- `webhook_handler()` - skeleton for Etsy/Gumroad integration (future)

**Quick Test:** `python3 automation_server.py` generates both product types.

### 4. Etsy Listing Templates (`LISTING_TEMPLATES.md`)

Copy-paste ready content for 5 listings:
- Numbers 1-10 bundle ($11.99)
- Numbers 11-20 extension ($9.99)
- Complete numbers 1-20 bundle ($18.99)
- Monthly homeschool budget ($12.99)
- Complete finance bundle ($24.99)

Each includes: optimized title, description, 13 tags, pricing strategy, image requirements.

---

## Quick Start

### 1. Install Dependencies

```bash
cd "/home/workspace/Digital_Product_Automation"
pip install fpdf2 openpyxl
```

### 2. Test the Generators

```bash
# Test preschool worksheets
python3 preschool_number_generator.py

# Test budget spreadsheets
python3 homeschool_budget_generator.py

# Test automation server (both)
python3 automation_server.py
```

Output files appear in:
- `./output_worksheets/` (PDFs)
- `./output_budgets/` (Excel files)

### 3. Generate Custom Products

```python
from automation_server import AutomationServer

server = AutomationServer()

# Generate a custom preschool bundle for "Sophie" with numbers 1-15
preschool_order = {
    "customer_name": "Parent Name",
    "child_name": "Sophie",
    "numbers": list(range(1, 16)),
    "product_type": "number_bundle",
    "order_id": "PRE-001"
}
result = server.generate_preschool_order(preschool_order)
print(result["files"])  # List of generated file paths

# Generate a budget spreadsheet for "Johnson Family"
budget_order = {
    "customer_name": "Sarah Johnson",
    "family_name": "Johnson Family",
    "product_type": "full_bundle",
    "year": 2025,
    "order_id": "BUD-001"
}
result = server.generate_budget_order(budget_order)
```

---

## Phase 3: Etsy Setup (Requires You)

### Step 1: Create Etsy Seller Account

1. Go to [etsy.com](https://www.etsy.com) and click "Sell on Etsy"
2. Choose shop preferences (language, country, currency)
3. Set up shop name (suggestions below)
4. Add payment method (bank account for deposits)
5. Set up billing (credit card for listing fees - $0.20 per listing)
6. Add shop policies (returns, shipping, etc. - for digital products set "No returns" and processing time "1-2 days" for instant downloads)

**Shop Name Ideas:**
- PrintableLearningCo
- EarlyMathPrintables
- HomeschoolBudgetShop
- SimplePrintablesCo
- LearningBundleHQ

### Step 2: Create Listings

1. Click "Add listing" in your Etsy dashboard
2. Upload product images (screenshots from generated files)
3. Copy-paste title, description, tags from `LISTING_TEMPLATES.md`
4. Set price (start with recommended prices, adjust after 10 sales based on demand)
5. Category selection: See "Category Selection" section in LISTING_TEMPLATES.md
6. Item type: "Digital download"
7. Upload sample file (include first page or preview)
8. Publish!

### Step 3: Initial Listings (Launch with 5-7 Products)

- **Preschool line (3 listings):** Numbers 1-10, 11-20, Complete 1-20
- **Budget line (2 listings):** Monthly Budget, Complete Bundle

You can add the curriculum tracker later as a standalone or as part of bundle.

### Step 4: Handle Orders Manually (Initially)

For first 20-50 sales:
1. Check Etsy dashboard for new orders
2. Note customer name (and child name if provided in "notes to seller")
3. Run appropriate generator command locally:
   ```bash
   python3 automation_server.py  # but you'll need to customize to take args
   ```
   Or better: I'll create a simple CLI wrapper for you to run with parameters.

4. Upload individualized PDF to Etsy's "Digital files" section for that order
5. Confirm order and send message "Your order is ready! Download from your purchases page."

**Alternative:** Set up webhook integration (see below) after you stabilize.

---

## Future Automation (Webhook Integration)

Once you're getting consistent sales (20+/week), we can automate fulfillment:

1. **Etsy API Setup** (requires Etsy developer account)
   - Apply for Etsy API access: https://developers.etsy.com/
   - Create app, get API key/secret
   - Enable "order listing" and "order details" permissions

2. **Configure Zo Service**
   - Save Etsy API credentials in [Settings > Advanced](/?t=settings&s=advanced) as `ETSY_API_KEY`, `ETSY_API_SECRET`
   - Deploy automation_server.py as a persistent service on Zo
   - Set up webhook endpoint in Etsy developer portal to point to your Zo service

3. **Auto-Generate & Deliver**
   - Webhook triggers on purchase
   - Server extracts customization data (child name, numbers, etc.)
   - Generate personalized PDF automatically
   - Upload to Etsy's CDN and attach to order
   - Send delivery confirmation message

**Timeline for automation:** 1-2 weeks after consistent sales pattern emerges.

---

## Pricing & Revenue Projections

### Assumptions
- **Conversion rate:** 2% of views to sales (typical Etsy digital products)
- **Initial traffic:** 50-100 views/day with 5 listings = ~1500-3000 views/month
- **Monthly sales:** 30-60 orders (conservative)
- **Average order value:** $13-18

### Revenue Projections

| Month | Listings | Est. Orders | Avg. Price | Revenue | Etsy Fees (10%) | Net |
|-------|----------|-------------|------------|---------|-----------------|-----|
| 1 | 5 | 25 | $13 | $325 | $33 | $292 |
| 2 | 7 | 45 | $14 | $630 | $63 | $567 |
| 3 | 10 | 70 | $15 | $1,050 | $105 | $945 |
| 6 | 12 | 120 | $16 | $1,920 | $192 | $1,728 |

**Year 1 total (conservative):** $8,000-12,000 net profit after fees
**Year 2 (automated, 20 listings):** $20,000-30,000

*Note: This does not include tax implications. Consult an accountant.*

### Cost Structure
- **Initial setup:** $0 (already have Zo server, all tools free)
- **Monthly costs:** $0-5 (Zo free tier covers everything)
- **Per-listing fee:** $0.20 (paid to Etsy when listing)
- **Transaction fee:** 6.5% + $0.20 payment processing (from Etsy)
- **Total platform take:** ~10-11% including payment processing

---

## Why This Works

1. **Proven demand:** Bestsellers with 2k-12k reviews on Etsy prove market exists
2. **Low competition:** Niching to "preschool number worksheets" (258 listings) vs generic "preschool printables" (230k+)
3. **Perfect for automation:**
   - PDFs are parameterized: child's name + numbers → unique product
   - Spreadsheets are templated: family name auto-placed
   - Zero marginal cost per additional sale
4. **Etsy handles payment & delivery:** No Stripe, no hosting fees
5. **Scalable:** One generator → infinite variations (different numbers, custom family names)
6. **Fast time to market:** 2 weeks from Etsy account to first listing

---

## Next Immediate Actions

1. **Today:** Review generated sample files in `output_worksheets/` and `output_budgets/`
2. **Today:** Create Etsy seller account (if you're ready)
3. **Today:** Design product images (screenshots of sample PDFs)
4. **Tomorrow:** Create first 3 listings (copy from LISTING_TEMPLATES.md)
5. **Within 48h:** Launch first 5 listings
6. **Week 1:** Monitor impressions, adjust titles/tags if < 100 impressions/day
7. **Week 2-3:** Make first sales (hopefully!)
8. **After 10 sales:** Review pricing, add 2 more listings, iterate

---

## Files in This Project

```
Digital_Product_Automation/
├── README.md                    # This file
├── LISTING_TEMPLATES.md         # Copy-paste Etsy content
├── AGENTS.md                    # Project memory (update as we go)
├── preschool_number_generator.py    # PDF generator for number worksheets
├── homeschool_budget_generator.py   # Excel generator for budgets
├── automation_server.py         # Unified order processor
├── output_worksheets/           # Generated PDF samples (safe to delete/regen)
└── output_budgets/              # Generated Excel samples
```

---

## Support & Questions

- **Technical issues:** Check Python dependencies, file permissions
- **Etsy questions:** Refer to Etsy Seller Help Center
- **Customization requests:** Can add new worksheet types (alphabet, shapes, colors) or new budget templates (sports team, small business) in 1-2 hours each

---

**Let's make your first sale!** 🎯

Ready to proceed? I'll be available when you need:
- Etsy account setup guidance
- Review of listing drafts before publishing
- New product ideas based on sales data
- Webhook automation after you hit 20 sales/week

**Your next move:** Create Etsy seller account, then let me know your shop name so I can customize branding suggestions.