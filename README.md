# Electricity Demand Prediction for Delhi

This project aims to develop an AI-based model for predicting electricity demand, including peak demand projection, for the Delhi power system. The model accounts for various factors such as seasonal variations, weather conditions, and public holidays to provide accurate forecasts.

## Table of Contents
- [Problem Statement](#problem-statement)
- [Project Structure](#project-structure)
- [Model Information](#model-information)
- [Installation](#installation)
- [Usage](#usage)
- [Model Inputs](#model-inputs)
- [Streamlit UI](#streamlit-ui)
- [Data Analysis (EDA)](#data-analysis-eda)
- [Technologies Used](#technologies-used)
- [License](#license)

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