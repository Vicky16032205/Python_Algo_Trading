"""
Question: Given a list of strings representing transactions, parse each string into a tuple containing the type of transaction ('Buy' or 'Sell') and the amount, then filter out any transactions under $200.
"""

transactions = [
    "Buy 150",
    "Sell 300",
    "Buy 250",
    "Sell 100",
    "Buy 500",
    "Sell 180",
    "Buy 220",
    "Sell 450"
]

parsed_transactions = []
for item in transactions:
    t_type, amount = item.split(" ")
    amount = int(amount)
    if amount >= 200:
        parsed_transactions.append((t_type, amount))

print(parsed_transactions)


parse_transactions = [
    (t_type, int(amount)) for t_type, amount in (item.split(" ") for item in transactions) if int(amount) >= 200
]

print(parse_transactions)