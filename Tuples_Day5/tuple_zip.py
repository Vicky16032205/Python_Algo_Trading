"""
Question: You have two lists of stock prices at different times. Use zip() to create tuples paired by their indices and print those stocks where the price has increased.
"""

symbols = ['AAPL', 'GOOG', 'MSFT', 'TSLA', 'AMZN']
prices_time1 = [190.5, 2750.0, 320.2, 700.0, 3400.0]
prices_time2 = [191.0, 2745.0, 322.5, 705.0, 3395.0]

tuple1 = tuple(zip(symbols , prices_time1))
tuple2 = tuple(zip(symbols , prices_time2))

print("Ascending sorting on tuple1 ",sorted(tuple1, key=lambda x:x[1]))
print("Ascending sorting on tuple2 ",sorted(tuple2, key=lambda x:x[1]),"\n")


print("Descending sorting on tuple1 ",sorted(tuple1, key=lambda x:x[1], reverse=True))
print("Descending sorting on tuple2 ",sorted(tuple2, key=lambda x:x[1], reverse=True))
