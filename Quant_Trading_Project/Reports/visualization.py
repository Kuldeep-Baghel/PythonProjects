import matplotlib.pyplot as plt

def plot_strategy(stock_data, strategy_name="Strategy"):
    """Plots stock prices with buy/sell signals"""
    plt.figure(figsize=(12, 6))
    
    plt.plot(stock_data["Date"], stock_data["Close"], label="Stock Price", color="blue")
    
    if "Buy_Signal" in stock_data.columns:
        plt.scatter(stock_data["Date"], stock_data["Buy_Signal"], label="Buy Signal", marker="^", color="green", alpha=1)
    
    if "Sell_Signal" in stock_data.columns:
        plt.scatter(stock_data["Date"], stock_data["Sell_Signal"], label="Sell Signal", marker="v", color="red", alpha=1)
    
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.title(f"{strategy_name} Performance")
    plt.legend()
    plt.grid()
    plt.show()
