# %%
# Import Libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
import logging
import os

# %%
# Configure Logging
logging.basicConfig(
    filename='trade_log.txt',
    level=logging.INFO,  # ✅ Fixed missing comma
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# %%
# Configuration - User defined settings
ticker = 'INFY.NS'
start_date = '2021-01-01'
end_date = date.today()

# %%
# Fetching Stock Data
def fetch_stock_data(
        ticker=ticker, 
        start_date='2021-01-01',
        end_date=None,  # ✅ Set default to None
        save_csv=True):                   
    
    if end_date is None:  # ✅ Fix default date issue
        end_date = date.today()
    
    # Fetch Data from YFinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # Check if Data is available
    if stock_data.empty:
        raise ValueError(f"Stock Data for {ticker} not found. Check the ticker symbol or date range.")
    
    # Drop Missing Values
    stock_data.dropna(inplace=True)

    # Save to CSV
    file_path = None
    if save_csv:
        # ✅ Use the script's folder (instead of undefined PROJECT_DIR)
        data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")  
        os.makedirs(data_folder, exist_ok=True)
        file_path = os.path.join(data_folder, f'{ticker}.csv')
        stock_data.to_csv(file_path)
        print(f"Data Saved: {file_path}")

    return (stock_data, file_path) if save_csv else stock_data  # ✅ Return correctly
