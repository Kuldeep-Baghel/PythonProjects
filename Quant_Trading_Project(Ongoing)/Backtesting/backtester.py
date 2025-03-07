# Import Libraries
import pandas as pd
import numpy as np
import os
import sys

# Add project root directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load Configuration
from utils.config import CONFIG
from utils.data_loader import fetch_stock_data
from strategies.sma import apply_sma_strategy
from strategies.ema import apply_ema_strategy

# Backtesting Engine
def backtester(stock_data):
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

# Main Execution
if __name__ == "__main__":
    stock_data = fetch_stock_data()
    stock_data = apply_sma_strategy(stock_data)
    stock_data = apply_ema_strategy(stock_data)
    portfolio_values = backtester(stock_data)
    print("Final Portfolio Value:", portfolio_values[-1])

