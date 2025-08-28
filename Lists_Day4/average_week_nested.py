"""
You have a list of lists where each sublist contains stock symbols followed by their daily closing prices over a week. Create a flattened list of symbols paired with their average weekly price.
"""

stock_data = [
    ["AAPL", 172.5, 174.0, 173.2, 175.1, 176.0],
    ["GOOGL", 2820.0, 2835.5, 2840.2, 2830.0, 2825.7],
    ["MSFT", 299.1, 300.5, 301.0, 298.7, 299.9],
    ["TSLA", 720.0, 725.5, 730.2, 728.0, 726.5]
]

res = []
for item in stock_data:
    avg = sum(item[1:]) / len(item[1:])
    res.append([item[0], round(avg,2)])

print(res)