#print all the subsequence having given target sum usin recurence

count = 0
def subseq(indx, n, arr, lst, tsum, sum):
    global count
    if(indx == n):
        if(sum == tsum):
            print(lst)
            count += 1
        return
    
    lst.append(arr[indx])
    sum += arr[indx]
    subseq(indx+1, n, arr, lst, tsum, sum)
    sum -= arr[indx]
    lst.remove(arr[indx])
    #lst.pop()
    subseq(indx+1, n, arr, lst, tsum, sum)
    
    return count

if __name__ == '__main__':
	n = int(input("Input size of array: "))
	arr = []
	for i in range(n):
	    ele = int(input())
	    arr.append(ele)
	lst = []
	tsum = int(input("Input target sum:" ))
	res = subseq(0, n, arr, lst, tsum, 0)
	print(res)
	
