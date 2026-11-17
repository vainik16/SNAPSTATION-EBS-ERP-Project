# SnapStation ERP - Demo Database

Sanitized demonstration database for the SnapStation Dolibarr ERP project.

## Requirements
- macOS
- MySQL Server 8.0
- Dolibarr ERP 20.0.3
- Compatible PHP installation

## Clone the repository
git clone https://github.com/vainik16/SNAPSTATION-EBS-ERP-Project.git
cd SNAPSTATION-EBS-ERP-Project

## Create the database
mysql -u root -p -e "CREATE DATABASE snapstation_demo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

## Import the dataset
mysql -u root -p snapstation_demo < database/snapstation_demo.sql

## Dolibarr database configuration
Database type: mysqli
Host: localhost
Port: 3306
Database: snapstation_demo
Table prefix: llx_
Use your own local MySQL username and password.
Install Dolibarr 20.0.3 separately. Do not run a fresh installation over the imported tables.
Never upload your local conf.php file.

## Demo login accounts
Username: demo_admin_07, demo_admin_08, demo_admin_09, demo_admin_10, demo_admin_11
Shared demo password: SnapStationDemo2026!
These are public demonstration credentials. Change them before any non-demo use.

## Dataset contents
280 tables; 5 users; 15 customers and suppliers; 30 products;
10 sales orders; 10 purchase orders; 6 customer invoices;
7 supplier invoices; 76 stock movements; 1 proposal.

## Notes
- Customer and supplier identities and contact details are anonymized.
- Sensitive bank details and configuration credentials are cleared.
- Scheduled cron jobs are disabled.
- Physical document attachments are not included.
- This is a demonstration database, not a production database.
- Import was tested in a separate MySQL database.

## Demonstrated workflows
- Customer and supplier management
- Product management
- Sales and purchase orders
- Customer and supplier invoicing
- Inventory and stock movements
- Business proposals

Project: SNAPSTATION - Enterprise Business Systems
ERP: Dolibarr 20.0.3
