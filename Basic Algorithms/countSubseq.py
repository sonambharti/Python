#print count of the subseq of a given array

count = 0
def subseq(indx, n, arr, lst):
    global count
    if(indx == n):
        #print(lst)
        count += 1
        return
    
    lst.append(arr[indx])
    subseq(indx+1, n, arr, lst)
    lst.remove(arr[indx])
    #lst.pop()
    subseq(indx+1, n, arr, lst)
    
    return count

if __name__ == '__main__':
	n = int(input("Input size of array: "))
	arr = []
	for i in range(n):
	    ele = int(input())
	    arr.append(ele)
	lst = []
	res = subseq(0, n, arr, lst)
	print(res)
	
