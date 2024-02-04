import pandas as pd
import streamlit as st
import datetime as dt
import pandas_datareader as pdr

def reading_data(stock, sd, ed):
  data = pdr.DataReader(stock, 'stooq', sd, ed)
  st.subheader('Data')
  st.dataframe(data)
  st.dataframe(data.head())
  st.dataframe(data.tail())
  

def rolling():
  pass

def expanding():
  pass

def main():
  sd = dt.datetime(2000,1,1)
  ed = dt.datetime(2020,1,1)
  stock = st.text('Enter Stock Name')
  reading_data(stock, sd,ed)

if __name__ == '__main__':
  main()
