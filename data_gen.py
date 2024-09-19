import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker to generate synthetic data
fake = Faker()

# Set seed for reproducibility
np.random.seed(42)

# Function to generate random weather data
def generate_weather_data(season):
    if season == 'summer':
        temperature = np.random.uniform(30, 45)
        humidity = np.random.uniform(20, 60)
    elif season == 'rainy':
        temperature = np.random.uniform(20, 35)
        humidity = np.random.uniform(60, 100)
    elif season == 'autumn':
        temperature = np.random.uniform(15, 30)
        humidity = np.random.uniform(30, 70)
    else:  # winter
        temperature = np.random.uniform(5, 20)
        humidity = np.random.uniform(40, 80)
    
    wind_speed = np.random.uniform(0, 15)
    rainfall = np.random.uniform(0, 10)
    return temperature, humidity, wind_speed, rainfall

# Function to simulate load demand based on time, season, and other factors
def simulate_load(hour, day_of_week, temperature, humidity, is_holiday, season):
    base_load = 2000
    
    if season == 'summer':
        base_load = 6000
    elif season == 'rainy':
        base_load = 4000
    elif season == 'autumn':
        base_load = 3500
    
    if 15 <= hour <= 17 or 23 <= hour <= 1:
        base_load += 1000
    if day_of_week >= 5:
        base_load += 500
    if is_holiday:
        base_load -= 300
    
    load = base_load + (temperature - 25) * 50 + (humidity - 50) * 10
    return max(2000, min(load, 9000))

# Generate balanced dataset
seasons = ['summer', 'rainy', 'autumn', 'winter']
rows_per_season = 2500 // len(seasons)

data = []
for season in seasons:
    for _ in range(rows_per_season):
        hour = np.random.randint(0, 24)
        day_of_week = np.random.randint(0, 7)
        is_holiday = random.random() < 0.1
        
        temperature, humidity, wind_speed, rainfall = generate_weather_data(season)
        
        load = simulate_load(hour, day_of_week, temperature, humidity, is_holiday, season)
        energy_consumption = np.random.uniform(100, 500)
        shedding = np.random.uniform(0, 50)
        transmission_losses = np.random.uniform(1, 5)
        system_availability = np.random.uniform(95, 100)
        
        data.append({
            'hour_of_day': hour,
            'day_of_week': day_of_week,
            'is_holiday': is_holiday,
            'season': season,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'rainfall': rainfall,
            'Peak_Demand_met_(MW)': load,
            'Load_Growth_(%)': np.random.uniform(-10, 50),
            'Energy_Consumption_(MUs)': energy_consumption,
            'Shedding_(MUs)': shedding,
            'Shedding_as_of_Energy_Consumption': (shedding / energy_consumption) * 100,
            'Transmission_Losses_(%)': transmission_losses,
            'System_Availability_(%)': system_availability,
            'electricity_load_MW': load
        })

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Save the dataset as a CSV file
df.to_csv('balanced_electricity_demand.csv', index=False)

print("Balanced dataset generated and saved as 'balanced_electricity_demand.csv'")