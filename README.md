# Digital Product Automation Project - Porter LaForce

## 🔲 TO-DO
- 🔲 Decide on a shop name (branding) — **ThePrintableDesk** is the top candidate
- 🔲 Create logo and favicon (see Branding section below)
- 🔲 Choose theme color: **Lemon** vs **Blackberry** (decision pending)
- 🔲 Generate free sampler lead magnet — Numbers 1-3 preview PDF (free listing on Lemon Squeezy)
- 🔲 Create product cover images (screenshots → Canva at 1920x1080px)

---

**Status:** Phase 2 Complete - MVP Generators Built | Ready for Phase 3 (Lemon Squeezy Store Setup)

**Project Goal:** Launch automated digital product store on Lemon Squeezy (primary) selling preschool worksheets and homeschool budget spreadsheets with zero manual fulfillment. Gumroad as backup storefront.

**Store Name:** The Printable Desk | **Store URL:** ThePrintableDesk

**Timeline:** First listing ready immediately (this package). Lemon Squeezy store setup → live listings → first sale within 2-3 weeks.

---

## Branding

### Shop Name
**The Printable Desk** (display) | **ThePrintableDesk** (URL slug)

### Theme Color Options (Decision Pending)

| Option | Primary | Accent | Feel |
|---|---|---|---|
| **Lemon** | `#F5C518` (warm yellow) | `#FFFFFF` + `#2D2D2D` | Bright, playful, energetic |
| **Blackberry** | `#3B1F5E` (deep purple) | `#E8D5F5` + `#FFFFFF` | Premium, calm, trustworthy |

### Logo Concept
- Icon: pencil + desk or open book on a desk
- Font: rounded, friendly (e.g., Nunito, Poppins)
- Style: simple, scalable (works at 512px logo AND 32px favicon)

### Favicon
- Use the logo icon only (no text) — typically initials "TPD" or just the pencil/desk icon
- Export at 32x32px and 192x192px

### Brand Colors (Confirmed Base)
- Neutral: `#FFFFFF` (white), `#F5F5F5` (light gray)
- Text: `#2D2D2D` (near-black for readability)

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
- `webhook_handler()` - skeleton for Lemon Squeezy/Gumroad integration (future)

**Quick Test:** `python3 automation_server.py` generates both product types.

### 4. Lemon Squeezy Listing Templates (`LISTING_TEMPLATES.md`)

Copy-paste ready content for 5 listings:
- Numbers 1-10 bundle ($11.99)
- Numbers 11-20 extension ($9.99)
- Complete numbers 1-20 bundle ($18.99)
- Monthly homeschool budget ($12.99)
- Complete finance bundle ($24.99)

