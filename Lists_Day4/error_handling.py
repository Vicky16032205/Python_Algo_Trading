"""
Question: Attempt to access the 10th element of a list that contains only 5 elements. Use exception handling to manage the potential IndexError and print a custom error message.
"""

arr_list = [1,2,3,4,5]

try:
    ele = arr_list[10]
    print(ele)
except IndexError as e:
    print("Error occured:", e)
finally:
    print("Error Handling carefully implemented")