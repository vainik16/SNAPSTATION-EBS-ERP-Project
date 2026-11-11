# SNAPSTATION EVENT TECHNOLOGIES Ã¢â‚¬â€ ERP IMPLEMENTATION GUIDE
**Course:** Enterprise Business Systems (UE24CS343AB8)
**Academic Period:** August Ã¢â‚¬â€œ December 2026
**Institution:** PES University, Bengaluru
**Submission Deadline:** 16 November 2026
**Presentation / Viva Period:** 16 Ã¢â‚¬â€œ 19 November 2026

---

## 1. Project Team Details
1. **Vainik** Ã¢â‚¬â€œ `PES1UG24CS513` Ã¢â‚¬â€œ Lead Systems Architect & Sales Lead
2. **Skanda** Ã¢â‚¬â€œ `PES1UG24CS457` Ã¢â‚¬â€œ Procurement & Supply Chain Lead
3. **Sujal** Ã¢â‚¬â€œ `PES1UG24CS476` Ã¢â‚¬â€œ Warehouse & Operations Manager
4. **Shreyank** Ã¢â‚¬â€œ `PES1UG24CS443` Ã¢â‚¬â€œ Finance & Accounts Analyst

---

## 2. Enterprise Overview (Fictional Academic Business)
- **Company Name:** SNAPSTATION EVENT TECHNOLOGIES
- **Tagline:** Photography. Experiences. Memories.
- **Corporate Headquarters:** Plot 14, Electronics City Phase 1, Hosur Road, Bengaluru, Karnataka, India 560100
- **Operational Currency:** INR (Indian Rupee - Ã¢â€šÂ¹)
- **Core Industry:** Photography Equipment, Event Technology, Photobooth Solutions & Turnkey Event Services
- **Client Base:** Wedding planners, academic institutions (e.g., PES Event Committee), corporate event managers, and commercial photography studios across Karnataka.

---

## 3. Technology Stack & Environment
- **Operating System:** Windows 11 Professional (Build 10.0.26200 x64)
- **Database Engine:** MySQL Community Server 8.0.33 running as Windows Service `MySQL80` on port 3306
- **Database Name:** `dolibarr_snapstation` (276 Relational Tables, utf8mb4_unicode_ci)
- **Application Server:** Portable PHP 8.2.35 (CLI & Built-in SAPI) deployed in `SNAPSTATION_EBS_PROJECT\php`
- **ERP Suite:** Dolibarr ERP & CRM Version 20.0.3 (Production lock active in `dolibarr_documents/install.lock`)
- **Web Host Address:** `http://localhost:8000`

---

## 4. Master Data Architecture
- **Customers (10):** Royal Moments Weddings (`CU2611-00001`), PixelCraft Photography (`CU2611-00002`), PES Event Committee (`CU2611-00003`), Celebration Hub Events (`CU2611-00004`), DreamDay Wedding Planners (`CU2611-00005`), UrbanFrame Studios (`CU2611-00006`), CorporateSpark Events (`CU2611-00007`), Lens & Light Photography (`CU2611-00008`), Grand Gala Events (`CU2611-00009`), Forever Frames Weddings (`CU2611-00010`).
- **Suppliers (5):** CameraWorld Distributors (`SU2611-00001`), ProLight Systems (`SU2611-00002`), PrintTech Supplies (`SU2611-00003`), EventGear India (`SU2611-00004`), LensPro Equipment Suppliers (`SU2611-00005`).
- **Product Catalog (30 SKUs):**
  - Physical Inventory: Cameras, lenses, photobooth hardware, 360 platforms, lighting units.
  - Consumables: Instant photo paper packs (100 sheets), dye-sub printer ribbons, lithium batteries.
  - Event Services: Daily equipment rentals, operated photobooth packages, platinum wedding tech packages.
- **Warehouses (2):**
  1. `WH-BLR-01`: Bengaluru Main Equipment Hub (10,000 sq.ft., Central inventory)
  2. `WH-MYS-01`: Mysuru Equipment Storage Centre (3,500 sq.ft., Regional depot)
- **System Users (5):** `admin` (Superuser), `vainik` (Sales), `skanda` (Procurement), `sujal` (Operations), `shreyank` (Finance). All users configured with full administrative and module privileges.
- **Bank Account:** HDFC Current Operating Account (`HDFC-01`, Ledger code 512000).

---

## 5. Enterprise Transactions & Audit Trail
- **Sales Orders:** 10 verified sales orders (`SO2611-0001` through `SO2611-0010`), totaling **Ã¢â€šÂ¹17,19,142.00**.
- **Customer Invoices:** 6 validated invoices (`IN2611-0001` through `IN2611-0006`), totaling **Ã¢â€šÂ¹11,07,194.00**.
- **Purchase Orders:** 10 verified purchase orders (`PO2611-0001` through `PO2611-0010`), totaling **Ã¢â€šÂ¹12,98,118.00**.
- **Supplier Invoices:** 7 validated invoices (`SI2611-0001` through `SI2611-0007`), totaling **Ã¢â€šÂ¹10,71,086.00**.
- **Bank Ledger:** 13 cleared transactions in `llx_bank` totaling **Ã¢â€šÂ¹21,78,280.00** in turnover.
