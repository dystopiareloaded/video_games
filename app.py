import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from dbhelper import DB

# Load the SQLite database file
db = DB("video_game_sales.db")

st.title("🎮 Video Game Sales Dashboard")

# Sidebar Filters
st.sidebar.title("Filters")
years = db.fetch_years()
selected_year = st.sidebar.selectbox("Select Year", years, index=len(years)-1)

# Genre Sales
st.subheader(f"Global Sales by Genre in {selected_year}")
genres, genre_sales = db.genre_sales_by_year(selected_year)
if genres and genre_sales:
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=genre_sales, y=genres, palette="viridis", ax=ax1)
    ax1.set_xlabel("Global Sales (Millions)")
    ax1.set_ylabel("Genre")
    st.pyplot(fig1)
else:
    st.warning("No data found for genres.")

# Publisher Sales
st.subheader(f"Top 20 Publishers by Global Sales in {selected_year}")
publishers, publisher_sales = db.publisher_sales_by_year(selected_year)
if publishers and publisher_sales:
    fig2, ax2 = plt.subplots(figsize=(10, 8))
    sns.barplot(x=publisher_sales, y=publishers, palette="magma", ax=ax2)
    ax2.set_xlabel("Global Sales (Millions)")
    ax2.set_ylabel("Publisher")
    st.pyplot(fig2)
else:
    st.warning("No data found for publishers.")

# Platform Sales
st.subheader(f"Global Sales by Platform in {selected_year}")
platforms, platform_sales = db.platform_sales_by_year(selected_year)
if platforms and platform_sales:
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=platform_sales, y=platforms, palette="coolwarm", ax=ax3)
    ax3.set_xlabel("Global Sales (Millions)")
    ax3.set_ylabel("Platform")
    st.pyplot(fig3)
else:
    st.warning("No data found for platforms.")

# Sales Over Time
st.subheader("Global Sales Over Years")
years, total_sales = db.sales_over_time()
if years and total_sales:
    fig4, ax4 = plt.subplots(figsize=(12, 5))
    sns.lineplot(x=years, y=total_sales, marker="o", color="green", ax=ax4)
    ax4.set_xlabel("Year")
    ax4.set_ylabel("Global Sales (Millions)")
    st.pyplot(fig4)
else:
    st.warning("No data found for sales over time.")
