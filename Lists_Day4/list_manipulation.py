"""
Given a list with stock prices, delete prices that are exactly $100, and replace the last three elements with their mean.
"""

stock_prices = [95, 100, 102, 99, 100, 105, 110, 100, 120, 115]

print("Original list: " ,stock_prices)

stock_prices = [item for item in stock_prices if item != 100]

mean = sum(stock_prices[-3:])/3

stock_prices[-3:] = [mean]*3

print("Modified list: ",stock_prices)