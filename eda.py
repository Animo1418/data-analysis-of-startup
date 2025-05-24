import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('cleaned_investments.csv')

# Strip whitespace from column names right after loading
df.columns = df.columns.str.strip()

print("Columns after stripping spaces:")
print(df.columns.tolist())

# Validate required columns exist
required_columns = [
    'funding_total_usd', 'market', 'status', 'country_code',
    'founded_year', 'funding_rounds', 'seed', 'venture', 'round_A',
    'round_B', 'round_C', 'round_D'
]
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}")

# Ensure numeric columns are properly converted
df['founded_year'] = pd.to_numeric(df['founded_year'], errors='coerce').fillna(0).astype(int)
df['funding_total_usd'] = pd.to_numeric(df['funding_total_usd'], errors='coerce').fillna(0)

# Remove invalid years (0 or less)
df = df[df['founded_year'] > 0]

# Insight 1: Top markets by total funding
top_markets = df.groupby('market')['funding_total_usd'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_markets.values, y=top_markets.index)
plt.title('Top 10 Markets by Total Funding (USD)')
plt.xlabel('Total Funding (USD)')
plt.ylabel('Market')
plt.savefig('top_markets.png')
plt.close()
print("Insight 1: Top markets by funding saved as 'top_markets.png'")

# Insight 2: Funding distribution by startup status
plt.figure(figsize=(8, 6))
sns.boxplot(x='status', y='funding_total_usd', data=df)
plt.title('Funding Distribution by Startup Status')
plt.xlabel('Status')
plt.ylabel('Funding (USD)')
plt.yscale('log')  # Log scale for better visualization
plt.savefig('funding_by_status.png')
plt.close()
print("Insight 2: Funding by status saved as 'funding_by_status.png'")

# Insight 3: Top countries by number of startups
top_countries = df['country_code'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 Countries by Number of Startups')
plt.xlabel('Number of Startups')
plt.ylabel('Country')
plt.savefig('top_countries.png')
plt.close()
print("Insight 3: Top countries saved as 'top_countries.png'")

# Insight 4: Total funding by founded year
funding_by_year = df.groupby('founded_year')['funding_total_usd'].sum()
print(funding_by_year.head())  # Debug print

plt.figure(figsize=(12, 6))
funding_by_year.plot(kind='line')
plt.title('Total Funding by Founded Year')
plt.xlabel('Founded Year')
plt.ylabel('Total Funding (USD)')
plt.savefig('funding_trends.png')
plt.close()
print("Insight 4: Funding trends saved as 'funding_trends.png'")

# Insight 5: Funding rounds vs total funding
plt.figure(figsize=(8, 6))
sns.scatterplot(x='funding_rounds', y='funding_total_usd', data=df)
plt.title('Funding Rounds vs. Total Funding')
plt.xlabel('Number of Funding Rounds')
plt.ylabel('Total Funding (USD)')
plt.yscale('log')
plt.savefig('funding_rounds.png')
plt.close()
print("Insight 5: Funding rounds vs. funding saved as 'funding_rounds.png'")

# Insight 6: Market share - top 5 markets by startup count
top_markets_count = df['market'].value_counts().head(5)
plt.figure(figsize=(8, 8))
plt.pie(top_markets_count, labels=top_markets_count.index, autopct='%1.1f%%')
plt.title('Top 5 Markets by Number of Startups')
plt.savefig('market_share.png')
plt.close()
print("Insight 6: Market share saved as 'market_share.png'")

# Insight 7: Funding by funding type
funding_types = ['seed', 'venture', 'round_A', 'round_B', 'round_C', 'round_D']
funding_sums = df[funding_types].sum()
plt.figure(figsize=(10, 6))
sns.barplot(x=funding_sums.index, y=funding_sums.values)
plt.title('Total Funding by Funding Type')
plt.xlabel('Funding Type')
plt.ylabel('Total Funding (USD)')
plt.savefig('funding_types.png')
plt.close()
print("Insight 7: Funding types saved as 'funding_types.png'")

# Insight 8: Acquisition rate by market
if 'acquired' in df['status'].unique():
    market_status = df.groupby(['market', 'status']).size().unstack(fill_value=0)
    market_status['acquired_rate'] = market_status.get('acquired', 0) / market_status.sum(axis=1)
    top_acquired = market_status['acquired_rate'].sort_values(ascending=False).head(5)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_acquired.values, y=top_acquired.index)
    plt.title('Top 5 Markets by Acquisition Rate')
    plt.xlabel('Acquisition Rate')
    plt.ylabel('Market')
    plt.savefig('acquisition_rate.png')
    plt.close()
    print("Insight 8: Acquisition rate saved as 'acquisition_rate.png'")
else:
    print("Warning: 'acquired' status not found in 'status' column, skipping acquisition rate insight.")

# Write summary of insights to file
with open('insights.txt', 'w') as f:
    f.write("Insight 1: Top markets by funding (see top_markets.png)\n")
    f.write("Insight 2: Funding distribution by status (see funding_by_status.png)\n")
    f.write("Insight 3: Top countries by startup count (see top_countries.png)\n")
    f.write("Insight 4: Funding trends over time (see funding_trends.png)\n")
    f.write("Insight 5: Funding rounds vs. funding (see funding_rounds.png)\n")
    f.write("Insight 6: Market share by startup count (see market_share.png)\n")
    f.write("Insight 7: Funding by type (see funding_types.png)\n")
    f.write("Insight 8: Top markets by acquisition rate (see acquisition_rate.png)\n")

print("All insights generated and saved.")
