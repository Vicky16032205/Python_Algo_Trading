"""
If you create a list a = [1, 2, 3] and then another list b = a, demonstrate what happens when you modify b and explain why.
"""

a= [1,2,3]
b=a
b.append(4)
print(a)

"This happens becuse lists are mutable and when trying to create new one from the previous one will refer to the same address where previous one is initialized and thus making changes in the new one will make changes to the previous one too."

"Professionally:"
"This happens because lists are mutable and assigning b = a does not create a new list, but makes b refer to the same list object as a. Therefore, changes made through b will also be reflected in a."