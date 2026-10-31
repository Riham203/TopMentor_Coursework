import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from prophet import Prophet
from mlxtend.frequent_patterns import apriori, association_rules

st.set_page_config(page_title="Restaurant Sales Analytics", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("restaurant_sales.csv")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['revenue'] = df['quantity'] * df['selling_price']
    df['cost'] = df['quantity'] * df['cost_price']
    df['profit'] = df['revenue'] - df['cost']
    df['hour'] = df['timestamp'].dt.hour
    df['day_name'] = df['timestamp'].dt.day_name()
    df['date'] = df['timestamp'].dt.date
    return df

df = load_data()

# Header
st.title("🍽️ Restaurant Sales Analysis & Demand Forecasting")
st.markdown("Operational insights, menu profitability matrix, market basket analysis, and time-series forecasting.")

# Sidebar Filters
st.sidebar.header("Filter Options")
order_type_filter = st.sidebar.multiselect("Order Type", options=df['order_type'].unique(), default=df['order_type'].unique())
category_filter = st.sidebar.multiselect("Category", options=df['category'].unique(), default=df['category'].unique())

filtered_df = df[(df['order_type'].isin(order_type_filter)) & (df['category'].isin(category_filter))]

# KPI Summary
total_revenue = filtered_df['revenue'].sum()
total_profit = filtered_df['profit'].sum()
total_orders = filtered_df['order_id'].nunique()
aov = total_revenue / total_orders if total_orders > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Avg Order Value (AOV)", f"${aov:.2f}")

st.divider()

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Sales & Peak Hours", "🧩 Menu Engineering", "🛒 Basket Analysis", "🔮 Prophet Forecasting"])

# Tab 1: Sales Trends & Peak Hours
with tab1:
    st.subheader("Sales Performance & Peak Operating Hours")
    t1_col1, t1_col2 = st.subplots if False else (st.container(), st.container())
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        hourly_sales = filtered_df.groupby('hour')['revenue'].sum().reset_index()
        fig_hour = px.bar(hourly_sales, x='hour', y='revenue', title="Revenue by Hour of Day",
                          labels={'hour': 'Hour of Day (24h)', 'revenue': 'Revenue ($)'},
                          color='revenue', color_continuous_scale='Blues')
        st.plotly_chart(fig_hour, use_container_width=True)
        
    with col_b:
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        daily_sales = filtered_df.groupby('day_name')['revenue'].sum().reindex(day_order).reset_index()
        fig_day = px.bar(daily_sales, x='day_name', y='revenue', title="Revenue by Day of Week",
                         labels={'day_name': 'Day', 'revenue': 'Revenue ($)'},
                         color='revenue', color_continuous_scale='Greens')
        st.plotly_chart(fig_day, use_container_width=True)

# Tab 2: Menu Engineering Matrix
with tab2:
    st.subheader("Boston Consulting Group (BCG) Menu Matrix")
    st.caption("Categorizes items into Stars, Plowhorses, Puzzles, and Dogs based on volume and contribution margin.")
    
    menu_perf = filtered_df.groupby('item_name').agg(
        volume=('quantity', 'sum'),
        avg_profit=('profit', 'mean'),
        total_revenue=('revenue', 'sum')
    ).reset_index()
    
    median_vol = menu_perf['volume'].median()
    median_profit = menu_perf['avg_profit'].median()
    
    def categorize_menu(row):
        if row['volume'] >= median_vol and row['avg_profit'] >= median_profit:
            return 'Star (Keep & Feature)'
        elif row['volume'] >= median_vol and row['avg_profit'] < median_profit:
            return 'Plowhorse (Increase Price)'
        elif row['volume'] < median_vol and row['avg_profit'] >= median_profit:
            return 'Puzzle (Promote/Rebrand)'
        else:
            return 'Dog (Remove/Revamp)'

    menu_perf['Category_Matrix'] = menu_perf.apply(categorize_menu, axis=1)
    
    fig_matrix = px.scatter(
        menu_perf, x='volume', y='avg_profit', text='item_name', color='Category_Matrix',
        size='total_revenue', title="Menu Engineering Matrix",
        labels={'volume': 'Sales Volume (Quantity Sold)', 'avg_profit': 'Average Profit per Item ($)'}
    )
    fig_matrix.add_hline(y=median_profit, line_dash="dash", line_color="gray")
    fig_matrix.add_vline(x=median_vol, line_dash="dash", line_color="gray")
    fig_matrix.update_traces(textposition='top center')
    
    st.plotly_chart(fig_matrix, use_container_width=True)
    st.dataframe(menu_perf.sort_values(by='total_revenue', ascending=False), use_container_width=True)

# Tab 3: Market Basket Analysis
with tab3:
    st.subheader("Market Basket Analysis (Apriori Rule Mining)")
    st.caption("Identifies items frequently bought together to optimize combo pricing and upselling.")
    
    basket = (filtered_df.groupby(['order_id', 'item_name'])['quantity']
              .sum().unstack().reset_index().fillna(0)
              .set_index('order_id'))
    basket_sets = basket.map(lambda x: 1 if x >= 1 else 0)
    
    frequent_itemsets = apriori(basket_sets, min_support=0.03, use_colnames=True)
    
    if not frequent_itemsets.empty:
        rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
        rules['antecedents'] = rules['antecedents'].apply(lambda x: list(x)[0])
        rules['consequents'] = rules['consequents'].apply(lambda x: list(x)[0])
        
        st.dataframe(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
                     .sort_values(by='lift', ascending=False), use_container_width=True)
    else:
        st.warning("Not enough item co-occurrences to generate strong association rules.")

# Tab 4: Sales Forecasting
with tab4:
    st.subheader("30-Day Daily Sales Demand Forecasting")
    
    daily_ts = filtered_df.groupby('date')['revenue'].sum().reset_index()
    daily_ts.columns = ['ds', 'y']
    
    with st.spinner("Training Prophet Model..."):
        m = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
        m.fit(daily_ts)
        future = m.make_future_dataframe(periods=30)
        forecast = m.predict(future)
        
    fig_forecast = go.Figure()
    fig_forecast.add_trace(go.Scatter(x=daily_ts['ds'], y=daily_ts['y'], mode='lines', name='Actual Revenue'))
    fig_forecast.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecasted Revenue', line=dict(dash='dash', color='orange')))
    fig_forecast.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], mode='lines', opacity=0.2, showlegend=False, line=dict(color='orange')))
    fig_forecast.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], mode='lines', opacity=0.2, fill='tonexty', showlegend=False, line=dict(color='orange')))
    
    fig_forecast.update_layout(title="Daily Sales Forecast (Next 30 Days)", xaxis_title="Date", yaxis_title="Revenue ($)")
    st.plotly_chart(fig_forecast, use_container_width=True)