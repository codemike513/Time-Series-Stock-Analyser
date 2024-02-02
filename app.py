import pandas as pd
import streamlit as st
import datetime as dt
import pandas_datareader as pdr

def reading_data(stock, sd, ed):
  data = pdr.DataReader(stock, 'stooq', sd, ed)
  st.dataframe(data.head())

def rolling():
  pass

def expanding():
  pass

def main():
  sd = dt.datetime(2000,1,1)
  ed = dt.datetime(2020,1,1)
  reading_data('AAPL', sd,ed)

if __name__ == '__main__':
  main()
