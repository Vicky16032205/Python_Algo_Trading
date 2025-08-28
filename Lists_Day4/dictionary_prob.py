"""
Pair each stock with its respective price using zip and then convert this list of pairs into a dictionary where stock symbols are keys and values are lists containing current price and a Boolean indicating if the price is over $150.
"""

stocks = ["AAPL", "GOOGL", "MSFT", "TSLA"]
prices = [176.0, 2825.7, 299.9, 726.5]

zip_list = list(zip(stocks, prices))

dictionary = {}

for item in zip_list:
    key = item[0]
    price = item[1]
    dictionary[key] = [price, price>1500]

print(dictionary)