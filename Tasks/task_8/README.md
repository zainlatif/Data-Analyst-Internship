# Ecommerce Sales Prediction & Analysis

## Overview
This project focuses on **sales prediction and performance analysis** for an ecommerce store using historical transaction data.  
The goal is to clean the dataset, analyze sales patterns, and build a **Linear Regression model** to predict sales with high accuracy.  
A **Power BI dashboard** is created to visualize revenue, profit, and regional performance.

## Dataset
Source: Kaggle – Ecommerce Store Data  
https://www.kaggle.com/datasets/zainlatif/ecommerce-store-data

- Records: Ecommerce sales transactions
- Target Variable: **Total Sales**

## Data Quality
Missing values per column:

- Order ID: 0  
- Date: 0  
- Product: 0  
- Category: 0  
- Quantity: 0  
- Unit Price: 0  
- Total: 0  
- Profit: 0  
- Region: 0  

✅ Dataset required **no missing-value imputation**  
✅ Cleaned dataset saved as:  
`ecommerce_sales_data_cleaned.csv`

## Model Used – Linear Regression
**Linear Regression** was used to model the relationship between sales-related features and total revenue due to:
- Simplicity and interpretability
- Strong linear relationship in the data
- High predictive performance on cleaned data

### Model Evaluation
- **R² Score:** 99.40%
- **Mean Absolute Error (MAE):** 18.20
- **Root Mean Squared Error (RMSE):** 22.44

⚠️ Note: High accuracy indicates strong feature correlation. Results were validated on a test split.

## Project Workflow
1. **Data Cleaning**
   - Verified missing values
   - Converted data types
   - Feature validation

2. **Exploratory Data Analysis (EDA)**
   - Sales and profit trends
   - Category and regional performance

3. **Model Training**
   - Train-test split
   - Linear Regression model training

4. **Evaluation**
   - R², MAE, RMSE metrics

5. **Visualization**
   - **Power BI dashboard** showing:
     - Total sales and profit
     - Category-wise performance
     - Region-wise revenue trends

## Tools & Technologies
- Python (Pandas, NumPy, Scikit-learn)
- Jupyter Notebook
- Power BI
- Kaggle

## Author
**Zain Latif**  
Data Science Intern | Computer Science Graduate  
Faisalabad, Pakistan