import numpy as np

def evaluate_performance(portfolio_values):
    """
    Evaluates strategy performance.
    
    :param portfolio_values: List of portfolio values.
    :return: Dictionary with performance metrics.
    """
    returns = np.diff(portfolio_values) / portfolio_values[:-1]
    total_return = (portfolio_values[-1] - portfolio_values[0]) / portfolio_values[0]
    volatility = np.std(returns)
    
    return {
        "Total Return": total_return * 100,
        "Volatility": volatility * 100
    }
