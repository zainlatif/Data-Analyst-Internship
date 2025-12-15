# Smart City Traffic Analysis

## Project Overview
This project demonstrates a simple yet valuable **traffic analysis workflow** using synthetic data. The goal is to analyze traffic congestion based on various factors like time of day, weather, location, and accidents. The project includes data generation, model training, and visualizations, making it suitable for portfolio and beginner-friendly.

---

## Steps

### Step 1: Data Generation
- Generated a **synthetic dataset** of 1000 rows.
- Columns included:
  - `Timestamp` — date and time of observation
  - `Latitude` & `Longitude` — location coordinates
  - `Traffic_Volume` — number of vehicles observed
  - `Weather` — weather condition (Clear, Rainy, Foggy)
  - `Accidents` — number of accidents recorded
  - `Congestion` — binary target (0 = low, 1 = high)
- Data saved as `smart_city_traffic_synthetic.csv`.

### Step 2: Data Overview
- Inspected dataset shape, data types, null values, and unique values.
- Verified all columns are complete and ready for modeling.

### Step 3: Model Training
- Trained a **Random Forest Classifier** to predict traffic congestion.
- Features used: `Hour` (from Timestamp), `Weather`, `Latitude`, `Longitude`, `Traffic_Volume`, `Accidents`.
- Achieved **100% accuracy** on the synthetic dataset (expected for controlled data).
- Feature importance revealed `Traffic_Volume` and `Hour` as the most influential.

### Step 4: Visualization
- Visualized **feature importance**, **actual vs predicted congestion**, and **traffic volume vs congestion** using Matplotlib and Seaborn.
- These visualizations help understand model predictions and traffic patterns.

---

## Future Work: Power BI Dashboard
- Plan to create an **interactive Power BI dashboard**.
- Features to include:
  - Traffic volume trends by hour/day
  - Congestion heatmaps by location
  - Weather impact analysis
  - Accident hotspot analysis
- Users will be able to **explore traffic patterns interactively**.

---

## Files in Repository
- `smart_city_traffic_synthetic.csv` — synthetic dataset
- `Smart_City_Traffic_Analysis.ipynb` — Jupyter Notebook with code
- `README.md` — project description

---

## How to Run
1. Clone the repository.
2. Open the Jupyter Notebook `Smart_City_Traffic_Analysis.ipynb`.
3. Run all cells to generate visualizations and train the model.
4. Explore the dataset for further analysis or future Power BI integration.

---

## Author
**Zain Latif** — [GitHub](https://github.com/zainlatif)
