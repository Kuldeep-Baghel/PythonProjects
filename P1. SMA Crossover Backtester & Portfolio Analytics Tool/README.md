#

## Overview
This Python project performs advanced backtesting on Simple Moving Average (SMA) crossover strategies. It enables interactive user input, dynamic portfolio performance tracking, and detailed visualizations using historical data from Yahoo Finance.

### ✅ Features  
    📈 Fetches stock data via yfinance  
    🔄 User inputs ticker, date range, initial capital & SMA periods  
    🟢 Detects Buy/Sell signals based on SMA crossovers  
    💼 Simulates trades with capital allocation logic  
    📊 Logs all trades in trade_log.txt  
    📉 Calculates advanced metrics:  
-            Sharpe Ratio  
-            Max Drawdown  
-            CAGR (Compounded Annual Growth Rate)  
-            Max Consecutive Losses  
    📷 Plots:  
-            Buy/Sell signals  
-            Portfolio performance  
-            Drawdown visualizations  

### ⚙️ Installation  
    Ensure Python is installed, then install required libraries:  
        pip install pandas numpy yfinance matplotlib  

### 🚀 Usage  
Run the script in any Python environment:  python advanced_sma_backtest.py  

### 🧠 You’ll be prompted to enter:  
-        Enter stock ticker (e.g., TCS.NS):  
-        Enter start date (YYYY-MM-DD):  
-        Enter end date (YYYY-MM-DD) or press Enter for today:  
-       Enter initial capital:  
-        Enter short SMA period:  
-        Enter long SMA period:  
 
### 📋 Sample Output  
    Inputs:  
-        Ticker: TCS.NS  
-        Date range: 2022-01-01 to 2024-12-31  
-        Capital: ₹100,000  
-        SMA periods: 50 & 200  

### 🔍 Backtest Summary:  
-        Final Portfolio Value: ₹123,456.78  
-        Profit: ₹23,456.78  
-        ROI: 23.46%  
-        Sharpe Ratio: 1.27  
-        Max Consecutive Losses: 2  
-        Max Drawdown: -7.32%  
-        CAGR: 11.12%  
✅ trade_log.txt captures buy/sell history  
✅ Two matplotlib charts:  
- SMA crossover with Buy/Sell markers  
- Portfolio value with drawdown shading  

🔍 Strategy Example: 50-SMA vs. 200-SMA  
Date	    | Action | Price  | Shares | Remaining Cash  
2022-02-15	    Buy	    ₹3,200	  31	  ₹800  
2023-05-30	    Sell	₹3,700    31	  ₹115,700  

Final Value: ₹115,700  
Profit: ₹15,700  
ROI: 15.7% 📈  

✅ Highlights:  
-        Interactive and customizable for any ticker  
-        Calculates real risk-adjusted return (Sharpe)  
-        Tracks drawdowns and trading losses streaks  
-        Shows CAGR for long-term performance insights  
-        Fully modular — easy to expand with new strategies (e.g., RSI, MACD)  

📄 License  
This project is open-source. Contributions and forks are welcome!

