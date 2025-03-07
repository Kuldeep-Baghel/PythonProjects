import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(
    filename="portfolio_report.log",  # Save logs to a file
    filemode="w",  # Overwrite the file on each run
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Step 1: Fetch Historical Data for Multiple Assets
def fetch_data(tickers, start='2023-01-01', end='2024-01-01'):
    data = yf.download(tickers, start=start, end=end)['Close']
    return data

# Step 2: Compute Daily Returns & Portfolio Performance
def calculate_portfolio_performance(weights, returns):
    portfolio_return = np.dot(weights, returns.mean()) * 252
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    sharpe_ratio = portfolio_return / portfolio_volatility
    return portfolio_return, portfolio_volatility, sharpe_ratio

# Step 3: Monte Carlo Simulation for Portfolio Optimization
def monte_carlo_simulation(returns, num_simulations=5000):
    num_assets = len(returns.columns)
    results = np.zeros((3, num_simulations))
    all_weights = np.zeros((num_simulations, num_assets))
    
    for i in range(num_simulations):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        all_weights[i, :] = weights
        results[:, i] = calculate_portfolio_performance(weights, returns)
    
    # Find the best Sharpe ratio portfolio
    max_sharpe_idx = np.argmax(results[2])
    best_weights = all_weights[max_sharpe_idx, :]
    
    # Find the minimum volatility portfolio
    min_vol_idx = np.argmin(results[1])
    min_vol_weights = all_weights[min_vol_idx, :]
    
    return results, best_weights, min_vol_weights

# Step 4: Value-at-Risk (VaR) and Conditional VaR (CVaR)
def calculate_var_cvar(returns, confidence_level=0.95):
    var = np.percentile(returns, (1 - confidence_level) * 100)
    cvar = returns[returns <= var].mean()  # Expected Shortfall
    return var, cvar

# Step 5: Black-Scholes Model for Option Pricing
def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    def norm_cdf(x):
        return (1.0 + np.sign(x) * np.sqrt(1 - np.exp(-x**2 / np.pi))) / 2.0
    
    if option_type == 'call':
        return S * norm_cdf(d1) - K * np.exp(-r * T) * norm_cdf(d2)
    else:
        return K * np.exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)

# Step 6: Visualization of Monte Carlo Simulation
def plot_monte_carlo(results):
    plt.figure(figsize=(10, 6))
    plt.scatter(results[1], results[0], c=results[2], cmap='viridis', alpha=0.5)
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Volatility')
    plt.ylabel('Return')
    plt.title('Monte Carlo Simulation of Portfolio Allocation')
    plt.show()

def save_results(optimized_weights, min_vol_weights, var_95, cvar_95, option_price):
    logging.info("=== Portfolio Optimization & Risk Analysis ===")
    logging.info(f"Optimized Portfolio Weights: {optimized_weights}")
    logging.info(f"Minimum Volatility Portfolio Weights: {min_vol_weights}")
    logging.info(f"95% Value-at-Risk (VaR): {var_95:.6f}")
    
    # Convert cvar_95 to a scalar if it's a Pandas Series
    cvar_95_value = cvar_95.mean() if isinstance(cvar_95, pd.Series) else cvar_95
    logging.info(f"95% Conditional VaR (CVaR): {cvar_95_value:.6f}")
    
    logging.info(f"Black-Scholes Option Price: {option_price:.6f}")

if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
    stock_data = fetch_data(tickers)
    daily_returns = stock_data.pct_change().dropna()
    
    # Monte Carlo Simulation
    mc_results, optimized_weights, min_vol_weights = monte_carlo_simulation(daily_returns)
    
    # VaR & CVaR Calculation
    var_95, cvar_95 = calculate_var_cvar(daily_returns)
    
    # Black-Scholes Example Calculation
    option_price = black_scholes(S=150, K=145, T=0.5, r=0.05, sigma=0.2)
    
    # Save results to log file
    save_results(optimized_weights, min_vol_weights, var_95, cvar_95, option_price)
    
    # Plot Monte Carlo Results
    plot_monte_carlo(mc_results)