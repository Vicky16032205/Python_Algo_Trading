"""
You have a list of stock symbols and their corresponding prices. Use list comprehension to create a list of tuples for only those stocks with prices over $1000, and sort this list by price in descending order
"""


stock_symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
stock_prices = [175.64, 2835.23, 299.35, 3450.16]

list = list(zip(stock_symbols, stock_prices))

tuple = [item for item in list if item[1] > 1000]
tuple.sort(key=lambda x : x[1], reverse= True)

print(tuple)