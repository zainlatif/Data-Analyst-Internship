# Telecom Customer Churn Prediction System

## Overview
Customer churn in the **telecommunication industry** happens when customers leave due to **poor network quality, high service charges, weak customer support, or short-term contracts**.  
This project builds a **machine learning–based churn prediction system** using telecom customer data to identify customers at high risk of churn and support retention strategies.

## Dataset
Source: Kaggle – Telecom Customer Dataset  
https://www.kaggle.com/datasets/jazidesigns/telecom-dataset

- Records: **7,043**
- Features: **21**
- Target Variable: **Churn** (Yes / No)

## Key Features
- Demographics: Gender, SeniorCitizen, Partner, Dependents  
- Account Info: Tenure, Contract, Payment Method, PaperlessBilling  
- Services: PhoneService, InternetService, TechSupport, Streaming services  
- Charges: MonthlyCharges, TotalCharges  

## Model Used – CatBoost
**CatBoost Classifier** was used as the primary model due to:
- Native handling of **categorical features** (no heavy encoding needed)
- Strong performance on **tabular telecom data**
- Reduced overfitting compared to traditional tree models

**Train/Test Split:** 80 / 20  
**Model Accuracy:** ~80%

## Installation
Install required dependencies using pip:

```bash
pip install catboost pandas numpy scikit-learn matplotlib seaborn
