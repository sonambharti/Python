def solve(n, arr):
  # CODE HERE

  lst = []
    for i in arr:
        if i not in lst:
            lst.append(i)
	
  #set1 = set(arr)
  #lst = list(set1)

  if(len(lst) == n):
    return 0
  else:
    return 1

if __name__ == '__main__':
	n = int(input())
	for i in range(n):
	    ele = int(input())
	    arr.append(ele)
	
	res = solve(n, arr)
	print(res)
