"""
Question: You receive data in the form of a list of tuples where each tuple contains a stock symbol, its opening price, and its closing price. Calculate the daily change for each stock using tuple unpacking.
"""

stock_data = [
    ('AAPL', 190.0, 193.5),
    ('GOOG', 2750.0, 2745.0),
    ('MSFT', 320.0, 322.5),
    ('TSLA', 700.0, 705.0),
    ('AMZN', 3400.0, 3395.0),
]

print([(stock, closing_price - open_price) for stock, open_price, closing_price in stock_data])