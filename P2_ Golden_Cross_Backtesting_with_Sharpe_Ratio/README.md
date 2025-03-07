# Quantitative Trading Strategy - SMA Crossover Backtest

This project implements a simple **Quantitative Trading Strategy** using **SMA (Simple Moving Average) Crossover**. 
The strategy involves calculating two moving averages (50-day and 200-day) and generating buy/sell signals based on crossovers.

## Features
- Fetches historical stock price data using Yahoo Finance.
- Implements a **Golden Cross & Death Cross Strategy**.
- Conducts **backtesting** to evaluate strategy performance.
- Logs trade executions in a text file.
- Visualizes **trading signals and portfolio performance**.

## Strategy Logic
- **Golden Cross** (Buy Signal) → When the **50-day SMA** crosses above the **200-day SMA**.
- **Death Cross** (Sell Signal) → When the **50-day SMA** crosses below the **200-day SMA**.

## Technologies Used
- **Python**
- **pandas, numpy** (Data Handling & Analysis)
- **yfinance** (Fetching Stock Data)
- **matplotlib** (Data Visualization)
- **logging** (Trade Logging)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/quant-trading-sma.git
   cd quant-trading-sma
   ```
2. Install dependencies:
   ```sh
   pip install pandas numpy yfinance matplotlib
   ```
3. Run the script:
   ```sh
   python backtest_sma.py
   ```

## Output
- Buy/Sell signals plotted on the stock price chart.
- Final Portfolio Value, ROI, and trade log in `trade_log.txt`.
- Portfolio performance visualization.

## Future Enhancements
- Add **Sharpe Ratio Calculation** to evaluate risk-adjusted returns.
- Implement **Stop-Loss & Take-Profit** rules.
- Enhance the strategy using **RSI & MACD Indicators**.
- Optimize backtesting with **vectorized calculations**.

## License
This project is open-source and free to use.

---
Developed with ❤️ for learning and quant finance exploration! 🚀
