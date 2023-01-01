def solve(n):
  # CODE HERE
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return solve(n-1)+solve(n-2)

   

if __name__ == '__main__':
	n = int(input())
	out = solve(n)
	print(out)
