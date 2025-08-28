"""
You have a list of current holdings in your portfolio. Add new stocks at the end, a list of upcoming stocks in the middle, and a special stock at the beginning

"append" adds element at the last position of the list
"extends" adds elements at any position in-between as classified
"insert" adds element at the starting position of the list
"""

holding_price = [150.5, 320.0, 87.75, 245.3, 410.2, 99.9, 275.0, 180.6, 305.4, 210.8]

print("Original ",holding_price)
holding_price.append(500.5)
print(holding_price)
holding_price.extend([899])
print(holding_price)
holding_price.insert(0,192.5)
print(holding_price)
