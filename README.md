Solar Power Output Prediction using Machine Learning

Overview:
This project predicts the AC power output of a solar power plant using weather sensor data (irradiation, ambient temperature, module temperature). It combines electrical engineering domain knowledge with machine learning to demonstrate how solar generation can be modeled and forecasted.

Motivation:
Solar power output is highly dependent on environmental conditions. Being able to predict output from weather data is useful for grid planning, maintenance scheduling, and identifying underperforming inverters. This project explores how well simple ML models can capture that relationship.

Dataset:
Source: Solar Power Generation Data (Kaggle)
Contents: 34 days of data from two solar power plants in India

Generation data: DC power, AC power, daily yield, total yield (per inverter, 15-min intervals)
Weather sensor data: ambient temperature, module temperature, irradiation (15-min intervals)

Approach:
Data Loading & Cleaning — Loaded generation and weather CSVs, converted timestamps to datetime format.
Merging — Joined generation and weather data on DATE_TIME and PLANT_ID, since one weather sensor's readings apply to all inverters in a plant at a given timestamp.
Exploratory Data Analysis — Visualized relationships between AC power and each weather feature via scatter plots.
Modeling — Trained and compared two models:

Linear Regression (baseline)
Random Forest Regressor (to capture potential non-linear effects)

Evaluation — Assessed models using RMSE and R² score, and analyzed feature importance.

Key Findings:
Irradiation is by far the strongest predictor of AC power output (feature importance ≈ 0.997 in the Random Forest model), consistent with the physical principle that solar panels convert incoming solar energy directly into electrical power.
Module and ambient temperature have a much weaker, noisier relationship with output — they affect panel efficiency rather than directly driving generation.
Linear Regression: RMSE ≈ 55.5, R² ≈ 0.980
Random Forest: RMSE ≈ 45.7, R² ≈ 0.986

Random Forest slightly outperformed Linear Regression, suggesting minor non-linear effects (e.g., temperature-related efficiency losses) exist beyond a simple linear relationship — but the fact that a basic linear model already achieves R² of 0.98 confirms that solar generation is a largely physics-driven, near-linear process.

Tech Stack:
Python (Google Colab)
pandas, numpy — data handling
matplotlib — visualization
scikit-learn — modeling (Linear Regression, Random Forest)

How to Run:
Open the notebook in Google Colab.
Set up a Kaggle API token and download the dataset (anikannal/solar-power-generation-data).
Run all cells sequentially — data loading → merging → EDA → modeling → evaluation.

Possible Extensions:
Incorporate time-based features (hour of day, day of week) to capture daily/seasonal patterns.
Compare additional models (XGBoost, Gradient Boosting).
Extend analysis to Plant 2 and compare performance across plants.
Build a simple dashboard (Streamlit) for real-time prediction input.

Author
Jithesh Kumar A — Electrical & Electronics Engineering, KPR Institute of Engineering and Technology.
Author

[Your Name] — Electrical & Electronics Engineering, [Your College]
