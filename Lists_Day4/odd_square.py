"""
Question: Using a list of numbers, create a new list that contains the square of each number, but only if the number is odd.
"""

orig_list = [1,2,3,4,5,6,7,8,9,10]
print([num**2 for num in orig_list if num%2 != 0])