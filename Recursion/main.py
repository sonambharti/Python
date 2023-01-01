#print all permutations of a string/Array.....

def recurPermut(arr, lst, res, flag):
    if len(lst)==len(arr):
        res.append(lst.copy())
        #res.append(list(lst))
        return
    
    for i in range(0,len(arr)):
        if not flag[i]:
            flag[i] = True
            lst.append(arr[i])
            recurPermut(arr, lst, res, flag)
            #lst.remove(arr[i])
            lst.pop()
            flag[i] = False
    

if __name__ == '__main__':
    
    n = int(input("Input size of array: "))
    arr = []
    for i in range(n):
        ele = int(input())
        arr.append(ele)
    lst = []
    res = []
    flag = [False] * n
    arr.sort()
    recurPermut(arr, lst, res, flag)
    print(res)