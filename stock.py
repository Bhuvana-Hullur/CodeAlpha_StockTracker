stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 125,
    "MSFT": 300
}

portfolio = {} 
total_investment = 0

print(" Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when finished.\n")


while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print(" Stock not found. Try again.")
        continue
    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity


print("\n Investment Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n Total Investment Value: ${total_investment}")


save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}")
    print(" Summary saved to 'portfolio_summary.txt'")
