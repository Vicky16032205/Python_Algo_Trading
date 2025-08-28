"""
Process a list of stock transactions and exit the loop if a transaction exceeds 500, but skip any transaction below 100.
"""

transactions = [50, 120, 80, 200, 95, 300, 510, 150, 75, 400]

for item in transactions:
    if item>500:
        break
    elif item<100:
        continue
    else:
        print(item, end=" ")