"""
A simple Python3 program
to calculate Euler's
Totient Function
"""

# Function to return gcd of a and b
def gcd(a, b):

	if (a == 0):
		return b
	return gcd(b % a, a)

# A simple method to evaluate Euler Totient Function
def phi(n):

	result = 1
	for i in range(2, n):
		if (gcd(i, n) == 1):
			result+=1
	return result

# Driver Code
print("Find Euler Totient Function of any integer n....")
n=int(input("Enter value of n: "))
print("phi(",n,")= ",phi(n))