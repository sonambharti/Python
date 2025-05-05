class Fibonacci:
    def __init__(self, limit):
        self.a, self.b = 0, 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        return val

fibo = Fibonacci(3)
for v in fibo:
    print(v)
