# Electricity Demand Prediction for Delhi

This project aims to develop an AI-based model for predicting electricity demand, including peak demand projection, for the Delhi power system. The model accounts for various factors such as seasonal variations, weather conditions, and public holidays to provide accurate forecasts.

## Table of Contents
- [Problem Statement](#problem-statement)
- [Project Structure](#project-structure)
- [Model Information](#model-information)
- [Model Inputs](#model-inputs)
- [Streamlit UI](#streamlit-ui)
- [Data Analysis (EDA)](#data-analysis-eda)
- [Technologies Used](#technologies-used)

## Problem Statement

### Problem Statement ID: 1624
**Title**: To develop an Artificial Intelligence (AI) based model for electricity demand projection including peak demand projection for the Delhi Power system.

**Description**: 
The power demand in Delhi shows significant variations between seasons and even within a single day. The peak load can reach up to 8300 MW during summer and drop to 2000 MW in winter. The project aims to create a predictive model that factors in:
- **Weather Effects**: Temperature, humidity, wind speed, and rainfall.
- **Public Holidays and Weekends**.
- **Natural Load Growth and Real Estate Development**.

The model should help manage the power purchase and supply efficiently by anticipating demand fluctuations.

## Project Structure
Electricity-Demand-Prediction/
├── analysis.py              # Script containing EDA functions
├── app.py                   # Main Streamlit app file
├── column_transformer_m.sav # Trained Column Transformer for data preprocessing
├── model_main.sav           # Trained Random Forest model
├── data.csv                 # Dataset used for EDA and model training
└── README.md                # Project documentation


## Model Information

- **Model Type**: Random Forest Regressor
- **Features**:
  - Hour of the day
  - Day of the week
  - Is it a holiday?
  - Season (Spring, Summer, Autumn, Winter)
  - Temperature (°C)
  - Humidity (%)
  - Wind Speed (km/h)
  - Rainfall (mm)
  - Peak Demand Met (MW)
  - Load Growth (%)
  - Energy Consumption (MUs)
  - Shedding (MUs)
  - Shedding as % of Energy Consumption
  - Transmission Losses (%)
  - System Availability (%)

## Model Inputs

The following parameters can be set to make a prediction:

	•	Hour of Day: The hour for which you want to project electricity demand (0-23).
	•	Day of Week: The day of the week (0-6, where 0 = Monday).
	•	Is Holiday: Whether it is a public holiday (Yes/No).
	•	Season: The current season (Spring, Summer, Autumn, Winter).
	•	Temperature: Temperature in °C.
	•	Humidity: Humidity in %.
	•	Wind Speed: Wind speed in km/h.
	•	Rainfall: Rainfall in mm.
	•	Peak Demand Met (MW): The peak demand met in MW.
	•	Load Growth (%): The percentage load growth.
	•	Energy Consumption (MUs): Energy consumption in MUs.
	•	Shedding (MUs): Shedding in MUs.
	•	Shedding as % of Energy Consumption: Shedding as a percentage of energy consumption.
	•	Transmission Losses (%): Transmission losses as a percentage.
	•	System Availability (%): System availability percentage.

Click the “Predict” button to generate the forecast.

## Streamlit UI

	•	Model Prediction:
	•	Provides an interface to input parameters and predict the electricity demand.
	•	Data Analysis (EDA):
	•	Offers various visualizations to understand the dataset.

## Data Analysis (EDA)

The EDA module provides insights into the dataset, including:

	1.	Electricity Load by Hour of Day: A bar chart showing the total electricity load for each hour.
	2.	Electricity Load During Holidays vs Non-Holidays: A line plot comparing the electricity load on holidays and non-holidays.
	3.	Electricity Load Distribution Across Seasons: A boxplot showing load distribution across different seasons.

## Technologies Used

	•	Python
	•	Streamlit
	•	scikit-learn
	•	Pandas
	•	Matplotlib
	•	Seaborn
	•	Joblib


### Explanation:

1. **Problem Statement**: Summarizes the problem you're addressing and key aspects of the solution.
2. **Project Structure**: Describes the organization of files in the project directory.
3. **Model Information**: Provides details on the model used and its features.
4. **Installation**: Step-by-step guide to set up the project.
5. **Usage**: Instructions for running the app and navigating the Streamlit interface.
6. **Model Inputs**: Details the parameters needed for model prediction.
7. **Streamlit UI**: Brief overview of the functionalities in the app.
8. **Data Analysis (EDA)**: Lists the visualizations included in the `analysis.py`.
9. **Technologies Used**: Lists the key libraries and tools used in the project.
10. **License**: States the licensing terms for the project.