"""
Question: Given a dictionary mapping stock symbols to their daily prices over a week, create a nested dictionary that maps each symbol to another dictionary of 'highest' and 'lowest' prices of the week.
"""


# Sample data: stock symbol -> list of daily prices for a week
weekly_prices = {
    'AAPL': [190.5, 192.0, 191.3, 193.1, 192.8, 194.0, 193.5],
    'GOOG': [2750.0, 2745.5, 2752.5, 2755.0, 2751.0, 2758.0, 2756.5],
    'MSFT': [320.2, 321.0, 322.5, 323.0, 321.8, 324.0, 323.5],
    'TSLA': [700.0, 705.0, 702.5, 707.0, 704.5, 709.0, 708.5],
    'AMZN': [3400.0, 3395.0, 3402.5, 3405.0, 3401.0, 3408.0, 3406.5],
}

result = {}

for symbol, prices in weekly_prices.items():
    high= max(prices)
    low= min(prices)
    result[symbol] = {'highest': high, 'lowest': low}

print(result)