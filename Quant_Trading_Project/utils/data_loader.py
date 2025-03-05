# %%
#Import Liabraries
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date
import os

#%%
# Function to fetch the Data
def fetch_stock_data(
        ticker, 
        start_date='2022-01-01',
        end_date = date.today(),
        save_csv =True):                    
    
    #fetch Data from Yfinance
    stock_data = yf.download(ticker, start= start_date, end=end_date)

    # Check if Data is available
    if stock_data.empty:
        raise ValueError(f"Stock Data for {ticker} not found. Check the tricker symbol or date range")
    
    # Drop Missing Value
    stock_data.dropna(inplace= True)

    # Save to CSV
    if save_csv:
        os.makedirs("data", exist_ok=True)
        file_path = f"data/{ticker}.csv"
        stock_data.to_csv(file_path)
        print(f"Data Saved: {file_path}")

    return stock_data

# %%
#Example Usage
if __name__ == "__main__":
    fetch_stock_data("INFY.NS")

# %%
