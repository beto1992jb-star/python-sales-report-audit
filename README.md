# Python Sales Report Script — Bug Fix & Audit

## Overview
This repository contains the audited and fixed version of `sales_report.py`, an automated Python & Pandas ETL reporting script designed to process retail transaction data (`sales.csv`) and output key business metrics: total revenue, regional sales breakdown, top-selling products, and regional average ticket size

## Issues Identified & Resolved

1. **Syntax Error (`average_ticket`)**
   - **Issue:** Used an assignment operator (`=`) instead of a comparison operator (`==`) inside the Pandas boolean filter (`df[df["region"] = region]`), causing Python to raise a `SyntaxError` during parsing before execution
   - **Fix:** Replaced `=` with `==`

2. **Incorrect Revenue Aggregation (`revenue_by_region`)**
   - **Issue:** Used `.mean()` instead of `.sum()`, returning average line-item revenue per region rather than total regional revenue
   - **Fix:** Replaced `.mean()` with `.sum()`

3. **Inverted Product Ranking (`top_products`)**
   - **Issue:** `.sort_values()` defaulted to ascending order, returning the 3 lowest-selling products instead of the top 3 bestsellers
   - **Fix:** Added `ascending=False` to sort from highest to lowest units sold

## How to Run

1. Ensure `pandas` is installed:
   ```bash
   pip install pandas

2. Run the script in the same directory as sales.csv:
python sales_report.py

   Expected Output
   
   === SALES REPORT ===
Total revenue: 6,457,100.00

Revenue by region:
  Este: 3,913,800.00
  Sur: 1,361,000.00
  Norte: 650,300.00
  Oeste: 532,000.00

Top 3 products by units sold:
  Teclado: 37
  Monitor: 32
  Webcam: 24

Average ticket (Norte): 108,383.33
