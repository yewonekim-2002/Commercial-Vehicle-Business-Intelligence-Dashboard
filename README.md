# Commercial Vehicle Sales Analysis & BI Dashboard

## Project Overview

This project analyzes commercial vehicle sales data to identify sales trends, regional performance, and vehicle category performance. The project combines Python for data cleaning and exploratory data analysis (EDA) with Power BI for interactive dashboard development.

The goal of this project is to demonstrate an end-to-end data analysis workflow, from raw data preparation to business intelligence reporting.

---

## Tools & Technologies

* **Python**

  * Pandas
  * NumPy
  * Matplotlib
  * Seaborn
* **Power BI**
* **Jupyter Notebook**
* **Git & GitHub**

---

## Project Structure

```text
commercial-vehicle-sales-analysis/
│
├── data/
│   ├── sales_data.csv
│   └── generate_data.py
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   └── 02_eda.ipynb
│
├── powerbi/
│   └── Commercial_Vehicle_Dashboard.pbix
│
└── README.md
```

---

## Data Cleaning

The following data preparation steps were performed using Python:

* Converted the `date` column into datetime format.
* Identified and handled missing values.
* Replaced missing values in the `industry` column with `"Unknown"`.
* Replaced missing values in `unit_price` using the mean value.
* Created additional time-based features for analysis.

---

## Exploratory Data Analysis (EDA)

The analysis focused on:

### Monthly Sales Trend

* Analyzed monthly revenue trends to identify seasonal patterns.

### Revenue by State

* Compared sales performance across Australian states.

### Revenue by Vehicle Type

* Evaluated revenue contribution by vehicle category.

### Industry Analysis

* Investigated revenue distribution across different industries.

---

## Power BI Dashboard

An interactive dashboard was developed in Power BI to monitor key business metrics.

### Dashboard Features

* KPI Cards

  * Total Revenue
  * Total Units Sold
  * Average Unit Price
  * Number of Transactions

* Monthly Revenue Trend

* Revenue by State

* Revenue by Vehicle Type

* Dynamic filtering by vehicle type

---

## Key Insights

* Revenue fluctuates throughout the year, indicating seasonal sales patterns.
* Certain states consistently generate higher revenue than others.
* Vehicle categories contribute differently to overall sales performance.
* Interactive filters allow users to explore sales performance from multiple perspectives.

---

## Future Improvements

* Add additional slicers for state and industry.
* Implement advanced DAX measures in Power BI.
* Build forecasting models for future sales prediction.
* Connect Power BI to a live database.

---

### Author

**Yewon Kim**  
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yewonekim-2002)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/yewone_22)
