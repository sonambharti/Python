"""
Power set is a collection of all subsets, empty set and the original set itself.
Cardinalituy of PowerSet = 2**n, wher n = no. of elements.
"""

def powerset(indx, arr, lst, res):
    res.append(lst.copy())
    for i in range(indx, len(arr)):
        if(i<=indx and arr[i] == arr[i-1]):
            continue
        lst.append(arr[i])
        subset(i+1, arr, lst, res)
        lst.pop()
        
        
indx = 0
arr = ['a', 's', 'd', 'f']
lst = []
res = []
powerset(indx, arr, lst, res)
print(len(res))
