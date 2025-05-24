import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Page config
st.set_page_config(page_title="🚀 Startup Investment Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_investments.csv')
    df.columns = df.columns.str.strip()
    df['founded_year'] = pd.to_numeric(df['founded_year'], errors='coerce').fillna(0).astype(int)
    df['funding_total_usd'] = pd.to_numeric(df['funding_total_usd'], errors='coerce').fillna(0)
    return df

df = load_data()

# Sidebar filters
with st.sidebar:
    st.header("🎯 Filter Data")
    selected_status = st.multiselect("Status", sorted(df['status'].dropna().unique()), default=list(df['status'].dropna().unique()))
    selected_market = st.multiselect("Market", sorted(df['market'].dropna().unique()), default=sorted(df['market'].dropna().unique())[:5])
    selected_country = st.multiselect("Country", sorted(df['country_code'].dropna().unique()), default=['USA', 'GBR'])
    founded_range = st.slider("Founded Year", int(df['founded_year'].min()), int(df['founded_year'].max()), (2005, 2015))
    min_funding = st.slider("Minimum Funding ($)", 0, int(df['funding_total_usd'].max()), 1_000_000, step=500_000)

# Filter dataset
filtered_df = df[
    df['status'].isin(selected_status) &
    df['market'].isin(selected_market) &
    df['country_code'].isin(selected_country) &
    df['founded_year'].between(*founded_range) &
    (df['funding_total_usd'] >= min_funding)
]

if filtered_df.empty:
    st.warning("No data available for selected filters.")
    st.stop()

# Data Overview (clickable URLs, 20 rows max)
st.markdown("## 📊 Filtered Startup Overview")
st.write(f"Total Startups: {filtered_df.shape[0]}")

if 'homepage_url' in filtered_df.columns:
    display_df = filtered_df[['name', 'market', 'country_code', 'status', 'founded_year', 'funding_total_usd', 'homepage_url']].copy()
    display_df['homepage_url'] = display_df['homepage_url'].apply(lambda x: f"[Website]({x})" if pd.notna(x) and x.startswith('http') else '')
    st.markdown(display_df.head(20).to_markdown(index=False), unsafe_allow_html=True)
else:
    st.write(filtered_df.head(20))

# Add vertical spacing helper function
def add_spacing(lines=1):
    for _ in range(lines):
        st.write("")

# Set seaborn style and palette
sns.set(style="whitegrid")
palette = sns.color_palette("crest", as_cmap=False)

# Layout: 2 columns per row for neatness
col1, col2 = st.columns(2)

# 1. Bar Chart: Top Markets by Total Funding
with col1:
    st.markdown("### 💡 Top Markets by Total Funding")
    top_markets = filtered_df.groupby('market')['funding_total_usd'].sum().sort_values(ascending=False).head(10)
    fig1, ax1 = plt.subplots(figsize=(8,5))
    sns.barplot(x=top_markets.values, y=top_markets.index, palette='Blues_r', ax=ax1)
    ax1.set_xlabel("Total Funding (USD)")
    ax1.set_ylabel("Market")
    ax1.ticklabel_format(style='plain', axis='x')
    st.pyplot(fig1)

add_spacing(2)  # Add space after plot

# 2. Line Chart: Total Funding Over Years
with col2:
    st.markdown("### 📈 Total Funding Over Founded Years")
    yearly_funding = filtered_df.groupby('founded_year')['funding_total_usd'].sum()
    fig2 = px.line(yearly_funding, x=yearly_funding.index, y=yearly_funding.values,
                   labels={'x': 'Year', 'y': 'Total Funding (USD)'},
                   title="Funding Over Years",
                   template='plotly_white',
                   color_discrete_sequence=['#1f77b4'])
    fig2.update_layout(margin=dict(l=40, r=40, t=40, b=40))
    st.plotly_chart(fig2, use_container_width=True)

add_spacing(3)

# 3. Pie Chart: Startup Count by Country
with col1:
    st.markdown("### 🌍 Startup Count by Country")
    country_counts = filtered_df['country_code'].value_counts().head(7)
    fig3, ax3 = plt.subplots(figsize=(7,7))
    colors = sns.color_palette("pastel")[0:7]
    ax3.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'w'})
    ax3.set_title("Top Countries by Startup Count")
    st.pyplot(fig3)

add_spacing(3)

# 4. Box Plot: Funding Distribution by Status
with col2:
    st.markdown("### 📊 Funding Distribution by Status")
    fig4, ax4 = plt.subplots(figsize=(8,5))
    sns.boxplot(x='status', y='funding_total_usd', data=filtered_df, palette='crest', ax=ax4)
    ax4.set_yscale('log')
    ax4.set_title("Funding Distribution (Log Scale)")
    ax4.set_xlabel("Status")
    ax4.set_ylabel("Funding (USD)")
    st.pyplot(fig4)

add_spacing(3)

# 5. Scatter Plot: Funding Rounds vs Total Funding
with col1:
    st.markdown("### 🔄 Funding Rounds vs Total Funding")
    if 'funding_rounds' in filtered_df.columns:
        fig5 = px.scatter(filtered_df, x='funding_rounds', y='funding_total_usd', color='market',
                          log_y=True, size='funding_total_usd', hover_data=['name', 'status'],
                          title="Funding Rounds vs Total Funding",
                          template='plotly_white',
                          color_discrete_sequence=px.colors.sequential.Teal)
        fig5.update_layout(margin=dict(l=40, r=40, t=40, b=40))
        st.plotly_chart(fig5, use_container_width=True)
    else:
        st.info("Funding rounds data not available for scatter plot.")

add_spacing(3)

# 6. Horizontal Bar: Average Funding by Market
with col2:
    st.markdown("### 📉 Average Funding per Market")
    avg_funding = filtered_df.groupby('market')['funding_total_usd'].mean().sort_values(ascending=False).head(7)
    fig6, ax6 = plt.subplots(figsize=(8,5))
    sns.barplot(x=avg_funding.values, y=avg_funding.index, palette='rocket', ax=ax6)
    ax6.set_xlabel("Average Funding (USD)")
    ax6.set_ylabel("Market")
    ax6.ticklabel_format(style='plain', axis='x')
    st.pyplot(fig6)

add_spacing(3)

# 7. Bar Chart: Acquisition Rate by Market (if applicable)
with col1:
    if 'acquired' in filtered_df['status'].values:
        st.markdown("### 📈 Acquisition Rate by Market")
        status_data = filtered_df.groupby(['market', 'status']).size().unstack(fill_value=0)
        status_data['acq_rate'] = status_data.get('acquired', 0) / status_data.sum(axis=1)
        top_acq = status_data['acq_rate'].sort_values(ascending=False).head(7)
        fig7, ax7 = plt.subplots(figsize=(8,5))
        sns.barplot(x=top_acq.values, y=top_acq.index, palette='mako', ax=ax7)
        ax7.set_xlabel("Acquisition Rate")
        ax7.set_ylabel("Market")
        ax7.set_xlim(0,1)
        st.pyplot(fig7)
    else:
        st.info("No acquisitions found in the filtered data.")
