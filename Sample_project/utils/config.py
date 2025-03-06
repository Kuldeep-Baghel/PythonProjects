# Import Libraires
from datetime import date
import os

# Get the absolute path of the project directory
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# config.py - Holds all user-defined settings
CONFIG = {
    # Configuration for Fetching Stock Data
    'ticker':'NTPC.NS',               # Stock Symbol
    'start_date': '2021-01-01',                 # Start Date for historical data
    'end_date': date.today().isoformat(),       # End Date

    # Configuration for Strategies
    'price_column': 'Close',            # Price taken for the Calculation of different Strategies
    'fast_period': 50,                  # Shorter Period for Calculation of Strategies
    'slow_period' : 200,                # Longer Period for Calculaton of Strategies

    # Configuration for Backtesting
    'initial_capital': 100000,          # Initial Value for Investment
    'position': 0,                      # Any Position in Market

    # Paths
    'data_folder': os.path.abspath(os.path.join(PROJECT_DIR, "..", "data")),  # Ensures correct data folder path
}