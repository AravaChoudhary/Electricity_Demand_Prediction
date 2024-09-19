import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def eda(dataframe):
    st.title("General Information About the Data")
    st.write("# Data Overview")
    st.write(dataframe.head())

    st.write("### Descriptive Statistics")
    st.write(dataframe.describe())

    # Bar chart for hour_of_day vs electricity load
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='hour_of_day', y='electricity_load_MW', data=dataframe, estimator=sum, errorbar=None, ax=ax)
    ax.set_title('Electricity Load by Hour of Day')
    ax.set_xlabel('Hour of Day')
    ax.set_ylabel('Total Electricity Load (MW)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    # Line plot for hour_of_day vs electricity load
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='hour_of_day', y='electricity_load_MW', data=dataframe, estimator='sum', errorbar=None, ax=ax)
    ax.set_title('Electricity Load by Hour of Day')
    ax.set_xlabel('Hour of Day')
    ax.set_ylabel('Total Electricity Load (MW)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    # Line plot for is_holiday vs electricity load
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.lineplot(x='is_holiday', y='electricity_load_MW', data=dataframe, estimator='sum', errorbar=None, ax=ax)
    ax.set_title('Electricity Load on Holidays vs Non-Holidays')
    ax.set_xlabel('Holiday (1 = Yes, 0 = No)')
    ax.set_ylabel('Total Electricity Load (MW)')
    st.pyplot(fig)

    # Boxplot for electricity load across different seasons
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='season', y='electricity_load_MW', data=dataframe, ax=ax)
    ax.set_title('Electricity Load Distribution Across Seasons')
    ax.set_xlabel('Season')
    ax.set_ylabel('Electricity Load (MW)')
    st.pyplot(fig)

    # Boxplot for electricity load during holidays vs non-holidays
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x='is_holiday', y='electricity_load_MW', data=dataframe, ax=ax)
    ax.set_title('Electricity Load During Holidays vs Non-Holidays')
    ax.set_xlabel('Holiday (1 = Yes, 0 = No)')
    ax.set_ylabel('Electricity Load (MW)')
    st.pyplot(fig)

    # Pie chart for hour_of_day: Proportion of electricity load by hour of the day
    hourly_data = dataframe.groupby('hour_of_day')['electricity_load_MW'].sum()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(hourly_data, labels=hourly_data.index, autopct='%1.1f%%', startangle=90)
    ax.set_title('Proportion of Electricity Load by Hour of Day')
    st.pyplot(fig)

    # Pie chart for is_holiday: Proportion of electricity load during holidays vs non-holidays
    holiday_data = dataframe.groupby('is_holiday')['electricity_load_MW'].sum()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(holiday_data, labels=['Non-Holiday', 'Holiday'], autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen'])
    ax.set_title('Proportion of Electricity Load on Holidays vs Non-Holidays')
    st.pyplot(fig)