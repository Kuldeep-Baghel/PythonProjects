import pandas as pd
import numpy as np
from utils.config import CONFIG

def backtester(stock_data):
    """
    Backtests a trading strategy on given stock data.
    
    :param stock_data: DataFrame with 'Close', 'Buy_Signal', 'Sell_Signal'.
    :return: Portfolio value list.
    """
    initial_capital = CONFIG['initial_capital']
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
            print(f"Sell {position:.2f} shares at {row['Close']:.2f}, Total Capital: {capital:.2f}")
            position = 0
        
        total_value = capital + (row['Close'] * position)
        portfolio_value.append(total_value)

    # Final Sell
    if position > 0:
        capital += position * stock_data.iloc[-1]['Close']
        print(f"Final Sale: Sold at {stock_data.iloc[-1]['Close']:.2f}, Total Capital: {capital:.2f}")
    
    return portfolio_value
    