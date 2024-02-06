# ----IMPORTING PACKAGES----
import pandas as pd
import streamlit as st
import datetime as dt
import pandas_datareader as pdr

# --- PAGE SETTINGS AND STYLING ---
page_title = "Stock Analyser - Time Series"
page_icon = ":chart_with_upwards_trend:"
icon = ':chart_with_downwards_trend:'

st.set_page_config(page_title, page_icon)

# ----READING DATA----
def reading_data(stock, sd, ed):
  data = pdr.DataReader(stock, 'stooq', sd, ed)
  st.dataframe(data)

  col3, col4 = st.columns(2)

  col3.subheader('Head')
  col3.dataframe(data.head())
  col4.subheader('Tail')
  col4.dataframe(data.tail())

  return data

# ----PLOTTING DATA----
def basic_plots(data, tag):
  st.line_chart(data[tag])

def limit_plots(data, tag, xs, xe, ys, ye):
  st.pyplot(data[tag].plot(xlim=[xs, xe],ylim=[ys, ye], color='red',figsize=(10,5)).figure)
  
# ----ROLLING----
def rolling(data, tag, window, min_period):
  rolled = data[tag].rolling(window, min_period).mean()
  if window:
    col1, col2 = st.columns(2)
    col1.dataframe(rolled.head(15))
    col2.line_chart(rolled, use_container_width=False)

    data['Open Rolling'] = rolled
    st.dataframe(data.head())
    st.pyplot(data[['Open', 'Open Rolling']].plot(figsize=(15,5)).figure)

# ----EXPANDING----
def expanding(data, tag):
  expanded = data[tag].expanding().mean()
  col1, col2 = st.columns(2)
  col1.dataframe(expanded.head(15))
  col2.line_chart(expanded, use_container_width=False)

# ----MAIN FUNCTION----
def main():
  st.title(f'{page_title} {page_icon}{icon}')
  st.subheader('By Mihir Pesswani')
  st.header('STOCK DATA')

  stock = st.selectbox('Select Stock', ['Choose an option', 'AAPL', 'AMZN', 'GOOG', 'IBM', 'MSFT'])
  col1,col2 = st.columns(2)
  sd = col1.date_input('Select Start Date', min_value=dt.date(1997,1,1), max_value=dt.date(2035, 1, 1), value=None, key='start')
  ed = col2.date_input('Select End Date', min_value=dt.date(1997,1,1), max_value=dt.date(2035, 1, 1), value=None, key='end')

  if stock != 'Choose an option':
    st.subheader('Data')
    data = reading_data(stock, sd,ed)

    st.markdown('---')
    st.subheader('Plots')
    tag = st.selectbox('Select the data to plot', data.columns)
    basic_plots(data, tag)

    col3, col4 = st.columns(2)
    xs = col3.date_input('Enter Start X-Limit', min_value=dt.date(1997,1,1), max_value=dt.date(2035, 1, 1), value=None, key='xstart')
    xe = col4.date_input('Enter End X-Limit', min_value=dt.date(1997,1,1), max_value=dt.date(2035, 1, 1), value=None, key='xend')
    ys = col3.number_input('Enter Start Y-Limit', key='ystart', step=1)
    ye = col4.number_input('Enter Start Y-Limit', key='yend', step=1)
    limit_plots(data, tag, xs, xe, ys, ye)

    st.markdown('---')
    st.header('ROLLING')
    col5, col6 = st.columns(2)
    window = col5.number_input('Enter Window Size', key='window_size', step=1)
    min_period = col6.number_input('Enter Min Period', key='min_period', step=1)
    rolling(data, tag, window, min_period)

    st.markdown('---')
    st.header("EXPANDING")
    expanding(data, tag)

if __name__ == '__main__':
  main()
