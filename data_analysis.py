import pandas as pd
import numpy as np

# Load the dataset
try:
    df = pd.read_excel('investments_VC.xlsx')
    print("File loaded successfully.")
except FileNotFoundError:
    print("Error: File 'investments_VC.xlsx' not found.")
    exit()

# Quick overview
print(df.head())
print(df.info())
print(df.describe())

# Replace '-' with NaN in funding_total_usd
if 'funding_total_usd' in df.columns:
    df['funding_total_usd'] = df['funding_total_usd'].replace('-', np.nan)
    df['funding_total_usd'] = pd.to_numeric(df['funding_total_usd'], errors='coerce')
    df['funding_total_usd'] = df['funding_total_usd'].fillna(0)
else:
    print("Warning: 'funding_total_usd' column not found.")

# Handle missing values
if 'founded_year' in df.columns:
    df['founded_year'] = df['founded_year'].fillna(df['founded_year'].median())

for col in ['country_code', 'market', 'status']:
    if col in df.columns:
        df[col] = df[col].fillna('Unknown')

# Remove duplicates
print(f"Number of duplicates: {df.duplicated().sum()}")
df = df.drop_duplicates()

# Standardize market names
if 'market' in df.columns:
    df['market'] = df['market'].astype(str).str.strip().str.capitalize()

# Convert date columns
for date_col in ['founded_at', 'first_funding_at', 'last_funding_at']:
    if date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

# Save cleaned data
df.to_csv('cleaned_investments.csv', index=False)
print("✅ Cleaned data saved to 'cleaned_investments.csv'")
