#Find if No. is power of 2 or not

def solve(n):
    # CODE HERE
    if(n == 0):
        return 0
    while(n!=1):
        if(n%2 != 0):
            return 0;
        n = n//2
    return 1
  
if __name__ == '__main__':
	n = int(input("Enter the number: "))
	ans = solve(n)
	print(ans)
