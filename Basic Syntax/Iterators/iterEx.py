"""
In Python, an iterator is an object that allows you to traverse through all the elements of a collection (like a list or tuple), 
one element at a time.

Key Concepts:
Iterable: Any Python object capable of returning its elements one at a time (like lists, tuples, strings, sets, etc.).
Iterator: An object with two key methods:
__iter__() — returns the iterator object itself.
__next__() — returns the next value from the iterable. Raises StopIteration when no more items.
"""

# A list is an iterable
nums = [1, 2, 3]

# Convert to an iterator
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # Raises StopIteration
