"""
Given two lists, stock_symbols and stock_prices, use the zip() function to pair each stock with its price in a dictionary. Then print each pair
"""

stock_symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
stock_prices = [175.64, 2835.23, 299.35, 3450.16]

print(list(zip(stock_symbols, stock_prices)))