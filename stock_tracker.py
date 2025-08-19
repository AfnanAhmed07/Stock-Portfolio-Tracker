def main():
    # Hardcoded stock prices dictionary
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2700,
        "AMZN": 3300,
        "MSFT": 300
    }

    print("Welcome to the Simple Stock Tracker!")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")

    total_investment = 0
    investments = {}

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not found in price list. Please try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter an integer.")
            continue

        investments[stock] = investments.get(stock, 0) + quantity
        total_investment += stock_prices[stock] * quantity

    print("\nYour Investments:")
    for stock, qty in investments.items():
        print(f"{stock}: {qty} shares at ${stock_prices[stock]} each")

    print(f"\nTotal Investment Value: ${total_investment}")

    save_option = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save_option == 'yes':
        file_type = input("Enter file type to save (txt/csv): ").lower()
        filename = input("Enter filename (without extension): ")

        if file_type == 'txt':
            with open(f"{filename}.txt", "w") as f:
                f.write("Stock Investments\n")
                for stock, qty in investments.items():
                    f.write(f"{stock}: {qty} shares at ${stock_prices[stock]} each\n")
                f.write(f"Total Investment Value: ${total_investment}\n")
            print(f"Results saved to {filename}.txt")
        elif file_type == 'csv':
            import csv
            with open(f"{filename}.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
                for stock, qty in investments.items():
                    writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock]*qty])
                writer.writerow([])
                writer.writerow(["Total Investment Value", "", "", total_investment])
            print(f"Results saved to {filename}.csv")
        else:
            print("Unsupported file type. Result not saved.")

if __name__ == "__main__":
    main()
