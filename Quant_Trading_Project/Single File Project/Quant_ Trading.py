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
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

#%%
# Configure Logging
log_file_path = os.path.join(script_dir, 'trade_log.txt')
logging.basicConfig(
    filename='trade_log.txt',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# %%
# Configuration - User defined settings

# Stock Data Configuration
ticker = ['INFY.NS','M&M.NS', 'NTPC.NS', 'TCS.NS']
start_date = '2021-01-01'
end_date = date.today()

# Strategies Configuration 
price_column ='Close'            # Price taken for the Calculation of different Strategies
fast_period = 50                 # Shorter Period for Calculation of Strategies
slow_period = 200                # Longer Period for Calculaton of Strategies

# Backtester Congiuration
initial_capital = 100000

# %%
#fetch Data from Yfinance
stock_data = yf.download(ticker, start= start_date, end=end_date)

# Check if Data is available
if stock_data.empty:
    raise ValueError(f"Stock Data for {ticker} not found. Check the tricker symbol or date range")
    
# Drop Missing Value
stock_data.dropna(inplace= True)

#%%
# Define Simple Moving Average (SMA)
def sma(stock_data, price_column, period):
    return stock_data[price_column].rolling(window=period).mean()

# Define SMA Crossover Strategy
def sma_crossover(stock_data):
       
    # Calculate Fast and Slow SMA
    stock_data[f'{fast_period}_SMA'] = sma(stock_data, price_column, fast_period)
    stock_data[f'{slow_period}_SMA'] = sma(stock_data, price_column, slow_period)

    # Generate Signal
    stock_data['Signal'] = np.where(stock_data[f'{fast_period}_SMA'] > stock_data[f'{slow_period}_SMA'], 1, 0)
    stock_data['Crossover'] = stock_data['Signal'].diff()

    # Initialize Buy/Sell Signal
    stock_data['Buy_Signal'] = np.where(stock_data['Crossover'] == 1, 1, 0)
    stock_data['Sell_Signal'] = np.where(stock_data['Crossover'] == -1, 1, 0)
    return stock_data

# %%
# Define Exponential Moving Average (EMA)
def ema(stock_data, price_column, period):
    return stock_data[price_column].ewm(span=period, adjust= False).mean()

# Define EMA Crossover
def ema_crossover(stock_data):
    
    stock_data[f'{fast_period}_EMA'] = ema(stock_data, price_column, fast_period)
    stock_data[f'{slow_period}_EMA'] = ema(stock_data, price_column, slow_period)

    # Generate Signal
    stock_data['Signal'] = np.where(stock_data[f'{fast_period}_EMA'] > stock_data[f'{slow_period}_EMA'], 1, 0)
    stock_data['Crossover'] = stock_data['Signal'].diff()

    # Initialize Buy/Sell Signal
    stock_data['Buy Signal'] = np.where(stock_data['Crossover'] == 1, 1, 0)
    stock_data['Sell Signal'] = np.where(stock_data['Crossover'] == -1, 1, 0)

    return stock_data

# %%
# Backtesting Engine
def backtester(stock_data):
    capital = initial_capital
    position = 0
    portfolio_value = []

    for index, row in stock_data.iterrows():
        if row['Buy_Signal'] == 1 and capital > 0:
            position = capital / row['Close']
            capital -= position * row['Close']
            print(f"Buy {position:.2f} shares at {row['Close']:.2f}, Remaining capital: {capital:.2f}")

        elif row['Sell_Signal'] == 1 and position > 0:
            capital += position * row['Close']
            print(f"Sell {position:.2f} shares at {row['Close']:.2f}, Total Capital {capital:.2f}")
            position = 0

        total_value = capital + (row['Close'] * position)
        portfolio_value.append(total_value)

    # Final Sale (if still holding a position)
    if position > 0:
        capital += position * stock_data.iloc[-1]['Close']
        print(f"Final Sale: Sold {position:.2f} shares at {stock_data.iloc[-1]['Close']:.2f}, Total Capital: {capital:.2f}")
        portfolio_value.append(capital)
    
    return portfolio_value

portfolio_values = backtester(stock_data)
profit = portfolio_values - initial_capital
roi = (profit / initial_capital) * 100

# Logging Summary
logging.info(f"Final Portfolio Value: {portfolio_values:.2f}")
logging.info(f"Total Profit: {profit:.2f}")
logging.info(f"ROI: {roi:.2f}%")
# %%
