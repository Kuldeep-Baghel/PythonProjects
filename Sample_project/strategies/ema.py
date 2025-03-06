import pandas as pd

def apply_ema_strategy(data, short_window=12, long_window=26):
    """
    Implements the EMA crossover strategy.
    
    :param data: DataFrame with 'Close' prices.
    :param short_window: Shorter EMA period.
    :param long_window: Longer EMA period.
    :return: DataFrame with buy/sell signals.
    """
    data['EMA_Short'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA_Long'] = data['Close'].ewm(span=long_window, adjust=False).mean()

    data['Buy_Signal'] = (data['EMA_Short'] > data['EMA_Long']).astype(int)
    data['Sell_Signal'] = (data['EMA_Short'] < data['EMA_Long']).astype(int)
    
    return data
