def generate_results(performance):
    """
    Prints the backtesting results.
    
    :param performance: Performance metrics dictionary.
    """
    print("\nBacktest Results:")
    print(f"Total Return: {performance['Total Return']:.2f}%")
    print(f"Volatility: {performance['Volatility']:.2f}%")
