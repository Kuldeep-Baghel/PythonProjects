import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
import logging

# Setup logging
logging.basicConfig(
    filename='trade_log.txt',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Define stock
ticker = 'TCS.NS'
start_date = '2021-01-01'
end_date = date.today()

# Fetch Stock Data
stock = yf.download(ticker, start=start_date, end=end_date)
if stock.empty:
    raise ValueError("No data fetched. Check ticker symbol or date range.")

# Function to Calculate Moving Averages
def stock_SMA(df, price_column, period):
    return df[price_column].rolling(window=period).mean()

# Compute SMAs
stock['50_SMA'] = stock_SMA(stock, 'Close', 50)
stock['200_SMA'] = stock_SMA(stock, 'Close', 200)

# Implement Trading Strategy
stock['Signal'] = np.where(stock['50_SMA'] > stock['200_SMA'], 1, 0)
stock['Crossover'] = stock['Signal'].diff()

# Initialize Backtest Parameters
initial_capital = 100000
capital = initial_capital
position = 0
portfolio_value = []
trade_returns = []
logging.info(f" Trade Analysis of {ticker}")

for i in range(len(stock)):
    price = stock['Close'].iloc[i].item()
    signal = stock['Crossover'].iloc[i].item()

    if signal == 1 and capital > 0:  # Buy signal
        position = capital // price
        capital -= position * price
        logging.info(f"Buy {position} shares at ₹{price:.2f}, Remaining Cash: ₹{capital:.2f}")
    elif signal == -1 and position > 0:  # Sell signal
        capital += position * price
        trade_returns.append((capital + (position * price)) - initial_capital)
        logging.info(f"Sell {position} shares at ₹{price:.2f}, New Cash: ₹{capital:.2f}")
        position = 0
    portfolio_value.append(capital + (position * price))

# Calculate Final Portfolio Value
final_value = capital + (position * stock['Close'].iloc[-1].item())
profit = final_value - initial_capital
roi = profit / initial_capital * 100
logging.info(f"Final Portfolio Value: ₹{final_value:.2f}")
logging.info(f"Profit: ₹{profit:.2f}")
logging.info(f"ROI: {roi:.2f} %")

# Calculate Sharpe Ratio
returns = pd.Series(portfolio_value).pct_change().dropna()
risk_free_rate = 0.05 / 252  # Annualized 5% risk-free rate converted to daily
sharpe_ratio = (returns.mean() - risk_free_rate) / returns.std()
logging.info(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# Calculate Maximum Consecutive Losses without using groupby
max_consecutive_losses = 0
current_loss_streak = 0

for ret in trade_returns:
    if ret < 0:
        current_loss_streak += 1
        max_consecutive_losses = max(max_consecutive_losses, current_loss_streak)
    else:
        current_loss_streak = 0  # Reset streak on profit

logging.info(f"Max Consecutive Losses: {max_consecutive_losses}")

# Plot Portfolio Performance
plt.figure(figsize=(15, 8))
plt.plot(stock.index[:len(portfolio_value)], portfolio_value, label="Portfolio Value", color='purple')
plt.axhline(y=initial_capital, color='grey', linestyle='--', label='Initial ₹1,00,000')
plt.xlabel('Date')
plt.ylabel('Portfolio Value (₹)')
plt.title('Backtest Portfolio Performance')
plt.legend()
plt.show()
