"""
From the given list of stock symbols, change the symbol 'GOOG' to 'GOOGL' and remove 'NFLX' from the list.
"""

list = ["Titan", "Larsen", "Coal India", "Maruti Suzuki", "Hero MotoCorp", "GOOG", "NFLX"]

print(list)
list[5] = "GOOGL"
list.remove("NFLX")
print(list)