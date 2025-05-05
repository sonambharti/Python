"""
🔁 What Are Custom Iterators in Python?
A custom iterator is a user-defined class that implements the iterator protocol — meaning it must define two methods:

__iter__() — returns the iterator object itself.
__next__() — returns the next value or raises StopIteration.
✅ Use Case
You create a custom iterator when:

You want full control over how values are generated.
Your iteration needs state tracking between calls.
You want to model complex iteration behavior, like skipping, looping, filtering, etc.
"""

class CountDown:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self  # the object is its own iterator

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        current = self.num
        self.num -= 1
        return current


cd = CountDown(3)

for num in cd:
    print(num)

"""
Output:
3
2
1
"""
