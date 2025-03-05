# Import Librairies
import pandas as pd
import numpy as np

# Define Exponential Moving Average (EMA)
def ema(stock_data, price_column, period):
    return stock_data[price_column].ewm(span=period, adjust= False).mean()

# Define EMA Crossover
def ema_crossover(stock_data, price_column= 'Close', fast_period=50, slow_period=100):
    stock_data[f'{fast_period}_EMA'] = ema(stock_data, price_column, fast_period)
    stock_data[f'{slow_period}_EMA'] = ema(stock_data, price_column, slow_period)

    # Generate Signal
    stock_data['Signal'] = np.where(stock_data[f'{fast_period}_EMA'] > stock_data[f'{slow_period}_SMA'], 1, 0)
    stock_data['Crossover'] = stock_data['Signal'].diff()

    # Initialize Buy/Sell Signal
    stock_data['Buy Signal'] = np.where(stock_data['Crossover'] == 1, 1, 0)
    stock_data['Sell Signal'] = np.where(stock_data['Crossover'] == -1, 1, 0)

    return stock_data