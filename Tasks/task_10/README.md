# Smart City Traffic Analysis

## Overview

A beginner-friendly **traffic congestion analysis project** using synthetic smart city data. The project covers data generation, machine learning modeling, and visualization to demonstrate a complete data analysis workflow suitable for portfolios.

## Dataset

* **Type:** Synthetic traffic data (1000 records)
* **Source (Kaggle):** [https://www.kaggle.com/datasets/zainlatif/trafic-data-smart-city](https://www.kaggle.com/datasets/zainlatif/trafic-data-smart-city)
* **Key Features:**

  * Timestamp, Latitude, Longitude
  * Traffic Volume
  * Weather (Clear, Rainy, Foggy)
  * Accidents
  * Congestion (0 = Low, 1 = High)

## Workflow

1. **Data Preparation** – Generated and validated a clean dataset.
2. **Feature Engineering** – Extracted `Hour` from timestamp and encoded weather.
3. **Modeling** – Trained a **Random Forest Classifier** to predict congestion.
4. **Evaluation** – Achieved 100% accuracy (expected due to controlled synthetic data).
5. **Visualization** – Feature importance and traffic–congestion relationships.

## Tools & Tech

* Python, Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn

## Future Work

* Interactive **Power BI dashboard**:

  * Hourly traffic trends
  * Congestion heatmaps
  * Weather & accident impact analysis

## Repository Files

* `smart_city_traffic_synthetic.csv`
* `Smart_City_Traffic_Analysis.ipynb`
* `README.md`

## How to Run

1. Clone the repo.
2. Open `Smart_City_Traffic_Analysis.ipynb`.
3. Run all cells.

## Author

**Zain Latif**
GitHub: [https://github.com/zainlatif](https://github.com/zainlatif)
