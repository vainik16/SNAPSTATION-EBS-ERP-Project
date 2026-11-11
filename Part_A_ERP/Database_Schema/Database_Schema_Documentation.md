# RELATIONAL DATABASE SCHEMA DOCUMENTATION
**System Name:** SNAPSTATION ERP Implementation
**Underlying EBS Package:** Dolibarr ERP & CRM (Version 20.0.3)
**RDBMS Engine:** MySQL Community Server 8.0.33 (x86_64)
**Database Name:** `dolibarr_snapstation`
**Host Configuration:** `localhost:3306` via TCP/IP Socket
**Character Set & Collation:** `utf8mb4` / `utf8mb4_unicode_ci`
**Schema Inspection Tool:** MySQL Workbench 8.0 / MySQL 8.0 Information Schema

---

## 1. Core Enterprise Tables & Architecture

The Dolibarr ERP underlying database structure follows a highly normalized relational model with standardized prefixes (`llx_`), auto-incrementing primary keys (`rowid`), entity multi-tenancy support (`entity`), audit timestamps (`datec`, `tms`), and explicit referential integrity constraints.

### 1.1 Master Data Entities

#### Table: `llx_societe` (Third Parties - Customers & Suppliers)
- **Description:** Central registry storing all external legal entities (both Customers and Vendors).
- **Primary Key:** `rowid` (int, auto_increment)
- **Key Attributes:**
  - `nom`: Legal company name (varchar 128)
  - `code_client`: Customer alphanumeric identifier (`CUyyMM-nnnnn`)
  - `code_fournisseur`: Supplier alphanumeric identifier (`SUyyMM-nnnnn`)
  - `client`: Customer status flag (1 = Customer, 2 = Prospect, 0 = Neither)
  - `fournisseur`: Vendor status flag (1 = Supplier, 0 = Non-supplier)
  - `address`, `zip`, `town`: Physical location details
  - `fk_pays`: Foreign key referencing `llx_c_country` (117 = India)
  - `status`: Active/inactive flag (1 = Active)
- **Foreign Keys:**
  - `fk_pays` -> `llx_c_country(rowid)`
  - `fk_user_creat` -> `llx_user(rowid)`

#### Table: `llx_user` (Employees & System Users)
- **Description:** Stores identity, academic SRNs, credentials, and access roles for team members.
- **Primary Key:** `rowid` (int, auto_increment)
- **Key Attributes:**
  - `login`: System login handle (`vainik`, `skanda`, `sujal`, `shreyank`)
  - `firstname`: Team member name
  - `lastname`: Team member SRN (`PES1UG24CS513`, `PES1UG24CS457`, `PES1UG24CS476`, `PES1UG24CS443`)
  - `job`: Enterprise job responsibility
  - `pass_crypted`: Blowfish / Argon2 secure password hash
  - `admin`: Superuser administrative privilege flag (1 = Admin)

#### Table: `llx_product` (Products and Services Catalog)
- **Description:** Central product master containing physical items, rental service packages, and consumables.
- **Primary Key:** `rowid` (int, auto_increment)
- **Key Attributes:**
  - `ref`: Unique SKU / Catalog code (`CAM-001`, `PB-001`, `360-001`, `SRV-001`)
  - `label`: Item description
  - `fk_product_type`: 0 = Physical Inventoried Goods, 1 = Service / Rental Package
  - `price`: Unit selling price in INR (Base HT)
  - `cost_price`: Unit purchase / standard cost price in INR
  - `tva_tx`: Applicable Goods and Services Tax rate (18.00%)
  - `tosell`: Sales availability flag (1 = Active on sale)
  - `tobuy`: Purchase availability flag (1 = Active on purchase)

