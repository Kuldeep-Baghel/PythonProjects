#%%
# Import Libraries
import pandas as pd
import numpy as np

#%%
# Define Simple Moving Average (SMA)
def sma(stock_data, price_column, period):
    """
    Calculate Simple Moving Average (SMA).

    Parameters:
    stock_data (pd.DataFrame): DataFrame containing stock price data.
    price_column (str): Column name for stock prices.
    period (int): Moving average period.

    Returns:
    pd.Series: SMA values.
    """
    return stock_data[price_column].rolling(window=period).mean()

# Define SMA Crossover Strategy
def sma_crossover(stock_data, price_column='Close', fast_period=50, slow_period=200):
    '''
    Implements The SMA Crossoverover Strategy

    Parameters:
    stock_data (pd.DataFrame): DataFrame containing stock price data.
    price_column (str): Column name for stock prices (default: "Close").
    fast_period (int): Short-term SMA period (default: 50).
    slow_period (int): Long-term SMA period (default: 200).

    Returns:
    pd.DataFrame: Stock data with SMA values and Buy/Sell signals.
    '''
    # Calculate Fast and Slow SMA
    stock_data[f'{fast_period}_SMA'] = sma(stock_data, price_column, fast_period)
    stock_data[f'{slow_period}_SMA'] = sma(stock_data, price_column, slow_period)

    # Generate Signal
    stock_data['Signal'] = np.where(stock_data[f'{fast_period}_SMA'] > stock_data[f'{slow_period}_SMA'], 1, 0)
    stock_data['Crossover'] = stock_data['Signal'].diff()

    # Initialize Buy/Sell Signal
    stock_data['Buy_Signal'] = np.where(stock_data['Crossover'] == 2, 1, 0)
    stock_data['Sell_Signal'] = np.where(stock_data['Crossover'] == -2, 1, 0)
    return stock_data

