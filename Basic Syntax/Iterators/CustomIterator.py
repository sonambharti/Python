"""
Here's the difference between __iter__() and __next__() in Python:

🔁 __iter__()
Purpose: Returns the iterator object itself.
Who uses it: Called when an iteration is started, e.g., by iter(obj) or in a for loop.
Requirement: Must be implemented for an object to be iterable.

🔄 __next__()
Purpose: Returns the next item in the sequence.
Who uses it: Called repeatedly by the iterator protocol or next(obj) until StopIteration is raised.
Requirement: Must be implemented by any iterator.
"""


class Counter:
    def __init__(self, max_val):
        self.max_val = max_val
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_val:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

c = Counter(3)
for num in c:
    print(num)  # Outputs: 1 2 3
