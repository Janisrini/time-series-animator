import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("time_series_data.csv")

# Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort by Date
df = df.sort_values('Date')

# Quick static line plots
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Temperature'], label='Temperature (°C)')
plt.plot(df['Date'], df['Rainfall'], label='Rainfall (mm)')
plt.plot(df['Date'], df['Humidity'], label='Humidity (%)')
plt.xlabel("Date")
plt.ylabel("Values")
plt.title("Time Series Overview")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()