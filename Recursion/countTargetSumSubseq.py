#print count of the subseq for target sum of a given array using recursion
def subseq(indx, n, arr, tsum, sum):
    if(indx == n):
        if(sum == tsum):
            #print(lst)
            return 1
        else:
            return 0
    
    
    
    sum += arr[indx]
    l = subseq(indx+1, n, arr, tsum, sum) 
    sum -= arr[indx]
    
    r = subseq(indx+1, n, arr, tsum, sum)
       
    res = l+r
    return res

if __name__ == '__main__':
	n = int(input("Input size of array: "))
	arr = []
	for i in range(n):
	    ele = int(input())
	    arr.append(ele)
	lst = []
	tsum = int(input())
	res = subseq(0, n, arr, tsum, 0)
	print(res)
	
