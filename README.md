# 🏠 Real Estate Market Tracker using Power BI & Web Scraping

## 📌 Project Overview

This project analyzes real estate market trends using property listing data scraped from **Magicbricks.com**.
The focus is on understanding **property pricing behavior, neighborhood-level value differences, and market inventory patterns** using an interactive **Power BI dashboard**.

The project demonstrates a complete **data analytics workflow** — from web scraping and data cleaning to feature engineering and business-focused visualization.

---

## 🎯 Objectives

* Analyze **average property prices** and **price per square foot**
* Compare pricing patterns across **different BHK configurations**
* Identify **premium and affordable localities**
* Understand **market inventory** using listing distribution
* Build a **clear and insight-driven Power BI dashboard**

---

## 🌐 Data Collection

* **Source:** Magicbricks.com
* **Method:** Web scraping using **Python (Requests + BeautifulSoup)**
* Data was extracted from **server-rendered HTML and structured metadata** available in the page source.
* Scraping was limited in scope and used strictly for **educational and portfolio purposes**.

---

## 🧾 Dataset Description

The cleaned dataset contains the following columns:

| Column Name    | Description                   |
| -------------- | ----------------------------- |
| Price          | Property price                |
| Area_sqft      | Built-up area in square feet  |
| Price_per_sqft | Derived metric (Price ÷ Area) |
| BHK            | Number of bedrooms            |
| Locality       | Property neighborhood         |
| City           | City name                     |

📁 File: `magicbricks_clean.csv`

---

## 🧹 Data Cleaning & Feature Engineering

* Removed currency symbols and text noise from price values
* Converted numerical fields into appropriate data types
* Extracted BHK and area information
* Engineered **Price per Sq Ft** for standardized price comparison
* Checked and handled missing or inconsistent values

---

## 📊 Power BI Dashboard Overview

### 🔹 Key KPIs

* Average Price per Sq Ft
* Average Property Price
* Total Listings
* Average Area (sqft)

---

### 🔹 Visualizations Included

* **Locality-wise Price Analysis:** Average price per sq ft by neighborhood
* **BHK-wise Comparison:** Average property price across BHK configurations
* **Scatter Plot (Area vs Price):** Identifies over- and under-priced properties
* **Market Inventory Proxy:** Listing count by locality
* **Summary KPIs:** Overall market overview

> The dashboard is designed to provide **clear insights without slicers**, focusing on comparison and pattern recognition at a glance.

---

## 📈 Key Insights

* Significant variation in **price per square foot across localities**
* Certain neighborhoods command **premium pricing despite smaller areas**
* High listing concentration in some localities suggests **potential oversupply**
* Larger property size does not always translate to better price efficiency

---

## 🛠 Tools & Technologies

* **Python:** Requests, BeautifulSoup, Pandas
* **Power BI:** Data modeling, DAX measures, data visualization
* **Data Analysis:** Feature engineering and exploratory analysis

---


## ⚠️ Limitations

* JavaScript-rendered content restricts full data extraction using BeautifulSoup alone
* Market inventory is inferred using **listing count**, not actual sold dates
* The dataset represents a **snapshot of listings** at the time of scraping

---

## 🚀 Future Enhancements

* Add time-based scraping to analyze **price trends**
* Include **days-on-market** calculations
* Expand analysis to multiple cities
* Add amenity-level pricing impact

---

