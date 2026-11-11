# BUSINESS PROCESS 1 Ã¢â‚¬â€ ORDER-TO-CASH (O2C) WALKTHROUGH
**System:** SNAPSTATION Dolibarr ERP 20.0.3
**Client Entity:** Royal Moments Weddings (`CU2611-00001`)
**Order Reference:** `SO2611-0001`
**Total Value:** Ã¢â€šÂ¹3,37,716.00 (Inclusive of 18% GST)
**Assigned Leads:** Vainik (Sales), Sujal (Logistics), Shreyank (Finance)

---

## Workflow Stages & Technical Execution

### Stage 1: Commercial Proposal / Quotation (`PR2611-0001`)
- **Action:** Created commercial proposal for client booking a luxury wedding photo experience at Palace Grounds, Bengaluru.
- **Line Items:**
  1. `SRV-001`: DSLR Camera Rental & Operating Crew (2 Days @ Ã¢â€šÂ¹8,000/day = Ã¢â€šÂ¹16,000)
  2. `SRV-003`: Classic Photobooth Complete Experience Package (1 Unit = Ã¢â€šÂ¹35,000)
  3. `SRV-004`: 360-Degree Video Booth Experience Package (1 Unit = Ã¢â€šÂ¹45,000)
  4. `CON-001`: Instant Photo Paper Pack (5 Packs @ Ã¢â€šÂ¹1,200 = Ã¢â€šÂ¹6,000)
  5. `PB-006`: Custom Wedding Backdrop Stand (1 Unit = Ã¢â€šÂ¹6,500)
  6. `LGT-001`: Professional LED Studio Light Panel (2 Units @ Ã¢â€šÂ¹12,500 = Ã¢â€šÂ¹25,000)
- **Status:** Validated and Accepted by Client.
- **Artifact:** `Part_A_ERP/Screenshots/Order_to_Cash/O2C_01_Commercial_Proposal.png`

### Stage 2: Sales Order Draft & Stock Reservation (`SO2611-0001`)
- **Action:** Proposal `PR2611-0001` automatically converted into Sales Order `SO2611-0001`.
- **Inventory Check:** System verified stock availability in `WH-BLR-01` (Bengaluru Main Equipment Hub).
- **Status:** Draft (Pre-validation).
- **Artifact:** `Part_A_ERP/Screenshots/Order_to_Cash/O2C_02_Sales_Order_Creation.png`

### Stage 3: Sales Order Validation & Resource Allocation
- **Action:** Sales Lead Vainik (`PES1UG24CS513`) validated the order.
- **System Impact:** Stock reserved, pricing locked, PDF `SO2611-0001.pdf` generated via Einstein model.
- **Status:** Validated / Processing.
- **Artifact:** `Part_A_ERP/Screenshots/Order_to_Cash/O2C_03_Sales_Order_Validated.png`

### Stage 4: Shipment & Warehouse Fulfillment (`SH2611-0001`)
- **Action:** Warehouse Operations Manager Sujal (`PES1UG24CS476`) created shipment docket `SH2611-0001`.
- **System Impact:** Equipment prepped, consumables decremented from `llx_stock_mouvement`, transit van dispatched to Palace Grounds under tracking `TRK-BLR-2026-9041`.
- **Status:** Closed / Delivered.
- **Artifact:** `Part_A_ERP/Screenshots/Order_to_Cash/O2C_04_Shipment_Delivery.png`

### Stage 5: Customer Invoicing & Statutory Tax Recognition (`IN2611-0001`)
- **Action:** Accounts Analyst Shreyank (`PES1UG24CS443`) generated Customer Invoice `IN2611-0001`.
- **Financial Breakdown:**
  - Net Amount (HT): Ã¢â€šÂ¹2,86,200.00
  - CGST (9.0%): Ã¢â€šÂ¹25,758.00
  - SGST (9.0%): Ã¢â€šÂ¹25,758.00
  - Total Billed (TTC): Ã¢â€šÂ¹3,37,716.00
- **Status:** Validated.
- **Artifact:** `Part_A_ERP/Screenshots/Order_to_Cash/O2C_05_Customer_Invoice.png`

### Stage 6: Customer Payment Receipt & Settlement (`TXN-O2C-0001`)
- **Action:** Payment received via NEFT/RTGS deposited into HDFC Current Operating Account (`HDFC-01`).
- **Accounting Impact:** Invoice marked paid in full (Remaining balance Ã¢â€šÂ¹0.00), bank transaction posted to `llx_bank`.
- **Status:** Settled / Reconciled.
- **Artifact:** `Part_A_ERP/Screenshots/Order_to_Cash/O2C_06_Customer_Payment.png`