#### Table: `llx_entrepot` (Warehouses & Distribution Hubs)
- **Description:** Physical warehouse locations storing equipment assets.
- **Primary Key:** `rowid` (int, auto_increment)
- **Key Attributes:**
  - `ref`: Warehouse identification name (`Bengaluru Main Equipment Hub`, `Mysuru Equipment Storage Centre`)
  - `description`: Operational facility description
  - `town`: City location (`Bengaluru`, `Mysuru`)
  - `statut`: Operating status flag (1 = Open)

#### Table: `llx_product_stock` (Inventory Balances)
- **Description:** Real-time stock quantity matrix cross-referencing products and warehouses.
- **Primary Key:** `rowid` (int, auto_increment)
- **Key Attributes:**
  - `fk_product`: Foreign key referencing `llx_product(rowid)`
  - `fk_entrepot`: Foreign key referencing `llx_entrepot(rowid)`
  - `reel`: Current physical quantity on hand
- **Unique Constraint:** `(fk_product, fk_entrepot)`

---

### 1.2 Order-to-Cash (O2C) Workflow Tables

#### Table: `llx_propal` & `llx_propaldet` (Quotations / Commercial Proposals)
- **Header Table (`llx_propal`):**
  - Primary Key: `rowid`
  - Ref: `PRyyMM-nnnn`
  - Foreign Keys: `fk_soc` -> `llx_societe(rowid)`, `fk_user_author` -> `llx_user(rowid)`
  - Totals: `total_ht`, `total_ttc`, `tva`
  - Status: `fk_statut` (0 = Draft, 1 = Validated, 2 = Signed/Billed)
- **Lines Table (`llx_propaldet`):**
  - Primary Key: `rowid`
  - Foreign Keys: `fk_propal` -> `llx_propal(rowid)`, `fk_product` -> `llx_product(rowid)`
  - Metrics: `qty`, `subprice`, `total_ht`, `total_ttc`, `tva_tx`

#### Table: `llx_commande` & `llx_commandedet` (Customer Sales Orders)
- **Header Table (`llx_commande`):**
  - Primary Key: `rowid`
  - Ref: `SOyyMM-nnnn`
  - Foreign Keys: `fk_soc` -> `llx_societe(rowid)`, `fk_user_author` -> `llx_user(rowid)`
  - Totals: `total_ht`, `total_ttc`, `tva`
  - Status: `fk_statut` (0 = Draft, 1 = Validated, 2 = In Delivery, 3 = Closed/Billed)
- **Lines Table (`llx_commandedet`):**
  - Primary Key: `rowid`
  - Foreign Keys: `fk_commande` -> `llx_commande(rowid)`, `fk_product` -> `llx_product(rowid)`
  - Metrics: `qty`, `subprice`, `total_ht`, `total_ttc`, `tva_tx`

#### Table: `llx_expedition` & `llx_expeditiondet` (Shipments & Fulfilment)
- **Header Table (`llx_expedition`):**
  - Primary Key: `rowid`
  - Ref: `SHyyMM-nnnn`
  - Foreign Keys: `fk_soc` -> `llx_societe(rowid)`, `fk_user_author` -> `llx_user(rowid)`
  - Origin Link: `origin` = 'commande', `origin_id` -> `llx_commande(rowid)`
- **Lines Table (`llx_expeditiondet`):**
  - Foreign Keys: `fk_expedition` -> `llx_expedition(rowid)`, `fk_origin_line` -> `llx_commandedet(rowid)`, `fk_entrepot` -> `llx_entrepot(rowid)`
  - Metrics: `qty`

#### Table: `llx_facture` & `llx_facturedet` (Customer Invoices)
- **Header Table (`llx_facture`):**
  - Primary Key: `rowid`
  - Ref: `INyyMM-nnnn`
  - Foreign Keys: `fk_soc` -> `llx_societe(rowid)`, `fk_user_author` -> `llx_user(rowid)`
  - Financials: `total_ht`, `total_ttc`, `tva`
  - Payment Status: `paye` (0 = Unpaid, 1 = Completely Paid)
- **Lines Table (`llx_facturedet`):**
  - Foreign Keys: `fk_facture` -> `llx_facture(rowid)`, `fk_product` -> `llx_product(rowid)`

