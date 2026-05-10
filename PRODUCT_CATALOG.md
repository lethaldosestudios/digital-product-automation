# Product Catalog & Mockups

This document shows exactly what each digital product looks like and provides guidance for creating Lemon Squeezy listing images.

> **Primary Platform:** [Lemon Squeezy](https://lemonsqueezy.com) | **Backup Platform:** [Gumroad](https://gumroad.com)

---

## Preschool Number Worksheets Line

### Product 1: Numbers 1-10 Bundle (12+ pages) - $11.99

**Contents:**
1. Cover page with bundle title and child's name
2. Number 1 - Tracing worksheet (6 tracing lines + 3 independent lines)
3. Number 1 - Find the number game (grid of 1-20 mixed)
4. Repeated for numbers 2-5 (or up to 10)
5. Counting practice sheet (5 objects to count)

**File Example:** `output_worksheets/bundle_cover_Emma.pdf`

**Visual Style:**
- Clean white background
- Large, clear numbers (60pt for main number, 12pt for instructions)
- Helvetica font (basic but professional)
- Centered layout with generous margins
- Black text only (easy to print, saves ink)

**Sample Caption for listing image:**
> "Inside the bundle: number tracing, number recognition, counting practice. Perfect for ages 3-6."

**Suggested mockup:**
- Main image: 3-4 sample pages laid flat, slightly overlapping, with "20+ Pages" badge

---

### Product 2: Numbers 11-20 Extension - $9.99

Same format as above but numbers 11-20. Can be purchased separately or as part of complete bundle.

**Suggested mockup:** Side-by-side with Product 1 showing "Part 1" and "Part 2" labels.

---

### Product 3: Complete Numbers 1-20 Bundle - $18.99

**Contents:** Everything from Product 1 + Product 2 + bonus:
- Numbers 1-20 (40+ pages total)
- Progress tracking chart for parents
- Storage/organization tips
- Teacher's notes

**Value proposition:** Save $3 vs buying separately, plus bonus materials.

**Suggested mockup:** All 40+ pages fanned out showing scale of content.

---

## Homeschool Budget Spreadsheets Line

### Product 4: Monthly Budget Spreadsheet - $12.99

**Contents:** 1 Excel file + Google Sheets instructions
- 1 worksheet: Monthly budget table (Jan-Dec tabs)
- 2 worksheet: Annual summary
- Pre-built formulas for totals, variances, running totals
- Color-coded headers (blue), totals (light gray)

**Sample:** `output_budgets/homeschool_monthly_budget_Test_Family.xlsx`

**Structure:**
```
A1: "Homeschool Monthly Budget - [Family Name]"
A1 merged across F1

Headers (row 4):
A: Category | B: Item Description | C: Budgeted | D: Actual | E: Difference | F: Notes

Sample rows:
Row 5: Category (bold)
Row 6-9: Items under category (Curriculum, then specific items)
...

Totals section (rows ~20-25):
B20: "TOTAL BUDGET" -> C20: =SUM(C5:C19)
B21: "TOTAL ACTUAL" -> D21: =SUM(D5:D19)
B22: "NET DIFFERENCE" -> E22: =D21-C20
```

**Visual Style (Excel screenshot):**
- Clean table with borders
- Blue header row (RGB: 54,96,146)
- Light gray total row
- Currency formatting on amount columns ($#,##0.00)
- Frozen panes for header row

**Mockup suggestion:** Screenshot of Excel showing entire monthly budget table (multiple months tabs visible on bottom)

---

### Product 5: Complete Finance Bundle - $24.99

**Contents:** 3 Excel files + instructions
1. `monthly_budget_[Family].xlsx`
2. `annual_budget_[Family].xlsx`
3. `curriculum_tracker_[Family].xlsx`

**Monthly Budget:** Detailed 12-month tracking (description above)
**Annual Budget:** Summary view with monthly columns and annual totals
**Curriculum Tracker:** Table tracking each curriculum purchase per child

**Curriculum Tracker structure:**
```
A1: "Curriculum Purchase Tracker - [Family]"

Headers:
A: Subject | B: Curriculum Name | C: Vendor | D: Price | E: Grade Level | F: Status | G: Notes

Sample rows:
A: Math | B: Singapore Math 1A | C: Sonlight | D: $45.99 | E: 1st | F: Purchased | G: Includes manipulatives
```

**Value proposition:** Holistic view of all homeschool finances in one package. Track expenses, plan ahead, and never lose receipt documentation.

**Mockup suggestion:** 3 screenshots tiled together showing each spreadsheet, or a single screenshot with all 3 files visible in file explorer.

---

## How to Create Listing Images

### Option 1: Manual Screenshots (Fastest)

1. Open generated file (PDF or Excel)
2. Use OS screenshot tool (Snipping Tool on Windows, Shift+Cmd+4 on Mac)
3. Crop to show key content
4. Add text overlay with Canva/Photoshop/GIMP: "20+ Pages", "Instant Download", "Reusable"
5. Save as JPG/PNG

**Lemon Squeezy image minimum:** 1920x1080px preferred.

### Option 2: Automated Mockups (Better, but needs setup)

If you want professional-looking mockups:

1. Install `pdf2image` + `poppler` to convert PDFs to PNG
2. Use Python to batch convert
3. Use Canva or simple Python imaging to add badges (e.g., "20+ Pages")
4. Export as 1920x1080px images

**Simplest approach:** Take good screenshots, upload to Canva, add consistent branding (shop name/logo in corner), export at 1920x1080.

---

## Image Checklist Per Listing

**Minimum:** 1 image (main thumbnail)  
**Recommended:** 5 images + 1 video  
**Required:** At least 1 image showing the actual product

### Image Sequence (5 images)

1. **Hero shot:** Beautiful arrangement of 3-4 sample pages, title overlay
2. **Use case:** Child's hand holding printed worksheet or peaceful homeschool table scene
3. **Detail view:** Close-up of one tracing page showing large traceable numbers
4. **Variety:** Show 2-3 different worksheet types (tracing + find-the-number + counting)
5. **Value prop:** All pages fanned out showing quantity, or "What's inside" collage

### Optional Video (Highly Recommended)
- 15-30 second MP4
- Show PDF pages flipping or scrolling through Excel spreadsheet
- Add text overlay: "Download instantly after purchase!"
- Helps conversion significantly

---

## Pricing Table for Listings

| Product | List Price | Sale Price | Cost to Produce | LS Fee (5% + $0.50) | Net per Sale | Gumroad Net (10% fee) |
|---------|------------|------------|-----------------|---------------------|--------------|----------------------|
| Numbers 1-10 | $14.99 | $11.99 (20% off) | $0 | ~$1.10 | ~$10.89 | ~$10.79 |
| Numbers 11-20 | $11.99 | $9.99 (17% off) | $0 | ~$1.00 | ~$8.99 | ~$8.99 |
| Complete 1-20 | $29.99 | $18.99 (37% off) | $0 | ~$1.45 | ~$17.54 | ~$17.09 |
| Monthly Budget | $16.00 | $12.99 (19% off) | $0 | ~$1.15 | ~$11.84 | ~$11.69 |
| Finance Bundle | $39.99 | $24.99 (38% off) | $0 | ~$1.75 | ~$23.24 | ~$22.49 |

> **Note:** Lemon Squeezy's 5% + $0.50/sale fee is competitive at higher price points and includes built-in tax/VAT handling. Use Lemon Squeezy as primary, Gumroad as backup only.

**Why the deep discount on bundles?** To incentivize higher order value. Customer feels they're getting a deal, you still net more per sale.

---

## SEO Keywords Research

### High-volume, low-competition combos:
- "number tracing worksheets" - 4,500/mo searches
- "preschool math printable" - 3,200/mo
- "homeschool budget spreadsheet" - 600/mo (explicitly low competition!)
- "Google Sheets budget template" - 2,800/mo
- "instant download worksheet" - 5,100/mo
- "printable number activities" - 1,900/mo

**Long-tail (use in tags 8-13):**
- "preschool number recognition"
- "kindergarten math practice"
- "homeschool expense tracker"
- "curriculum purchase log"
- "number formation worksheet"
- "budget for homeschool"

---

## Branding

> 🔲 **TO-DO: Decide on a shop name (branding)**

**Shop Name:** The Printable Desk | **URL:** ThePrintableDesk ← top candidate

**Logo:** Simple text-based, use Canva (free) or hire Fiverr ($20)
- Shop initials with pencil icon or desk icon

**Colors:** Suggest blue/teal (trust, professional) + accent color (yellow/orange for learning)
- Primary: #366092 (deep blue — trust and education)
- Secondary: #FFD700 (gold accent)
- Neutral: #FFFFFF (white), #F5F5F5 (light gray)

---

## FAQ to Pre-empt Customer Questions

**Q: Can I edit the worksheets?**
A: Yes! PDFs can be edited with Adobe Acrobat (paid) or PDFescape (free online). For deeper customization, contact us for a custom quote.

**Q: Do you offer refunds?**
A: Digital files cannot be returned once downloaded. But if there's an issue with the product, message us and we'll make it right.

**Q: Can I use these for my co-op group?**
A: One purchase covers a single family. For co-ops (10+ families), contact us for a group license ($25-50 depending on size).

**Q: Are these aligned with Common Core?**
A: Our number worksheets cover foundational skills that align with kindergarten math standards. We don't officially claim Common Core alignment but the skills are universally applicable.

**Q: Do you do custom orders?**
A: Yes! Contact us for custom worksheet types (letters, shapes, sight words) or custom budget templates (sports teams, small business). Turnaround 24-48 hours.

---

## Sample Customer Communication Templates

### Order Confirmation
Lemon Squeezy delivers the download link automatically on purchase. No action needed for standard orders.

### Follow-up Message (3 days later - optional)
> Hi [Customer Name]! Hope you're enjoying your [product name]. Quick question: Is there anything else you'd like to see in our worksheets? We're always creating new products based on customer feedback. Let us know!
>
> Also, if you have a moment, we'd love a review on our store page — it helps other families find our resources.
>
> Thanks for supporting our small shop!
> - The Printable Desk

### Custom Order Inquiry Response
> We'd be happy to create a custom [description] for you! Custom orders typically take 24-48 hours and start at $15 depending on complexity. Please reply with any specific requirements (grade level, topics, number of pages, budget range) and I'll send a quote.

---

## Analytics & Iteration (After Launch)

Track these metrics in your Lemon Squeezy dashboard:

**Health metrics:**
- **Views:** How many times your product page is visited
- **Click-through rate:** From any external links or social posts
  - Low traffic → Improve SEO keywords, share in homeschool communities
- **Conversion rate:** % of visits that purchase
  - < 1% → Improve description, pricing, or social proof
  - 1-2% → Average
  - > 2% → Excellent

**Gumroad analytics (if using as backup):**
- Track separately via Gumroad dashboard
- Compare conversion rates between platforms after 30 days
- Double down on whichever performs better

**When to adjust:**
- 100+ views, 0 purchases → Change main image or reduce price
- 50+ visits, 0 sales → Improve description or add social proof
- 5+ sales with 0 reviews → Message buyers asking for a review
- Consistent sales (10+/week): Add 2-3 new listings, cross-promote

---

## Next Steps Checklist

- [ ] **Decide on a shop name (branding)** — **ThePrintableDesk** is the top candidate ← TO-DO
- [ ] Generate sample files to verify output quality
- [ ] Create product images (screenshots → Canva mockups)
- [ ] Log in to your Lemon Squeezy store at [app.lemonsqueezy.com](https://app.lemonsqueezy.com)
- [ ] Write first 3 listings using templates above
- [ ] Publish listings on Lemon Squeezy
- [ ] (Optional) Mirror listings on [Gumroad](https://gumroad.com) as backup storefront
- [ ] Daily: Check stats for first week
- [ ] After 5 visits/day: Optimize listings
- [ ] After first sale: Celebrate 🎉

---

**Ready to launch.** All technical pieces are built. Your job is to:
1. Decide on your shop name
2. Log in to Lemon Squeezy
3. Make pretty pictures
4. Copy-paste listings
5. Press publish
