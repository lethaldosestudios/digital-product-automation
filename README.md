# Digital Product Automation Project - by: Porter LaForce

**Status:** Phase 2 Complete - MVP Generators Built | Ready for Phase 3 (Payhip Store Setup)

**Project Goal:** Launch automated digital product store on Payhip selling preschool worksheets and homeschool budget spreadsheets with zero manual fulfillment.

**Primary Platform:** [Payhip](https://payhip.com) | **Backup Platform:** [Gumroad](https://gumroad.com)

**Timeline:** First listing ready immediately (this package). Payhip account setup → live listings → first sale within 2-3 weeks.

---

## ✅ TO-DO List

- [ ] **Decide on a shop name (branding)** ← New Task
- [ ] Review generated sample files in `output_worksheets/` and `output_budgets/`
- [ ] Create Payhip seller account
- [ ] Design product images (screenshots of sample PDFs)
- [ ] Create first 3 listings (copy from `LISTING_TEMPLATES.md`)
- [ ] Launch first 5 listings on Payhip
- [ ] Monitor traffic — adjust titles/tags if < 100 views/day after Week 1
- [ ] Make first sales (target: Week 2-3)
- [ ] After 10 sales: Review pricing, add 2 more listings, iterate
- [ ] After 20 sales/week: Set up Payhip webhook automation
- [ ] Evaluate upgrading to Payhip Pro ($99/mo) when revenue exceeds ~$500/month

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
- `webhook_handler()` - skeleton for Payhip/Gumroad integration (future)

**Quick Test:** `python3 automation_server.py` generates both product types.

### 4. Payhip Listing Templates (`LISTING_TEMPLATES.md`)

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

## Phase 3: Payhip Store Setup (Requires You)

### Step 1: Create Payhip Account

1. Go to [payhip.com](https://payhip.com) and click "Get Started Free"
2. Create your free account (no credit card required)
3. Set up your store name — see shop name suggestions below
4. Add payment method via Stripe or PayPal (Payhip connects these for payouts)
5. Set up your store policies (for digital products: "No refunds" after download)
6. No per-listing fees — listings are free on Payhip

**Shop Name Ideas (Payhip-optimized):**
- LearnWithLaForce
- PrintableNestCo
- HomeschoolShopCo
- EarlyLearningVault
- LearningBundleHQ
- ThePrintableDesk
- NestLearningCo

> 🔲 **TO-DO: Decide on a shop name (branding)** — pick one from above or create your own!

**Backup Option — Gumroad:**
If you want a second storefront or to test both platforms:
1. Go to [gumroad.com](https://gumroad.com) and sign up free
2. Create the same listings with the same content
3. Gumroad charges 10% per sale (higher than Payhip's 5%) but has built-in creator discovery

### Step 2: Create Listings on Payhip

1. Click "Add Product" → select "Digital Product"
2. Upload your PDF or Excel file as the product file
3. Copy-paste title, description, and tags from `LISTING_TEMPLATES.md`
4. Set price (start with recommended prices, adjust after 10 sales based on demand)
5. Upload product preview image (screenshot of sample pages)
6. Toggle "Instant Download" — Payhip delivers files automatically on purchase
7. Publish!

### Step 3: Initial Listings (Launch with 5-7 Products)

- **Preschool line (3 listings):** Numbers 1-10, 11-20, Complete 1-20
- **Budget line (2 listings):** Monthly Budget, Complete Finance Bundle

You can add the curriculum tracker later as a standalone or as part of bundle.

### Step 4: Handle Orders Manually (Initially)

For first 20-50 sales:
1. Check Payhip dashboard for new orders
2. Note customer name (and child name if provided in "notes to buyer" field)
3. Run appropriate generator command locally:
   ```bash
   python3 automation_server.py
   ```
4. Upload individualized PDF to the order in Payhip's dashboard
5. Payhip sends automatic delivery email — optionally follow up with a personal message

**Alternative:** Set up Payhip webhook integration (see below) after you stabilize.

---

## Future Automation (Webhook Integration)

Once you're getting consistent sales (20+/week), we can automate fulfillment:

1. **Payhip Webhook Setup** (primary)
   - Go to Payhip dashboard → Settings → Webhooks
   - Add your server endpoint URL
   - Payhip sends a POST request for every purchase event
   - Docs: https://payhip.com/api

2. **Gumroad Webhook Setup** (backup/secondary store)
   - Go to Gumroad → Settings → Advanced → Ping URL
   - Add your server endpoint URL
   - Docs: https://app.gumroad.com/api

3. **Configure Server**
   - Save Payhip/Gumroad webhook secrets in environment variables as `PAYHIP_WEBHOOK_SECRET`, `GUMROAD_WEBHOOK_SECRET`
   - Deploy `automation_server.py` as a persistent service
   - The existing `webhook_handler()` skeleton is ready for this integration

4. **Auto-Generate & Deliver**
   - Webhook triggers on purchase
   - Server extracts customization data (child name, numbers, etc.)
   - Generate personalized PDF automatically
   - Payhip delivers file to buyer automatically via its CDN
   - Send custom delivery confirmation message

**Timeline for automation:** 1-2 weeks after consistent sales pattern emerges.

---

## Pricing & Revenue Projections

### Assumptions
- **Conversion rate:** 2% of views to sales (typical digital products)
- **Initial traffic:** 50-100 views/day with 5 listings = ~1,500-3,000 views/month
- **Monthly sales:** 30-60 orders (conservative)
- **Average order value:** $13-18

### Revenue Projections

| Month | Listings | Est. Orders | Avg. Price | Revenue | Payhip Fees (5%) | Net |
|-------|----------|-------------|------------|---------|------------------|-----|
| 1 | 5 | 25 | $13 | $325 | $16 | $309 |
| 2 | 7 | 45 | $14 | $630 | $32 | $598 |
| 3 | 10 | 70 | $15 | $1,050 | $53 | $997 |
| 6 | 12 | 120 | $16 | $1,920 | $96 | $1,824 |

> **Payhip vs Gumroad fee comparison:** Payhip charges 5% per sale; Gumroad charges 10%. On $1,920 revenue, that's $96 vs $192 — Payhip saves ~$96/month at Month 6.

**Year 1 total (conservative):** $9,000-13,500 net profit after fees
**Year 2 (automated, 20 listings):** $22,000-32,000

*Note: This does not include tax implications. Consult an accountant.*

### Cost Structure
- **Initial setup:** $0 (Payhip free tier, all tools free)
- **Monthly costs:** $0 (Payhip free plan)
- **Per-listing fee:** $0 (Payhip does not charge listing fees)
- **Transaction fee:** 5% per sale (Payhip free plan)
- **Upgrade option:** Payhip Plus ($29/mo, 2% fee) or Pro ($99/mo, 0% fee)
- **Gumroad backup:** 10% per sale, $0/month

---

## Why This Works

1. **Proven demand:** Bestsellers with 2k-12k reviews in this niche prove the market exists
2. **Low competition:** Niching to "preschool number worksheets" and "homeschool budget templates" — specific, searchable, underserved
3. **Perfect for automation:**
   - PDFs are parameterized: child's name + numbers → unique product
   - Spreadsheets are templated: family name auto-placed
   - Zero marginal cost per additional sale
4. **Payhip handles payment & delivery:** No Stripe setup needed, no hosting fees
5. **Scalable:** One generator → infinite variations (different numbers, custom family names)
6. **Fast time to market:** Create Payhip account → first listing live in under an hour
7. **Lower fees than alternatives:** 5% on Payhip vs 10-11% on other platforms — keeps more revenue per sale

---

## Next Immediate Actions

1. **Today:** 🔲 Decide on a shop name (branding) — see suggestions in Phase 3 above
2. **Today:** Review generated sample files in `output_worksheets/` and `output_budgets/`
3. **Today:** Create Payhip account at [payhip.com](https://payhip.com)
4. **Today:** Design product images (screenshots of sample PDFs)
5. **Tomorrow:** Create first 3 listings (copy from `LISTING_TEMPLATES.md`)
6. **Within 48h:** Launch first 5 listings on Payhip
7. **Optional:** Mirror listings on Gumroad as backup storefront
8. **Week 1:** Monitor views, adjust titles/descriptions if < 100 views/day
9. **Week 2-3:** Make first sales!
10. **After 10 sales:** Review pricing, add 2 more listings, iterate

---

## Files in This Project

```
Digital_Product_Automation/
├── README.md                        # This file
├── LISTING_TEMPLATES.md             # Copy-paste Payhip/Gumroad listing content
├── PRODUCT_CATALOG.md               # Product details and mockup guidance
├── preschool_number_generator.py    # PDF generator for number worksheets
├── homeschool_budget_generator.py   # Excel generator for budgets
├── automation_server.py             # Unified order processor
├── output_worksheets/               # Generated PDF samples (safe to delete/regen)
└── output_budgets/                  # Generated Excel samples
```

---

## Support & Questions

- **Technical issues:** Check Python dependencies, file permissions
- **Payhip questions:** Refer to [Payhip Help Center](https://help.payhip.com)
- **Gumroad questions (backup):** Refer to [Gumroad Help Center](https://help.gumroad.com)
- **Customization requests:** Can add new worksheet types (alphabet, shapes, colors) or new budget templates (sports team, small business) in 1-2 hours each

---

**Let's make your first sale!** 🎯

Ready to proceed? Available when you need:
- Payhip store setup guidance
- Review of listing drafts before publishing
- New product ideas based on sales data
- Webhook automation after you hit 20 sales/week

**Your next move:** 🔲 Decide on a shop name, then create your Payhip account!
