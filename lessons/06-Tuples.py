"""
Tuples
- Tuples are immutable lists.
- Tuples are used to store data that is not going to be changed.
- It is denoted by ()
"""

# create a tuple
tuple1 = (1, 2, 3, 4, 5)

print(tuple1)

print( tuple1[:3])

# tuple1[0] = 10

#returns the number of occurence of an item in a tuple
print( tuple1.count(10) )

#returns the index of an item in a tuple
print( tuple1.index(1) )