#### Table: `llx_paiement` & `llx_paiement_facture` (Customer Payments)
- **Payment Table (`llx_paiement`):**
  - Primary Key: `rowid`
  - Ref: `num_paiement` (`TXN-O2C-HDFC-001`)
  - Attributes: `amount`, `datep`, `fk_paiement` (2 = Bank Transfer), `fk_bank`
- **Junction Table (`llx_paiement_facture`):**
  - Links: `fk_paiement` -> `llx_paiement(rowid)`, `fk_facture` -> `llx_facture(rowid)`
  - Amount: `amount`

---

### 1.3 Procure-to-Pay (P2P) Workflow Tables

#### Table: `llx_commande_fournisseur` & `llx_commande_fournisseurdet` (Purchase Orders)
- **Header Table (`llx_commande_fournisseur`):**
  - Primary Key: `rowid`
  - Ref: `POyyMM-nnnn`
  - Foreign Keys: `fk_soc` -> `llx_societe(rowid)`, `fk_user_author` -> `llx_user(rowid)`
  - Totals: `total_ht`, `total_ttc`, `tva`
  - Status: `fk_statut` (1 = Validated, 2 = Approved, 3 = Sent, 5 = Received Completely)
- **Lines Table (`llx_commande_fournisseurdet`):**
  - Foreign Keys: `fk_commande` -> `llx_commande_fournisseur(rowid)`, `fk_product` -> `llx_product(rowid)`
  - Metrics: `qty`, `subprice`, `total_ht`, `total_ttc`, `tva_tx`

#### Table: `llx_facture_fourn` & `llx_facture_fourn_det` (Supplier Invoices)
- **Header Table (`llx_facture_fourn`):**
  - Primary Key: `rowid`
  - Ref: `SIyyMM-nnnn`
  - Supplier External Ref: `ref_supplier` (`CWD-INV-84920`)
  - Foreign Keys: `fk_soc` -> `llx_societe(rowid)`, `fk_user_author` -> `llx_user(rowid)`
  - Totals: `total_ht`, `total_ttc`, `tva`
  - Payment Status: `paye` (1 = Paid)

#### Table: `llx_paiementfourn` & `llx_paiementfourn_facturefourn` (Supplier Disbursements)
- **Disbursement Table (`llx_paiementfourn`):**
  - Primary Key: `rowid`
  - Ref: `num_paiement` (`TXN-P2P-HDFC-001`)
  - Attributes: `amount`, `datep`, `fk_bank`
- **Junction Table (`llx_paiementfourn_facturefourn`):**
  - Links: `fk_paiementfourn` -> `llx_paiementfourn(rowid)`, `fk_facturefourn` -> `llx_facture_fourn(rowid)`

---

### 1.4 Financial & Inventory Audit Tables

#### Table: `llx_stock_mouvement` (Inventory Ledger)
- **Description:** Immutable transaction journal tracking all stock increases and decreases.
- **Primary Key:** `rowid`
- **Foreign Keys:** `fk_product` -> `llx_product(rowid)`, `fk_entrepot` -> `llx_entrepot(rowid)`, `fk_user_author` -> `llx_user(rowid)`
- **Attributes:** `value` (Quantity delta, + or -), `price` (Valuation basis), `label` (Audit memo)

#### Table: `llx_bank` & `llx_bank_account` (Treasury & Cash Flow Ledger)
- **Account Table (`llx_bank_account`):**
  - Primary Key: `rowid`
  - Ref: `ref` (`HDFC-01`)
  - Attributes: `bank`, `number`, `currency_code` (`INR`), `solde` (Current balance)
- **Ledger Entries (`llx_bank`):**
  - Primary Key: `rowid`
  - Foreign Key: `fk_account` -> `llx_bank_account(rowid)`
  - Financials: `amount` (Positive for customer receipts, negative for supplier payouts), `label`
