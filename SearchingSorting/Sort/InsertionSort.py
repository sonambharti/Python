def InsertionSort(alist, n):
        #code here
    for wall in range(1,n):
        curr = alist[wall]
        pos_ptr = wall-1
        while(pos_ptr >= 0) and (curr < alist[pos_ptr]):
            alist[pos_ptr + 1] = alist[pos_ptr]
            pos_ptr -= 1
        alist[pos_ptr+1] = curr
    return alist
    
n = int(input("Enter size of array: "))
arr = []
print("Enter array element: ")
for i in range(n):
    ele = int(input())
    arr.append(ele)
    
res = InsertionSort(arr, n)
print(res)
