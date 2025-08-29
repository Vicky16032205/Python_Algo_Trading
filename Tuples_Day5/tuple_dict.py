"""
Question: You receive real-time market data in the form of tuples (symbol, price, volume). Store these tuples in a dictionary where the key is the symbol and the value is a list of tuples containing price and volume. Update the dictionary with new data and maintain only the last three entries per stock.
"""


market_data = [
    ('AAPL', 190.5, 1000),
    ('GOOG', 2750.0, 500),
    ('AAPL', 191.0, 1200),
    ('MSFT', 320.2, 800),
    ('AAPL', 192.3, 900),
    ('GOOG', 2752.5, 600),
    ('AAPL', 193.1, 1100),
    ('MSFT', 321.0, 700),
    ('GOOG', 2755.0, 550),
    ('MSFT', 322.5, 650),
]

tuple_dict = {}

for item in market_data:
    key = item[0]
    value = (item[1], item[2])

    if key not in tuple_dict:
        tuple_dict[key] = []
    tuple_dict[key].append(value)
    tuple_dict[key] = tuple_dict[key][-3:]

print(tuple_dict)