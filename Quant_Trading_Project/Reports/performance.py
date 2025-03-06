def calculate_performance(portfolio_value, initial_capital):
    """Calculates final portfolio value, profit, and ROI."""
    
    final_portfolio_value = portfolio_value[-1]
    profit = final_portfolio_value - initial_capital
    roi = (profit / initial_capital) * 100

    # Print Summary
    print(f"Final Portfolio Value: {final_portfolio_value:.2f}")
    print(f"Total Profit: {profit:.2f}")
    print(f"ROI: {roi:.2f}%")

    return final_portfolio_value, profit, roi  # Return values for further use
