# ----IMPORTING PACKAGES----
import pandas as pd
import streamlit as st
import datetime as dt
import pandas_datareader as pdr

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
  
# ----ROLLING----
def rolling():
  pass

# ----EXPANDING----
def expanding():
  pass

# ----MAIN FUNCTION----
def main():
  st.title('STOCK ANALYSER - TIME SERIES')
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


if __name__ == '__main__':
  main()
