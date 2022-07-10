"""
Pascal's Triangle:

             1
           1 2 1
          1 3 3 1
         1 4 6 4 1
"""

n = int(input("Enter the size of triangle: "))

for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
 
    # first element is always 1
    C = 1
    for j in range(1, i+1):
 
        # first value in a line is always 1
        print(' ', C, sep='', end='')
 
        # using Binomial Coefficient
        C = C * (i - j) // j
    print()
