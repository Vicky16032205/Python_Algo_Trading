"""
Given a list of stock prices, create a new list that contains the price increased by 5% for only those prices that are below $200. Additionally, print the index of each modified price in the original list.
"""

initial_prices = [150.5, 320.0, 87.75, 245.3, 410.2, 99.9, 275.0, 180.6, 305.4, 210.8]

new_price = [item+item*.05 if item<200 else item for item in initial_prices]

print(new_price)
print([item if new_price[item] != initial_prices[item] else -1 for item in range(0,len(new_price))])