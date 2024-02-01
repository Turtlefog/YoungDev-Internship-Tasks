from forex_python.converter import CurrencyRates

def currency_converter():
    # Create a CurrencyRates object
    c = CurrencyRates()

    print("Welcome to the Currency Converter!")

    # Get a list of available currencies
    currencies = c.get_rates('USD')

    # Display available currencies
    print("Available currencies:")
    for currency, rate in currencies.items():
        print(f"{currency} ({rate:.2f})")

    # Get user input for conversion
    from_currency = input("Enter the currency code you want to convert from: ").upper()
    to_currency = input("Enter the currency code you want to convert to: ").upper()
    amount = float(input("Enter the amount to convert: "))

    # Perform the conversion
    converted_amount = c.convert(from_currency, to_currency, amount)

    # Display the result
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    currency_converter()
