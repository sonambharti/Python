def solve(n, arr, key):
    # CODE HERE
    f = 0
    l = n-1

    if arr[0] > key:
        return 0
        
    while(f <= l):
        mid = (f + l)//2
        if(arr[mid] == key):
            return mid
        elif(arr[mid] > key):
            l = mid - 1
        elif(arr[mid] < key):
            f = mid + 1
    
    if(arr[mid] < key):
        return (mid + 1)
    else:
        return mid


    
        


if __name__ == '__main__':
	n = int(input())
	arr = []
  for i in range(n):
    ele = int(input())
    arr.append(ele)
	key = int(input())
	res = solve(n, arr, key)
	print(res)
