import streamlit as st

from src.analysis import load_sales_data, summarize_sales


st.set_page_config(
    page_title="Sales Data Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Sales Data Dashboard")
st.write("Interactive analysis of sample sales data")

sales = load_sales_data()
st.sidebar.header("Filters")

regions = sorted(sales["region"].unique())

selected_regions = st.sidebar.multiselect(
    "Select regions",
    options=regions,
    default=regions,
)

filtered_sales = sales[
    sales["region"].isin(selected_regions)
]
summary = summarize_sales(filtered_sales)


# KPI metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Revenue",
    f"${summary['total_revenue']:,.2f}",
)

col2.metric(
    "Total Transactions",
    len(filtered_sales),
)

col3.metric(
    "Average Transaction Value",
    f"${filtered_sales['revenue'].mean():,.2f}",
)


st.divider()


# Monthly revenue
st.subheader("Monthly Revenue")

monthly_revenue = summary["monthly_revenue"]

st.line_chart(monthly_revenue)


# Revenue by category
st.subheader("Revenue by Category")

st.bar_chart(summary["revenue_by_category"])


# Revenue by region
st.subheader("Revenue by Region")

st.bar_chart(summary["revenue_by_region"])


st.divider()

st.subheader("Sales Data")

st.dataframe(sales)