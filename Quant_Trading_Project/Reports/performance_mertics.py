import numpy as np
import pandas as pd

def calculate_total_return(stock_data):
    """Calculates the total return of the strategy"""
    initial_price = stock_data["Close"].iloc[0]
    final_price = stock_data["Close"].iloc[-1]
    return (final_price - initial_price) / initial_price

def calculate_sharpe_ratio(stock_data, risk_free_rate=0.02):
    """Calculates the Sharpe Ratio"""
    daily_returns = stock_data["Close"].pct_change().dropna()
    excess_returns = daily_returns - (risk_free_rate / 252)
    sharpe_ratio = np.sqrt(252) * excess_returns.mean() / excess_returns.std()
    return sharpe_ratio

def calculate_cagr(stock_data, years=1):
    """Calculates CAGR"""
    initial_price = stock_data["Close"].iloc[0]
    final_price = stock_data["Close"].iloc[-1]
    return (final_price / initial_price) ** (1 / years) - 1

def calculate_max_drawdown(stock_data):
    """Calculates the maximum drawdown"""
    cumulative_returns = stock_data["Close"].pct_change().cumsum()
    rolling_max = cumulative_returns.cummax()
    drawdown = rolling_max - cumulative_returns
    max_drawdown = drawdown.max()
    return max_drawdown
