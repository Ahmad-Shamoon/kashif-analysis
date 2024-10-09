import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Data Loading
@st.cache_data
def load_data():
    # Loading the dataset - adjust the path according to your file location
    df = pd.read_csv('ODI_Match_info.csv')
    return df

df = load_data()

# Replace these placeholders with actual column names from your dataset
column_name_for_filter = 'ActualColumnName'  # Change to a column name from your dataset
date_column = 'ActualDateColumn'  # Change to the date column in your dataset
value_column = 'ActualValueColumn'  # Change to the value column in your dataset
category_column = 'ActualCategoryColumn'  # Change to a category column in your dataset
x_column = 'ActualXColumn'  # Change to the x-axis column for the scatter plot
y_column = 'ActualYColumn'  # Change to the y-axis column for the scatter plot

# Sidebar Filters
st.sidebar.header('Filter Options')
column_filter = st.sidebar.multiselect('Select Columns to Display:', df.columns.tolist())

# Make sure 'column_name_for_filter' is an actual column name in your dataset
if column_name_for_filter in df.columns:
    filter_value = st.sidebar.selectbox('Filter by Column Value', df[column_name_for_filter].unique())
    filtered_data = df[df[column_name_for_filter] == filter_value]
else:
    st.error(f"Column '{column_name_for_filter}' not found in dataset.")
    filtered_data = df

# Applying column filter
if column_filter:
    filtered_data = filtered_data[column_filter]

# Dashboard Layout
st.title("Dashboard Title")
st.markdown("### Overview")
st.dataframe(filtered_data)

# Plotly Chart
st.markdown("### Plotly Chart")
if date_column in filtered_data.columns and value_column in filtered_data.columns:
    fig1 = px.line(filtered_data, x=date_column, y=value_column, title='Line Chart Example')
    st.plotly_chart(fig1)
else:
    st.warning("Please check the date and value column names for the Plotly chart.")

# Seaborn Plot
st.markdown("### Seaborn Chart")
if category_column in filtered_data.columns and value_column in filtered_data.columns:
    plt.figure(figsize=(10, 6))
    sns.barplot(x=category_column, y=value_column, data=filtered_data)
    st.pyplot(plt)
else:
    st.warning("Please check the category and value column names for the Seaborn chart.")

# Matplotlib Plot
st.markdown("### Matplotlib Chart")
if x_column in filtered_data.columns and y_column in filtered_data.columns:
    fig2, ax = plt.subplots()
    ax.scatter(filtered_data[x_column], filtered_data[y_column])
    ax.set_title('Scatter Plot Example')
    st.pyplot(fig2)
else:
    st.warning("Please check the x and y column names for the Matplotlib chart.")


    # (Continue with the rest of your code using the loaded `df`)
