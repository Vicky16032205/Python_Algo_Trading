"""
Using list comprehension, create a list of booleans indicating whether each stock price in the list is above 100.
"""

initial_prices = [150.5, 320.0, 87.75, 245.3, 410.2, 99.9, 275.0, 180.6, 305.4, 210.8]

print(["True" if item>200 else "False" for item in initial_prices])