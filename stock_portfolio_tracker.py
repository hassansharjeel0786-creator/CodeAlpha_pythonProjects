# Stock Portfolio Tracker
# This program allows users to track their stock investments using predefined stock prices.

# Hardcoded dictionary of stock symbols and their prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320
}

# Function to validate stock symbol
def is_valid_stock(symbol):
    return symbol.upper() in stock_prices

# Function to validate quantity (positive integer)
def is_valid_quantity(quantity):
    try:
        qty = int(quantity)
        return qty > 0
    except ValueError:
        return False

# Function to calculate total value for a stock
def calculate_stock_value(price, quantity):
    return price * quantity

# Main function
def main():
    portfolio = []  # List to store portfolio items
    total_investment = 0.0

    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print()

    while True:
        # Ask for stock symbol
        symbol = input("Enter stock symbol (or 'done' to finish): ").strip().upper()
        if symbol == 'DONE':
            break

        # Validate stock symbol
        if not is_valid_stock(symbol):
            print(f"Error: '{symbol}' is not a valid stock symbol. Please try again.")
            continue

        # Ask for quantity
        quantity_input = input(f"Enter quantity of shares for {symbol}: ").strip()

        # Validate quantity
        if not is_valid_quantity(quantity_input):
            print("Error: Quantity must be a positive integer. Please try again.")
            continue

        quantity = int(quantity_input)
        price = stock_prices[symbol]
        value = calculate_stock_value(price, quantity)

        # Add to portfolio
        portfolio.append({
            "symbol": symbol,
            "price": price,
            "quantity": quantity,
            "value": value
        })

        total_investment += value
        print(f"Added {quantity} shares of {symbol} at ${price} each. Total value: ${value:.2f}")
        print()

    # Display portfolio summary
    if portfolio:
        print("Portfolio Summary:")
        print("-" * 50)
        print(f"{'Stock':<10} {'Price':<10} {'Quantity':<10} {'Total Value':<15}")
        print("-" * 50)
        for item in portfolio:
            print(f"{item['symbol']:<10} ${item['price']:<9.2f} {item['quantity']:<10} ${item['value']:<14.2f}")
        print("-" * 50)
        print(f"Total Investment Value: ${total_investment:.2f}")
        print()

        # Optional: Save to file
        save_option = input("Do you want to save the portfolio to a file? (yes/no): ").strip().lower()
        if save_option == 'yes':
            filename = input("Enter filename (e.g., portfolio.txt): ").strip()
            try:
                with open(filename, 'w') as file:
                    file.write("Portfolio Summary\n")
                    file.write("-" * 50 + "\n")
                    file.write(f"{'Stock':<10} {'Price':<10} {'Quantity':<10} {'Total Value':<15}\n")
                    file.write("-" * 50 + "\n")
                    for item in portfolio:
                        file.write(f"{item['symbol']:<10} ${item['price']:<9.2f} {item['quantity']:<10} ${item['value']:<14.2f}\n")
                    file.write("-" * 50 + "\n")
                    file.write(f"Total Investment Value: ${total_investment:.2f}\n")
                print(f"Portfolio saved to {filename}")
            except Exception as e:
                print(f"Error saving file: {e}")
    else:
        print("No stocks added to portfolio.")

if __name__ == "__main__":
    main()
