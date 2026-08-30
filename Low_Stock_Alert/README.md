# Low Stock Alert System

Python automation project for detecting low-stock kiosk spare parts and generating an alert report.

## Project Overview

This script reads inventory transaction data from `inventory.csv`, calculates the total stock quantity per item, and generates a low-stock alert report when an item falls below a user-defined threshold.

The project was inspired by real kiosk maintenance operations where spare parts such as printers, bill acceptors, routers, and thermal paper must be monitored regularly.

---

## Features

* Reads inventory data from a CSV file
* Aggregates stock quantities per item
* Accepts a custom minimum stock threshold
* Displays low-stock items in the terminal
* Generates `inventory_summary.csv`
* Generates `low_stock_report.csv`
* Adds timestamps to alert entries for historical tracking

---

## Technologies Used

* Python 3
* `csv` module
* `datetime` module
* `os` module

---

## How It Works

1. Read `inventory.csv`
2. Group records by item name
3. Sum all quantities for each item
4. Save the summarized inventory to `inventory_summary.csv`
5. Compare each stock quantity with the threshold
6. Save low-stock items to `low_stock_report.csv`

---

## Example Input (`inventory.csv`)

```csv
Item Name,Quantity,Unit Value
Printer,2,10000
Printer,1,5000
Router,3,6000
Thermal Paper,10,45
```

---

## Example Terminal Output

```text
Enter minimum stock threshold: 20

LOW STOCK ALERT!

Threshold: 20
============================
Printer | Stock: 3
Router | Stock: 3
Thermal Paper | Stock: 10

Successfully logged to low_stock_report.csv file
```

---

## Example Report (`low_stock_report.csv`)

```csv
Timestamp,Item name,Quantity
2026-08-07 23:42:14,Printer,3
2026-08-07 23:42:14,Router,3
2026-08-07 23:42:14,Thermal Paper,10
```

---

## Skills Demonstrated

* File handling
* CSV processing
* Dictionary aggregation
* Conditional logic
* Reporting automation
* Timestamp logging
* Basic operational monitoring

---

## What I Learned

During development I learned how to:

* Aggregate values using dictionaries
* Distinguish CSV headers from dictionary keys
* Debug duplicate file writes
* Design logic before coding
* Build reusable operational automation scripts

---
