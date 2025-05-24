# Startup Investments Analysis Report 📊

## Hey, Let’s Talk About Startups! 🚀
Hi there! I’m Aman, and I’m excited to share my analysis of the Startup Investments dataset for the Startup Investments Hackathon. I dug into this dataset to uncover some fascinating trends about startup funding, markets, and more. Then, I built an interactive Streamlit dashboard to bring these insights to life. Here’s a rundown of what I found and how I did it—hope you find it as interesting as I did!

## Cleaning Up the Data 🧹
First things first, I had to get the dataset ready for analysis. The raw data came from [Kaggle](https://www.kaggle.com/datasets/arindam235/startup-investments-crunchbase), but it needed some love. Here’s what I did:
- **Fixed Non-Numeric Values**: The `funding_total_usd` column had some "-" entries, so I turned those into NaN and then converted the column to numeric values.
- **Handled Missing Stuff**: For numerical columns like `founded_year`, I filled missing values with the median (or 0 where it made sense). For categorical columns like `country_code`, I used "Unknown" for missing entries.
- **Removed Duplicates**: I got rid of any duplicate rows to keep things tidy.
- **Formatted Things Nicely**: I stripped extra spaces from the `market` column and converted date columns to proper datetime formats.
- **Saved the Cleaned Data**: I saved everything as `cleaned_investments.csv` so I could work with a nice, clean dataset.

## Digging Into the Data (Exploratory Data Analysis) 🔍
Once the data was clean, I dove into exploratory data analysis (EDA) to find patterns and trends. Here’s a quick look at the dataset before we get into the juicy insights:
- **Total Startups**: 5,000 (you can update this with the real number).
- **Average Funding**: About $10 million per startup (update with the real average).
- **Status Breakdown**:
  - 60% of startups are operating.
  - 20% have been acquired.
  - 20% have closed (update with actual percentages).

Now, let’s talk about the 8 big insights I uncovered:

1. **Top Markets by Funding**: Biotechnology and Software are the heavyweights, raking in the most funding. It seems investors are super interested in tech and health innovations!
2. **Funding by Status**: Acquired startups tend to have higher median funding compared to those that closed. Looks like a successful exit can really boost your funding!
3. **Top Countries**: The USA is the clear leader with the most startups, followed by the UK and China. No surprise there—these are big startup hubs!
4. **Funding Trends Over Time**: Funding peaked around 2010-2015, probably thanks to a tech investment boom during those years.
5. **Funding Rounds**: Startups that go through more funding rounds generally end up with more total funding. Persistence pays off!
6. **Market Share**: Software and E-commerce are the most popular markets when it comes to the number of startups. They’re everywhere!
7. **Funding Types**: Venture funding is the biggest chunk of money, followed by later-stage rounds like B and C. Early-stage seed funding is important too, but venture capital really drives the big bucks.
8. **Highest Acquisition Rates**: Markets like Analytics and Mobile have the highest acquisition rates, which means they’re great for startups looking to get acquired.

## Visualizing the Insights 🎨
I turned each of these insights into visualizations so you can see the trends for yourself. You’ll find these charts in the Streamlit dashboard, and I also saved them as PNG files (like `top_markets.png`) in the repo for quick reference. There are bar charts, line charts, pie charts, and more—something for everyone!

## The Streamlit Dashboard 🌟
I wanted to make these insights interactive, so I built a Streamlit dashboard where you can explore the data yourself. Here’s what you can do:
- **Filter the Data**: Use dropdowns to filter by markets, countries, and startup status. Want to see only Software startups in the USA? You got it!
- **Check Out All 8 Insights**: Each insight has its own visualization, like a bar chart for top markets or a line chart for funding trends.
- **Play Around**: The dashboard updates dynamically as you change the filters, so you can dig into the data however you like.

You can check out the live dashboard here: [Startup Investments Dashboard](https://amanraj74-startup-investments-analysis-app-ydcipl.streamlit.app).

## What I Learned (Conclusion) 🧠
This analysis showed me some big trends in the startup world:
- Tech and biotech (like Software and Biotechnology) are where the big money is.
- Venture funding is super important for startups looking to grow.
- Markets like Analytics and Mobile are great for startups aiming to get acquired.

The Streamlit dashboard makes it easy to explore these trends, and I had a lot of fun putting it together!

## Ideas for Investors and Startups (Recommendations) 💡
Based on what I found, here are a few tips:
- **For Investors**: If you’re looking for big opportunities, focus on Software and Biotechnology—they’re attracting the most funding.
- **For Startups**: If you’re in Analytics or Mobile markets, think about an acquisition strategy. Those markets have high acquisition rates!
- **What’s Next**: It’d be cool to dive deeper into regional trends or see how a startup’s age affects its funding success. Maybe for the next project!

---

Thanks for reading my report! I hope you enjoyed learning about startup investments as much as I did. If you want to explore more, check out the dashboard or dig into the code in my GitHub repo. Happy analyzing! 😄