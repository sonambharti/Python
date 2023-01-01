# print all possible unique subset using for loop...

def subseq(indx, arr, lst, res):
    res.append(lst.copy())
    #res.append(list(lst))
    for i in range(indx,len(arr)):
        if(i != indx and arr[i] == arr[i-1]):
            continue
        lst.append(arr[i])
        subseq(i+1, arr, lst, res)
        #lst.remove(arr[i])
        lst.pop()
    

if __name__ == '__main__':
    
    n = int(input("Input size of array: "))
    arr = []
    for i in range(n):
        ele = int(input())
        arr.append(ele)
    lst = []
    res = []
    arr.sort()
    subseq(0, arr, lst, res)
    print(res)
