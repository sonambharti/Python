#print all susequence of an array using recurrsion

def subseq(indx, n, arr, lst):
    if(indx == n):
        print(lst)
        return
    
    lst.append(arr[indx])
    subseq(indx+1, n, arr, lst)
    lst.remove(arr[indx])
    #lst.pop()
    subseq(indx+1, n, arr, lst)


if __name__ == '__main__':
	n = int(input("Input size of array: "))
	arr = []
	for i in range(n):
	    ele = int(input())
	    arr.append(ele)
	lst = []
	subseq(0, n, arr, lst)
	
