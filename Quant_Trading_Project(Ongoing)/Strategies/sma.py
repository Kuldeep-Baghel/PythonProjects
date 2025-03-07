# Add the project's root directory to Python's search path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import Libraries
import pandas as pd
import numpy as np
from utils.config import CONFIG

# Define Simple Moving Average (SMA)
def sma(stock_data, price_column, period):
    return stock_data[price_column].rolling(window=period).mean()

# Define SMA Crossover Strategy
def sma_crossover(stock_data):
    price_column= CONFIG['price_column']
    fast_period= CONFIG['fast_period']
    slow_period= CONFIG['slow_period']

   
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

