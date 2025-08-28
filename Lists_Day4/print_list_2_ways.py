"""
Demonstrate two ways to print each stock and its price from a list of tuples. The list is stocks = [('AAPL', 150), ('GOOG', 1200), ('MSFT', 200)]
"""

stocks = [('AAPL', 150), ('GOOG', 1200), ('MSFT', 200)]

print([item[0] for item in stocks])

items = []
for item in stocks:
    items.append(item[0])

print(items)