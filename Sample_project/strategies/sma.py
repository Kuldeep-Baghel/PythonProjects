import pandas as pd

def apply_sma_strategy(data, short_window=50, long_window=200):
    """
    Implements the SMA crossover strategy.
    
    :param data: DataFrame with 'Close' prices.
    :param short_window: Shorter SMA period.
    :param long_window: Longer SMA period.
    :return: DataFrame with buy/sell signals.
    """
    data['SMA_Short'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['SMA_Long'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

    data['Buy_Signal'] = (data['SMA_Short'] > data['SMA_Long']).astype(int)
    data['Sell_Signal'] = (data['SMA_Short'] < data['SMA_Long']).astype(int)
    
    return data
