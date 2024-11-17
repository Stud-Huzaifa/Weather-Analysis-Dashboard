"""WEATHER ANALYSIS DASHBOARD!!!"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
data = pd.read_csv("Weather Data.csv")

print(data.head())
print(data.info())
print(data.describe())

# Cleaning the Data
data["Date/Time"] = pd.to_datetime(data["Date/Time"])  # Corrected column name from "Data/Time" to "Date/Time"
print(data.isnull().sum())

data.fillna(method="ffill", inplace=True)  # Fill missing values using forward fill
data.dropna(inplace=True)  # Drop remaining missing values (if any)

# Adding date components
data['Year'] = data['Date/Time'].dt.year
data['Month'] = data['Date/Time'].dt.month
data['Day'] = data['Date/Time'].dt.day
data['Hour'] = data['Date/Time'].dt.hour

# Plotting the Temperature Over Time to Observe Trends
plt.figure(figsize=(12, 8))  # Corrected figsize syntax
plt.plot(data["Date/Time"], data["Temp_C"], label='Temperature (°C)', color='blue')
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid()
plt.show()


# Bar Plot: Monthly Average Temperature
monthly_temp_avg = data.groupby("Month")["Temp_C"].mean()
plt.figure(figsize=(10, 6))
monthly_temp_avg.plot(kind="bar", color="skyblue")
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Heatmap: Hourly Temperature by Month
hourly_temp = data.pivot_table(index='Month', columns='Hour', values='Temp_C', aggfunc='mean')
plt.figure(figsize=(12, 8))
sns.heatmap(hourly_temp, cmap='coolwarm', annot=False, cbar_kws={'label': 'Temperature (°C)'})
plt.title("Hourly Average Temperature by Month")
plt.xlabel("Hour")
plt.ylabel("Month")
plt.show()

# Weather Condition Frequency
weather_counts = data["Weather"].value_counts()
plt.figure(figsize=(10, 6))
weather_counts.head(10).plot(kind='bar', color='teal')
plt.title("Top 10 Weather Conditions")
plt.xlabel("Weather Condition")
plt.ylabel("Frequency")
plt.show()

# Seasonal Analysis
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Fall"

data['Season'] = data['Month'].apply(get_season)

plt.figure(figsize=(10, 6))
sns.boxplot(x='Season', y='Temp_C', data=data, palette='Set2')
plt.title("Temperature Distribution by Season")
plt.xlabel("Season")
plt.ylabel("Temperature (°C)")
plt.show()

#STREAM LIT
st.title("Weather Analysis Dashboard")
st.subheader("Temperature Trends Over Time")
st.line_chart(data['Temp_C'])

st.subheader("Monthly Average Temperature")
st.bar_chart(monthly_temp_avg)