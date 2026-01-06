import pandas as pd

# Load dataset
df = pd.read_csv("time_series_data.csv")

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Drop missing or duplicate values
df = df.dropna()
df = df.drop_duplicates()

# Reset index
df = df.sort_values("Date").reset_index(drop=True)

# Display cleaned data
print("Cleaned Data Preview:")
print(df.head())

# Save cleaned data
df.to_csv("cleaned_time_series.csv", index=False)