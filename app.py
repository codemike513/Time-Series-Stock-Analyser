import pandas as pd
import streamlit as st
import datetime as dt
import pandas_datareader as pdr

def reading_data(stock, sd, ed):
  data = pdr.DataReader(stock, 'stooq', sd, ed)
  st.dataframe(data)

  col3, col4 = st.columns(2)

  col3.subheader('Head')
  col3.dataframe(data.head())
  col4.subheader('Tail')
  col4.dataframe(data.tail())

  return data

def basic_plots(data, tag):
  st.line_chart(data[tag])
  
def rolling():
  pass

def expanding():
  pass

def main():
  st.title('STOCK ANALYSER - TIME SERIES')
  stock = st.selectbox('Select Stock', ['AAPL', 'AMZN', 'GOOG', 'IBM', 'MSFT'])
  sd = dt.datetime(2000,1,1)
  ed = dt.datetime(2020,1,1)
  st.subheader('Data')
  data = reading_data(stock, sd,ed)

  st.markdown('---')
  st.subheader('Plots')
  tag = st.selectbox('Select the data to plot', data.columns)
  basic_plots(data, tag)


if __name__ == '__main__':
  main()
