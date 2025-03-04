# SMA Backtesting with Python

## Overview
This project performs backtesting on **Simple Moving Average (SMA) crossover strategies** using historical stock data from Yahoo Finance. It allows users to test different SMA combinations and visualize buy/sell signals.

## Features
✅ Fetches historical stock data using `yfinance`
✅ Computes **custom SMA crossovers** (e.g., 20-SMA & 50-SMA, 50-SMA & 200-SMA)
✅ Identifies **buy & sell signals** based on SMA crossovers
✅ **Backtests strategy** with an initial capital of ₹100,000
✅ Logs trades in `trade_log.txt`
✅ **Visualizes** price movements, SMAs, and portfolio performance

---
## Installation
Ensure you have Python installed. Then, install the required dependencies:
```bash
pip install pandas numpy yfinance matplotlib
```

---
## Usage
### 1️⃣ Run the script
Execute the script in a Python environment:
```bash
python sma_backtest.py
```

### 2️⃣ Customize SMA Periods
Modify these variables in the script to test different strategies:
```python
short_sma_period = 20  # Change to any short-term SMA
long_sma_period = 50   # Change to any long-term SMA
```

### 3️⃣ Review Output
- **Trading signals plotted** on a price chart
- **Trade logs recorded** in `trade_log.txt`
- **Portfolio performance graph** displayed

---
## Example Strategy: 20-SMA vs. 50-SMA
| Date | Action | Price | Shares | Remaining Cash |
|------|--------|--------|---------|----------------|
| 2022-03-01 | Buy | ₹800 | 125 | ₹0 |
| 2022-06-15 | Sell | ₹920 | 125 | ₹115,000 |

Final Portfolio Value: ₹115,000  
Profit: ₹15,000  
ROI: **15%** 📈

---
## Next Steps
- Experiment with different SMA periods to optimize strategies.
- Extend the strategy with **stop-loss & take-profit conditions**.
- Upload results to GitHub and track different stock performances!

---
## License
This project is **open-source**. Feel free to modify and enhance it!

---
💡 **Need help?** Feel free to ask for modifications or explanations! 🚀


