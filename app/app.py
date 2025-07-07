import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from src.rfm import generate_rfm
from src.cohort import cohort_analysis, plot_cohort_heatmap
from src.ltv import calculate_ltv

st.set_page_config(layout="wide")
st.title("Customer Segmentation & Retention Dashboard")

# Load data
@st.cache_data
def load_data():
    orders = pd.read_csv("../data/olist_orders_dataset.csv", parse_dates=['order_purchase_timestamp'])
    customers = pd.read_csv("../data/olist_customers_dataset.csv")
    items = pd.read_csv("../data/olist_order_items_dataset.csv")
    payments = pd.read_csv("../data/olist_order_payments_dataset.csv")
    df = orders.merge(customers, on='customer_id') \
             .merge(items, on='order_id') \
             .merge(payments, on='order_id')
    return df

df = load_data()

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Cohort Analysis", "RFM Segmentation", "Lifetime Value"])

if page == "Overview":
    st.subheader("Dataset Overview")
    st.write(df.head())

elif page == "Cohort Analysis":
    st.subheader("Cohort Retention Heatmap")
    cohort_data = cohort_analysis(df)
    fig = plot_cohort_heatmap(cohort_data)
    st.pyplot(fig)

elif page == "RFM Segmentation":
    st.subheader("RFM Segmentation")
    rfm = generate_rfm(df)
    fig = px.scatter(rfm, x='recency', y='monetary', color='cluster', hover_data=['customer_id'])
    st.plotly_chart(fig)

elif page == "Lifetime Value":
    st.subheader("Lifetime Value per Cluster")
    rfm = generate_rfm(df)
    ltv_df = calculate_ltv(df)
    rfm_ltv = rfm.merge(ltv_df, on='customer_id', how='inner')
    fig = px.bar(rfm_ltv.groupby('cluster')['ltv'].mean().reset_index(), x='cluster', y='ltv', title="LTV per RFM Cluster")
    st.plotly_chart(fig)
