import requests

API_KEY = 'your_api_key'  # Replace with your financial API key
BASE_URL = 'https://www.alphavantage.co/query'

def fetch_stock_price(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    time_series = data.get('Time Series (1min)')
    if not time_series:
        return None
    latest_time = sorted(time_series.keys())[0]
    return float(time_series[latest_time]['1. open'])

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, shares):
        if symbol in self.stocks:
            self.stocks[symbol] += shares
        else:
            self.stocks[symbol] = shares

    def remove_stock(self, symbol, shares):
        if symbol in self.stocks:
            self.stocks[symbol] -= shares
            if self.stocks[symbol] <= 0:
                del self.stocks[symbol]

    def get_portfolio_value(self):
        total_value = 0
        for symbol, shares in self.stocks.items():
            price = fetch_stock_price(symbol)
            if price:
                total_value += price * shares
        return total_value

    def display_portfolio(self):
        for symbol, shares in self.stocks.items():
            print(f"{symbol}: {shares} shares")

def main():
    portfolio = Portfolio()
    while True:
        action = input("Enter action (add, remove, view, value, quit): ").strip().lower()
        if action == 'add':
            symbol = input("Enter stock symbol: ").strip().upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)
        elif action == 'remove':
            symbol = input("Enter stock symbol: ").strip().upper()
            shares = int(input("Enter number of shares: "))
            portfolio.remove_stock(symbol, shares)
        elif action == 'view':
            portfolio.display_portfolio()
        elif action == 'value':
            value = portfolio.get_portfolio_value()
            print(f"Total portfolio value: ${value:.2f}")
        elif action == 'quit':
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
