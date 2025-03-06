# Add the project's root directory to Python's search path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import Liabraries
import pandas as pd
import yfinance as yf
from datetime import date
from utils.config import CONFIG       # Import settings   

# Function to fetch the Data
def fetch_stock_data(
        ticker = CONFIG['ticker'], 
        start_date= CONFIG['start_date'],
        end_date = CONFIG['end_date'],
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
        data_folder = CONFIG['data_folder']
        os.makedirs(data_folder, exist_ok=True)
        file_path = os.path.join(data_folder, f'{ticker}.csv')
        stock_data.to_csv(file_path)
        print(f"Data Saved: {file_path}")

    return stock_data, file_path if save_csv else None

#Example Usage
if __name__ == "__main__":
    fetch_stock_data()
