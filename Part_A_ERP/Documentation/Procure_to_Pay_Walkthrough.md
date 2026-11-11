# BUSINESS PROCESS 2 Ã¢â‚¬â€ PROCURE-TO-PAY (P2P) WALKTHROUGH
**System:** SNAPSTATION Dolibarr ERP 20.0.3
**Vendor Entity:** CameraWorld Distributors (`SU2611-00001`)
**PO Reference:** `PO2611-0001`
**Total Value:** Ã¢â€šÂ¹2,95,000.00 (Inclusive of 18% GST)
**Assigned Leads:** Skanda (Procurement), Sujal (Logistics), Shreyank (Finance)

---

## Workflow Stages & Technical Execution

### Stage 1: Stock Shortage & Replenishment Alert
- **Action:** System detected stock falling below safety thresholds prior to high-season wedding bookings.
- **Deficit Items:**
  1. `360-001`: 360-Degree Video Booth Platform (Current Stock: 2, Buffer: 5, Reorder Qty: 2)
  2. `CAM-001`: DSLR Camera X1 Body & Kit (Current Stock: 5, Buffer: 8, Reorder Qty: 2)
  3. `PB-004`: Instant Dye-Sublimation Photo Printer (Current Stock: 4, Buffer: 6, Reorder Qty: 2)
- **Status:** Replenishment Triggered.
- **Artifact:** `Part_A_ERP/Screenshots/Procure_to_Pay/P2P_01_Stock_Requirement_Analysis.png`

### Stage 2: Purchase Order Draft (`PO2611-0001`)
- **Action:** Skanda (`PES1UG24CS457`) raised Purchase Order `PO2611-0001` to CameraWorld Distributors.
- **Commercial Valuation:**
  - 2 x 360 Platforms @ Ã¢â€šÂ¹60,000 = Ã¢â€šÂ¹1,20,000.00
  - 2 x DSLR Cameras @ Ã¢â€šÂ¹40,000 = Ã¢â€šÂ¹80,000.00
  - 2 x Photo Printers @ Ã¢â€šÂ¹25,000 = Ã¢â€šÂ¹50,000.00
  - Subtotal (Net): Ã¢â€šÂ¹2,50,000.00  Ã¢â‚¬Â¢  GST (18%): Ã¢â€šÂ¹45,000.00  Ã¢â‚¬Â¢  Total: Ã¢â€šÂ¹2,95,000.00
- **Status:** Draft.
- **Artifact:** `Part_A_ERP/Screenshots/Procure_to_Pay/P2P_02_Purchase_Order_Draft.png`

### Stage 3: Purchase Order Approval & Vendor Transmission
- **Action:** Skanda validated the purchase order.
- **System Impact:** Order status changed to 'Approved / Ordered', generating `PO2611-0001.pdf` transmitted to vendor.
- **Status:** Approved / Ordered.
- **Artifact:** `Part_A_ERP/Screenshots/Procure_to_Pay/P2P_03_Purchase_Order_Approved.png`

### Stage 4: Inward Goods Reception & Stock Inward (`REC2611-0001`)
- **Action:** Warehouse Manager Sujal (`PES1UG24CS476`) received consignment at Bengaluru Main Equipment Hub (`WH-BLR-01`).
- **System Impact:** QA inspection verified 100% item integrity; physical stock incremented by +6 units in `llx_stock_mouvement`.
- **Status:** Received into Hub.
- **Artifact:** `Part_A_ERP/Screenshots/Procure_to_Pay/P2P_04_Goods_Receipt_Stock_Entry.png`

### Stage 5: Supplier Invoice Verification & 3-Way Match (`SI2611-0001`)
- **Action:** Finance Analyst Shreyank (`PES1UG24CS443`) conducted 3-way match: PO (`PO2611-0001`) = Receipt (`REC2611-0001`) = Invoice (`SI2611-0001`).
- **Compliance:** 100% variance-free reconciliation. Input Tax Credit (ITC) of Ã¢â€šÂ¹45,000.00 recognized under GSTR-2B.
- **Status:** Validated / Approved for Payment.
- **Artifact:** `Part_A_ERP/Screenshots/Procure_to_Pay/P2P_05_Supplier_Invoice.png`

### Stage 6: Supplier Payment & Disbursement (`TXN-P2P-HDFC-001`)
- **Action:** Electronic RTGS disbursement of Ã¢â€šÂ¹2,95,000.00 to CameraWorld Distributors from HDFC Operating Account.
- **Accounting Impact:** Vendor invoice balance cleared to Ã¢â€šÂ¹0.00, completing the Procure-to-Pay cycle.
- **Status:** Settled / Paid in Full.
- **Artifact:** `Part_A_ERP/Screenshots/Procure_to_Pay/P2P_06_Supplier_Payment.png`
