import joblib
import pandas as pd
import streamlit as st
from analysis import eda

model = joblib.load('model_main.sav')
col_tran = joblib.load('column_transformer_m.sav')

# Layout
st.set_page_config(
    page_title="Electricity Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Data Pull and Functions
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Navigator")
option = st.sidebar.radio("Select a section", ["Model Prediction", "Data Analysis"])

st.sidebar.title('Electricity Demand Projection')

st.sidebar.header('Instructions')
st.sidebar.write('Welcome to the Electricity Demand Projection tool for Delhi.')
st.sidebar.write('Use the options below to set parameters for demand forecasting and analysis.')

st.sidebar.header('Select Parameters')
st.sidebar.write('1. **Hour of Day**: Choose the hour for which you want to project the electricity demand.')
st.sidebar.write('2. **Day of Week**: Select the day of the week to account for variations in demand.')
st.sidebar.write('3. **Holiday**: Check this if the selected day is a public holiday.')
st.sidebar.write('4. **Season**: Choose the season to account for seasonal variations in demand.')
st.sidebar.write('5. **Weather Conditions**: Input the temperature, humidity, wind speed, and rainfall for accurate predictions.')

st.sidebar.header('Projection Settings')
st.sidebar.write('1. **Peak Demand**: View the peak demand met in MW.')
st.sidebar.write('2. **Load Growth**: Adjust the load growth percentage for dynamic projections.')
st.sidebar.write('3. **Energy Consumption**: Enter energy consumption in MUs.')
st.sidebar.write('4. **Shedding**: Input shedding in MUs and view shedding as a percentage of energy consumption.')
st.sidebar.write('5. **Transmission Losses**: Set transmission losses as a percentage.')
st.sidebar.write('6. **System Availability**: Specify system availability percentage.')

st.sidebar.header('Additional Information')
st.sidebar.write('Use the provided fields to fine-tune your projections and analyze the electricity demand for various conditions in Delhi.')
st.sidebar.write('Click the "Run Projection" button to generate the forecast based on the selected parameters.')

if option == "Model Prediction":
    st.title("Electricity Demand Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        hour_of_day = st.number_input('Hour of Day', min_value=0, max_value=23, step=1, value=15)
        day_of_week = st.number_input('Day of Week', min_value=0, max_value=6, step=1, value=5)
        is_holiday = st.selectbox("Is Holiday?", ['Yes', 'No'], index=1)
        season = st.selectbox("Season", ['Spring', 'Summer', 'Autumn', 'Winter'], index=1)
        temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, step=0.1, value=44.71)

    with col2:
        humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1, value=56.13)
        wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=100.0, step=0.1, value=9.70)
        rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=200.0, step=0.1, value=6.93)
        peak_demand_met = st.number_input('Peak Demand Met (MW)', min_value=0.0, step=0.1, value=8546.78)
        load_growth = st.number_input('Load Growth (%)', min_value=0.0, step=0.1, value=49.96)

    with col3:
        energy_consumption = st.number_input('Energy Consumption (MUs)', min_value=0.0, step=0.1, value=120.64)
        shedding = st.number_input('Shedding (MUs)', min_value=0.0, step=0.1, value=33.50)
        shedding_percentage = st.number_input('Shedding as % of Energy Consumption', min_value=0.0, step=0.1, value=27.77)
        transmission_losses = st.number_input('Transmission Losses (%)', min_value=0.0, step=0.1, value=1.18)
        system_availability = st.number_input('System Availability (%)', min_value=0.0, max_value=100.0, step=0.1, value=97.94)
    input_data = pd.DataFrame({
        'hour_of_day': [hour_of_day],
        'day_of_week': [day_of_week],
        'temperature': [temperature],
        'humidity': [humidity],
        'wind_speed': [wind_speed],
        'rainfall': [rainfall],
        'Peak_Demand_met_(MW)': [peak_demand_met],
        'Load_Growth_(%)': [load_growth],
        'Energy_Consumption_(MUs)': [energy_consumption],
        'Shedding_(MUs)': [shedding],
        'Shedding_as_of_Energy_Consumption': [shedding_percentage],
        'Transmission_Losses_(%)': [transmission_losses],
        'System_Availability_(%)': [system_availability],
        'is_holiday': [1 if is_holiday == 'Yes' else 0],
        'season': [season]
    })

    input_data_transformed = col_tran.transform(input_data)

    if st.button("Predict"):
        prediction = model.predict(input_data_transformed)
        st.write("Predicted Electricity Demand:", prediction[0])

elif option == "Data Analysis":
    st.title("Data Analysis (EDA)")
    dataframe = pd.read_csv('data.csv')
    eda(dataframe)