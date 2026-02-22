from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# ------------------------
# Database connection
# ------------------------
DB_USER = "postgres"
DB_PASS = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "crypto_pipeline"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Read data from PostgreSQL
df = pd.read_sql("SELECT * FROM crypto_data", engine)

# ------------------------
# Streamlit page config
# ------------------------
st.set_page_config(
    page_title="Crypto Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Auto-refresh every 60 seconds
st_autorefresh(interval=60 * 1000)

# ------------------------
# Sidebar filters
# ------------------------
st.sidebar.header("Filters")
coin_list = df['id'].unique()
selected_coin = st.sidebar.selectbox("Select Coin", ["All"] + list(coin_list))

# Filter dataframe
if selected_coin != "All":
    df_filtered = df[df['id'] == selected_coin]
else:
    df_filtered = df.copy()

# ------------------------
# Metrics
# ------------------------
st.title("🚀 Crypto Dashboard - PostgreSQL Edition")
if selected_coin != "All":
    latest = df_filtered.sort_values('extracted_at').iloc[-1]
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Price", f"${latest['current_price']:.2f}")
    col2.metric("Market Cap", f"${latest['market_cap']:,}")
    col3.metric("24h Change", f"{latest['price_change_percentage_24h']:.2f}%")

# ------------------------
# Data Table
# ------------------------
st.subheader("Data Table")
st.dataframe(df_filtered[['symbol','name','current_price','market_cap','total_volume','price_change_percentage_24h','extracted_at']])

# ------------------------
# Line chart: Price over time
# ------------------------
if selected_coin != "All":
    fig_price = px.line(df_filtered, x='extracted_at', y='current_price',
                        title=f"{selected_coin.capitalize()} Price Over Time",
                        labels={'current_price':'Price ($)', 'extracted_at':'Time'})
    st.plotly_chart(fig_price, use_container_width=True)

# ------------------------
# Top 10 Market Cap
# ------------------------
top10 = df.groupby('id').agg({'market_cap':'max'}).sort_values('market_cap', ascending=False).head(10)
top10 = top10.merge(df[['id','name']], on='id', how='left').drop_duplicates('id')

fig_marketcap = px.bar(top10, x='id', y='market_cap', text='market_cap',
                       title="Top 10 Coins by Market Cap",
                       labels={'id':'Coin','market_cap':'Market Cap ($)'},
                       color='market_cap', color_continuous_scale='Viridis')
st.plotly_chart(fig_marketcap, use_container_width=True)

# ------------------------
# Top 10 24h Price Change
# ------------------------
latest_df = df.sort_values('extracted_at').groupby('id').tail(1)
top10_change = latest_df.sort_values('price_change_percentage_24h', ascending=False).head(10)

fig_change = px.bar(top10_change, x='id', y='price_change_percentage_24h', text='price_change_percentage_24h',
                    title="Top 10 Coins - 24h Price Change (%)",
                    labels={'id':'Coin','price_change_percentage_24h':'24h Change (%)'},
                    color='price_change_percentage_24h',
                    color_continuous_scale=['red','green'])
st.plotly_chart(fig_change, use_container_width=True)

# ------------------------
# Pie chart: Market Cap Distribution
# ------------------------
fig_pie = px.pie(top10, values='market_cap', names='id', title="Market Cap Distribution - Top 10")
st.plotly_chart(fig_pie, use_container_width=True)