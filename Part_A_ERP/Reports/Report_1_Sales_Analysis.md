# REPORT 1: SALES ORDERS AND REVENUE ANALYSIS
**Enterprise:** SNAPSTATION EVENT TECHNOLOGIES
**Academic Course:** UE24CS343AB8 Enterprise Business Systems (EBS)
**Database Source:** `dolibarr_snapstation` (MySQL 8.0)

### Summary Metrics:
- **Total Sales Orders:** 10
- **Total Product Line Items Sold:** 32
- **Total Units Sold:** 50
- **Total Sales Value (excl. Tax / HT):** Ã¢â€šÂ¹1,456,900.00
- **Total Sales Value (incl. 18% GST / TTC):** Ã¢â€šÂ¹1,719,142.00

### Transactional Breakdown:
| Order_Ref | Order_Date | Customer_Name | Product_Ref | Product_Name | Quantity | Unit_Price_INR | Subtotal_HT_INR | Total_TTC_INR | Order_Status | Responsible_Member |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SO2611-0001 | 2026-11-07 | Royal Moments Weddings | SRV-004 | Professional DSLR Camera Rental (Per Day) | 1 | 3500.0 | 3500.0 | 4130.0 | Closed/Billed | Vainik |
| SO2611-0001 | 2026-11-07 | Royal Moments Weddings | PB-001 | Classic Photobooth Machine | 1 | 150000.0 | 150000.0 | 177000.0 | Closed/Billed | Vainik |
| SO2611-0001 | 2026-11-07 | Royal Moments Weddings | 360-001 | 360-Degree Video Booth Platform 100cm | 1 | 85000.0 | 85000.0 | 100300.0 | Closed/Billed | Vainik |
| SO2611-0001 | 2026-11-07 | Royal Moments Weddings | CON-001 | Instant Photo Paper Pack (500 Sheets) | 1 | 3200.0 | 3200.0 | 3776.0 | Closed/Billed | Vainik |
| SO2611-0001 | 2026-11-07 | Royal Moments Weddings | PB-006 | Custom Modular Backdrop Stand | 1 | 8500.0 | 8500.0 | 10030.0 | Closed/Billed | Vainik |
| SO2611-0001 | 2026-11-07 | Royal Moments Weddings | LGT-001 | Professional Bi-Color LED Studio Panel | 2 | 18000.0 | 36000.0 | 42480.0 | Closed/Billed | Vainik |
| SO2611-0010 | 2026-11-07 | Forever Frames Weddings | SRV-001 | Classic Photobooth Rental Package (Full Day) | 1 | 25000.0 | 25000.0 | 29500.0 | Closed/Billed | Skanda |
| SO2611-0010 | 2026-11-07 | Forever Frames Weddings | ACC-005 | Keepsake Photo Frame Pack (50 pcs) | 2 | 2500.0 | 5000.0 | 5900.0 | Closed/Billed | Skanda |
| SO2611-0010 | 2026-11-07 | Forever Frames Weddings | PB-006 | Custom Modular Backdrop Stand | 1 | 8500.0 | 8500.0 | 10030.0 | Closed/Billed | Skanda |
| SO2611-0009 | 2026-11-06 | Grand Gala Events | PB-001 | Classic Photobooth Machine | 1 | 150000.0 | 150000.0 | 177000.0 | Validated | Vainik |
| SO2611-0009 | 2026-11-06 | Grand Gala Events | PB-004 | Instant Photo Printer | 1 | 38000.0 | 38000.0 | 44840.0 | Validated | Vainik |
| SO2611-0009 | 2026-11-06 | Grand Gala Events | CON-001 | Instant Photo Paper Pack (500 Sheets) | 3 | 3200.0 | 9600.0 | 11328.0 | Validated | Vainik |
| SO2611-0008 | 2026-11-05 | Lens & Light Photography | CAM-001 | DSLR Camera X1 | 1 | 45000.0 | 45000.0 | 53100.0 | Closed/Billed | Shreyank |
| SO2611-0008 | 2026-11-05 | Lens & Light Photography | LENS-002 | Portrait Camera Lens 85mm f/1.4 | 1 | 42000.0 | 42000.0 | 49560.0 | Closed/Billed | Shreyank |
| SO2611-0008 | 2026-11-05 | Lens & Light Photography | ACC-002 | High-Capacity Camera Battery | 2 | 3500.0 | 7000.0 | 8260.0 | Closed/Billed | Shreyank |
| SO2611-0008 | 2026-11-05 | Lens & Light Photography | ACC-003 | Memory Card 128GB High-Speed | 2 | 4200.0 | 8400.0 | 9912.0 | Closed/Billed | Shreyank |
| SO2611-0007 | 2026-11-04 | CorporateSpark Events | SRV-002 | 360-Degree Video Booth Experience Package (Full Day) | 1 | 35000.0 | 35000.0 | 41300.0 | Validated | Sujal |
| SO2611-0007 | 2026-11-04 | CorporateSpark Events | LGT-003 | Wireless RGB Event Light Tube | 4 | 9500.0 | 38000.0 | 44840.0 | Validated | Sujal |
| SO2611-0006 | 2026-11-03 | UrbanFrame Studios | CAM-003 | Professional 4K Video Camera | 1 | 120000.0 | 120000.0 | 141600.0 | Closed/Billed | Skanda |
| SO2611-0006 | 2026-11-03 | UrbanFrame Studios | LENS-001 | Wide-Angle Camera Lens 16-35mm | 2 | 35000.0 | 70000.0 | 82600.0 | Closed/Billed | Skanda |
| SO2611-0005 | 2026-11-02 | DreamDay Wedding Planners | 360-001 | 360-Degree Video Booth Platform 100cm | 1 | 85000.0 | 85000.0 | 100300.0 | Validated | Vainik |
| SO2611-0005 | 2026-11-02 | DreamDay Wedding Planners | 360-003 | Motorised Camera Arm | 1 | 28000.0 | 28000.0 | 33040.0 | Validated | Vainik |
| SO2611-0005 | 2026-11-02 | DreamDay Wedding Planners | 360-004 | LED Lighting Ring 360 | 1 | 12000.0 | 12000.0 | 14160.0 | Validated | Vainik |
| SO2611-0004 | 2026-11-01 | Celebration Hub Events | PB-002 | Selfie Photobooth System | 1 | 95000.0 | 95000.0 | 112100.0 | Validated | Shreyank |
| SO2611-0004 | 2026-11-01 | Celebration Hub Events | PB-005 | Photobooth Ring Light 18" | 2 | 7500.0 | 15000.0 | 17700.0 | Validated | Shreyank |
| SO2611-0004 | 2026-11-01 | Celebration Hub Events | ACC-001 | Heavy-Duty Camera Tripod | 2 | 6500.0 | 13000.0 | 15340.0 | Validated | Shreyank |
| SO2610-0003 | 2026-10-31 | PES Event Committee | SRV-003 | Premium Wedding Hybrid Experience (Photobooth + 360 Video) | 1 | 55000.0 | 55000.0 | 64900.0 | Closed/Billed | Sujal |
| SO2610-0003 | 2026-10-31 | PES Event Committee | CON-001 | Instant Photo Paper Pack (500 Sheets) | 3 | 3200.0 | 9600.0 | 11328.0 | Closed/Billed | Sujal |
| SO2610-0003 | 2026-10-31 | PES Event Committee | CON-002 | Printer Ink Cartridge Ribbon | 2 | 4800.0 | 9600.0 | 11328.0 | Closed/Billed | Sujal |
| SO2610-0002 | 2026-10-30 | PixelCraft Photography Studio | CAM-002 | Mirrorless Camera M1 | 2 | 75000.0 | 150000.0 | 177000.0 | Closed/Billed | Skanda |
| SO2610-0002 | 2026-10-30 | PixelCraft Photography Studio | LENS-002 | Portrait Camera Lens 85mm f/1.4 | 2 | 42000.0 | 84000.0 | 99120.0 | Closed/Billed | Skanda |
| SO2610-0002 | 2026-10-30 | PixelCraft Photography Studio | ACC-001 | Heavy-Duty Camera Tripod | 2 | 6500.0 | 13000.0 | 15340.0 | Closed/Billed | Skanda |
