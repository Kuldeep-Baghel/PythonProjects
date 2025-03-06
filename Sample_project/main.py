from utils import load_data, CONFIG
from strategies import apply_sma_strategy, apply_ema_strategy
from backtesting.backtester import backtester
from reports import evaluate_performance, generate_results

# Load stock data
file_path = "data/RELIANCE.NS.csv"
stock_data = load_data(file_path)

# Apply Strategy
stock_data = apply_sma_strategy(stock_data, CONFIG['short_sma'], CONFIG['long_sma'])
# stock_data = apply_ema_strategy(stock_data, CONFIG['short_ema'], CONFIG['long_ema'])  # Uncomment for EMA strategy

# Run Backtest
portfolio_values = backtester(stock_data)

# Evaluate Performance
performance = evaluate_performance(portfolio_values)
generate_results(performance)
