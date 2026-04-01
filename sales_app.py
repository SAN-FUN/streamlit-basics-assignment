import streamlit as st
import pandas as pd

# Title and description
st.title("Sales Dashboard")
st.subheader("Interactive sales summary by category")

# Create hardcoded dataset
data = {
    "Product": ["Laptop", "Shirt", "Phone", "Kurtis", "AC","Kidswear"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics","Clothing"],
    "Sales": [1200, 200, 800, 900, 600,900]
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.title("Filter Options")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter data
filtered_df = df[df["Category"] == category]

# Display filtered data
st.dataframe(filtered_df)

# Line chart
st.line_chart(filtered_df["Sales"])