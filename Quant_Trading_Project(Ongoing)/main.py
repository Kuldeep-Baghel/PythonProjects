import sys
import os
import pandas as pd
from utils.config import CONFIG
from data_fetcher import fetch_stock_data  # Import fetch function
from strategies.sma import sma_crossover  # Import SMA strategy
from strategies.ema import ema_crossover  # Import EMA strategy
from backtester import backtest  # Import backtesting function

def main():
    if len(sys.argv) != 3:
        print("Usage: python run.py <ticker> <strategy>")
        sys.exit(1)
    
    ticker = sys.argv[1]
    strategy_name = sys.argv[2].upper()
    
    # Fetch or load data
    file_path = os.path.join(CONFIG['data_folder'], f"{ticker}.csv")
    if os.path.exists(file_path):
        print(f"Loading existing data for {ticker}...")
        stock_data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    else:
        print(f"Fetching data for {ticker}...")
        stock_data, _ = fetch_stock_data(ticker=ticker, save_csv=True)
    
    # Apply strategy
    if strategy_name == "SMA":
        print("Applying SMA Crossover Strategy...")
        stock_data = sma_crossover(stock_data)
    elif strategy_name == "EMA":
        print("Applying EMA Crossover Strategy...")
        stock_data = ema_crossover(stock_data)
    else:
        print("Invalid strategy! Use SMA or EMA.")
        sys.exit(1)
    
    # Run backtest
    results = backtest(stock_data)
    print("Backtest Results:")
    print(results)
    
    # Save results
    output_file = os.path.join(CONFIG['data_folder'], f"{ticker}_{strategy_name}_results.csv")
    stock_data.to_csv(output_file)
    print(f"Results saved to {output_file}")
    
if __name__ == "__main__":
    main()
