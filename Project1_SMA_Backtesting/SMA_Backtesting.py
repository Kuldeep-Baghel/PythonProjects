# Import Libraries
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
import logging

# Setup Logging
logging.basicConfig(
    filename='trade_log.txt',  
    level=logging.INFO,        
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# User-defined Inputs (Customize SMA Periods)
ticker = 'M&M.NS'
short_sma_period = 20  # Short-term SMA (Customizable)
long_sma_period = 50   # Long-term SMA (Customizable)
start_date = '2021-01-01'
end_date = date.today()

# Fetch Stock Data
stock = yf.download(ticker, start=start_date, end=end_date)

# Ensure Data is Available
if stock.empty:
    raise ValueError("No data fetched. Check ticker symbol or date range.")

# Function to Calculate SMA
def calculate_SMA(df, price_column, period):
    return df[price_column].rolling(window=period).mean()

# Compute Short-Term and Long-Term SMAs
stock[f'{short_sma_period}_SMA'] = calculate_SMA(stock, 'Close', short_sma_period)
stock[f'{long_sma_period}_SMA'] = calculate_SMA(stock, 'Close', long_sma_period)

# Generate Buy/Sell Signals based on SMA Crossovers
stock['Signal'] = np.where(stock[f'{short_sma_period}_SMA'] > stock[f'{long_sma_period}_SMA'], 1, 0)
stock['Crossover'] = stock['Signal'].diff()

# Plot the Buy/Sell signals
plt.figure(figsize=(15,8))
plt.plot(stock.index, stock[f'{short_sma_period}_SMA'], label=f'{short_sma_period}-SMA', color='blue')
plt.plot(stock.index, stock[f'{long_sma_period}_SMA'], label=f'{long_sma_period}-SMA', color='orange')

# Buy signals (Green Up Arrows)
plt.scatter(stock.index[stock['Crossover'] == 1].dropna(), 
            stock['Close'][stock['Crossover'] == 1].dropna(), 
            label='Buy', marker='^', color='green', s=100)

# Sell signals (Red Down Arrows)
plt.scatter(stock.index[stock['Crossover'] == -1].dropna(), 
            stock['Close'][stock['Crossover'] == -1].dropna(), 
            label='Sell', marker='v', color='red', s=100)

plt.title(f'Trading Signals for {ticker} ({short_sma_period}-SMA & {long_sma_period}-SMA)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Initialize Backtest Parameters
initial_capital = 100000
capital = initial_capital
position = 0                    
portfolio_value = []             

# Backtesting Loop
for i in range(len(stock)):
    price = stock['Close'].iloc[i].item()  
    signal = stock['Crossover'].iloc[i].item()  

    # Buy Condition
    if signal == 1 and capital > 0:
        position = capital // price
        capital -= position * price
        logging.info(f"Buy {position} shares at ₹{price:.2f}, Remaining Cash: ₹{capital:.2f}")

    # Sell Condition
    elif signal == -1 and position > 0:
        capital += position * price
        logging.info(f"Sell {position} shares at ₹{price:.2f}, New Cash: ₹{capital:.2f}")
        position = 0  

    # Track Portfolio Value
    portfolio_value.append(capital + (position * price))

# Final Portfolio Performance
final_value = capital + (position * stock['Close'].iloc[-1].item())
profit = final_value - initial_capital
roi = profit / initial_capital * 100

logging.info(f"Final Portfolio Value: ₹{final_value:.2f}")
logging.info(f"Profit: ₹{profit:.2f}")
logging.info(f"ROI: {roi:.2f} %")

# Portfolio Performance Plot
plt.figure(figsize=(15,8))
plt.plot(stock.index, portfolio_value, label="Portfolio Value", color='purple')
plt.axhline(y=initial_capital, color='grey', linestyle='--', label='Initial ₹1,00,000')
plt.xlabel('Date')
plt.ylabel('Portfolio Value (₹)')
plt.title('Backtest Portfolio Performance')
plt.legend()
plt.show()
