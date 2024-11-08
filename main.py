import streamlit as sl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

sl.title('My Basic Streamlit App')

sl.sidebar.header('Settings')
num_rows = sl.sidebar.slider('Number of rows', min_value=5, max_value=100, value=20)
chart_type = sl.sidebar.selectbox('Select chart type', ['Line Chart', 'Bar Chart', 'Area Chart'])

uploaded_file = sl.file_uploader('customers-1000.csv', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    sl.write('Uploaded DataFrame:')
    sl.dataframe(df)
else:
    data = np.random.randn(100, 3)
    columns = ['A', 'B', 'C']
    df = pd.DataFrame(data, columns=columns)

    sl.write('Default DataFrame:')
    sl.dataframe(df)

sl.write(f'{chart_type} of the DataFrame:')
if chart_type == 'Line Chart':
    sl.line_chart(df.head(num_rows))
elif chart_type == 'Bar Chart':
    sl.bar_chart(df.head(num_rows))
elif chart_type == 'Area Chart':
    sl.area_chart(df.head(num_rows))

if sl.checkbox('Show summary statistics'):
    sl.write('Summary statistics:')
    sl.write(df.describe())

if sl.button('Generate Histogram for Column A'):
    sl.write('Histogram for Column A:')
    fig, ax = plt.subplots()
    ax.hist(df['A'], bins=20, color='skyblue')
    sl.pyplot(fig)

selected_column = sl.selectbox('Select a column to view', df.columns)
sl.write(f'Data for column {selected_column}:')
sl.line_chart(df[selected_column])

date = sl.date_input('Select a date')
sl.write('Selected date:', date)

theme = sl.sidebar.radio('Choose a theme', ['Light', 'Dark'])

sl.markdown('Created by Justin Vijar')
