def solve(n):
  # CODE HERE
  a, b = 0, 1
  for i in range(n-1):
    c = a+b
    a = b
    b = c

  return b

if __name__ == '__main__':
	n = int(input())
	out = solve(n)
	print(out)