Each includes: optimized title, description, tags, pricing strategy, image requirements.

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
    "year": 2026,
    "order_id": "BUD-001"
}
result = server.generate_budget_order(budget_order)
```

---

## Phase 3: Lemon Squeezy Store Setup

> **Store already created:** The Printable Desk (ThePrintableDesk) ✅  
> **Perplexity MCP Connector:** Lemon Squeezy API key connected ✅

### Step 1: Configure Your Store Profile

1. Go to [app.lemonsqueezy.com](https://app.lemonsqueezy.com) → Settings → Store
2. Set store name: **The Printable Desk**
3. Set store URL slug: **ThePrintableDesk**
4. Add store logo and banner (use product screenshot collage)
5. Set payout method: bank account or PayPal (Settings → Payouts)
6. Payouts are processed **twice a month** automatically

**Shop Name:** The Printable Desk  
**Store URL:** ThePrintableDesk

### Step 2: Create Products (Listings)

1. Go to **Products → New Product**
2. Set product type: **Digital download (single file or bundle)**
3. Upload the PDF/Excel file directly — Lemon Squeezy handles secure delivery
4. Copy-paste title, description, and tags from `LISTING_TEMPLATES.md`
5. Set price (recommended starting prices in templates)
6. Enable **"Pay what you want"** option optionally for lead magnets
7. Publish — your product gets a unique shareable checkout URL instantly

### Step 3: Initial Listings (Launch with 5-7 Products)

- **Preschool line (3 listings):** Numbers 1-10, Numbers 11-20, Complete 1-20
- **Budget line (2 listings):** Monthly Budget, Complete Finance Bundle
- **Lead magnet (1 free listing):** Numbers 1-3 Sampler — free download to drive discovery

Add the curriculum tracker later as a standalone or bundle upgrade.

### Step 4: Handle Orders Initially (Manual → Auto)

For first 20-50 sales:
1. Check Lemon Squeezy dashboard → **Orders** for new purchases
2. Note customer name (and child name if provided in order notes)
3. Since Lemon Squeezy handles static file delivery automatically, manual steps are only needed for **personalized** (custom name) orders
4. For non-personalized products, Lemon Squeezy delivers the file instantly — no action needed

**Next step:** Wire `webhook_handler()` for full automation (see below).

---

## Automation (Webhook Integration)

Once you're getting consistent sales (20+/week), automate personalized fulfillment:

### 1. Lemon Squeezy Webhook Setup
- Go to **Settings → Webhooks** in your Lemon Squeezy dashboard
- Add a new webhook endpoint pointing to your automation server URL
- Subscribe to the `order_created` event
- Copy the **signing secret** for payload verification

### 2. Configure Automation Server
- Save Lemon Squeezy API credentials as environment variables:
  - `LEMONSQUEEZY_API_KEY` — from Settings → API
  - `LEMONSQUEEZY_WEBHOOK_SECRET` — from the webhook you created
- Deploy `automation_server.py` as a persistent service
- Set the webhook endpoint URL in Lemon Squeezy to point to your deployed server

### 3. Perplexity MCP Connector ✅ (Active)
- Lemon Squeezy is connected to Perplexity via API key connector
- Use Perplexity to: query orders, update products, manage coupons, check revenue
- MCP also available via [Pipedream](https://mcp.pipedream.com/app/lemon_squeezy) for additional automation flows

### 4. Auto-Generate & Deliver
- `order_created` webhook triggers on purchase
- Server extracts customization data (child name, numbers range, family name, etc.)
- Generate personalized PDF/Excel automatically
- Upload to Lemon Squeezy order fulfillment via API
- Lemon Squeezy notifies customer with download link

### 5. Gumroad as Backup Channel
- Mirror top-performing listings on [Gumroad](https://gumroad.com) for additional discovery
- Gumroad charges 10% transaction fee on free plan (vs Lemon Squeezy's 5% + $0.50)
- Use `webhook_handler()` with a `platform` parameter to support both Lemon Squeezy and Gumroad events

**Timeline for automation:** 1-2 weeks after consistent sales pattern emerges.

---

## Pricing & Revenue Projections

### Platform Fee Structure

| Platform | Monthly Fee | Transaction Fee | Notes |
|---|---|---|---|
| **Lemon Squeezy (Primary)** | $0 | 5% + $0.50/sale | Merchant of record — handles all VAT/tax |
| **Gumroad (Backup)** | $0 | 10% | Simpler, less automation-friendly |

### Assumptions
- **Conversion rate:** 2% of views to sales (typical digital products)
- **Initial traffic:** 50-100 views/day with 5 listings = ~1,500-3,000 views/month
- **Monthly sales:** 30-60 orders (conservative)
- **Average order value:** $13-18

### Revenue Projections

| Month | Listings | Est. Orders | Avg. Price | Revenue | LS Fees (~8%) | Net |
|-------|----------|-------------|------------|---------|----------------|-----|
| 1 | 5 | 25 | $13 | $325 | $26 | $299 |
| 2 | 7 | 45 | $14 | $630 | $50 | $580 |
| 3 | 10 | 70 | $15 | $1,050 | $84 | $966 |
| 6 | 12 | 120 | $16 | $1,920 | $154 | $1,766 |

**Year 1 total (conservative):** $8,000-12,000 net profit after fees  
**Year 2 (automated, 20 listings):** $20,000-30,000

*Note: Lemon Squeezy acts as merchant of record and handles all sales tax/VAT automatically — no accountant needed for tax collection. Consult an accountant for income tax implications.*

### Cost Structure
- **Initial setup:** $0 (store is free, all tools free)
- **Monthly costs:** $0 — Lemon Squeezy has no monthly fee
- **Per-sale fee:** 5% + $0.50 per transaction
- **Total platform take:** ~8% effective rate at average $13 order value

---

## Why This Works

1. **Proven demand:** Bestsellers with 2k-12k reviews in this niche prove the market exists
2. **Low competition:** Niching to "preschool number worksheets" vs generic "preschool printables"
3. **Perfect for automation:**
   - PDFs are parameterized: child's name + numbers → unique product
   - Spreadsheets are templated: family name auto-placed
   - Zero marginal cost per additional sale
4. **Lemon Squeezy handles payment, delivery & taxes:** No Stripe setup, no VAT headaches, no hosting fees
5. **Full API + MCP:** Lemon Squeezy's REST API + Perplexity connector enables fully autonomous store management
6. **Scalable:** One generator → infinite variations (different numbers, custom family names)
7. **Fast time to market:** Store already created — first listing can go live today

---

## Next Immediate Actions

1. **Today:** Finalize logo, favicon, and theme color (Lemon vs Blackberry)
2. **Today:** Review generated sample files in `output_worksheets/` and `output_budgets/`
3. **Today:** Design product cover images (screenshots → Canva at 1920x1080px)
4. **Tomorrow:** Upload first 3 listings using `LISTING_TEMPLATES.md`
5. **Within 48h:** Launch first 5 listings + free lead magnet (Numbers 1-3 sampler)
6. **Week 1:** Monitor orders and views; adjust titles/tags if < 100 impressions/day
7. **Week 2-3:** Make first sales
8. **After 10 sales:** Review pricing, add 2 more listings, iterate
9. **After 20 sales/week:** Wire `webhook_handler()` to Lemon Squeezy webhook for full automation

---

## Files in This Project

```
Digital_Product_Automation/
├── README.md                        # This file
├── LISTING_TEMPLATES.md             # Copy-paste Lemon Squeezy listing content
├── PRODUCT_CATALOG.md               # Product visuals and mockup guidance
├── AGENTS.md                        # Project memory (update as we go)
├── preschool_number_generator.py    # PDF generator for number worksheets
├── homeschool_budget_generator.py   # Excel generator for budgets
├── automation_server.py             # Unified order processor (LS + Gumroad webhook skeleton)
├── samples_for_store/               # Generated sample files for store listings
├── output_worksheets/               # Generated PDF samples (safe to delete/regen)
└── output_budgets/                  # Generated Excel samples
```

---

## Support & Questions

- **Technical issues:** Check Python dependencies, file permissions
- **Lemon Squeezy questions:** Refer to [Lemon Squeezy Help Center](https://docs.lemonsqueezy.com)
- **API/automation help:** See [Lemon Squeezy API docs](https://docs.lemonsqueezy.com/api)
- **Customization requests:** Can add new worksheet types (alphabet, shapes, colors) or new budget templates (sports team, small business) in 1-2 hours each

---

**Let's make your first sale!** 🍋

Ready to proceed? Available when you need:
- Lemon Squeezy listing setup guidance
- Review of product pages before publishing
- New product ideas based on sales data
- Webhook automation after you hit 20 sales/week

**Your next move:** Finalize logo + theme color, then upload first product to [The Printable Desk on Lemon Squeezy](https://app.lemonsqueezy.com)!
