"""
Print possible unique subseq of a list to get a target sum
"""
res = []
def combSum(indx, target, lst, arr, n):
    global res
    if indx == n:
        if target == 0:
            #print(arr)
            res.append(arr.copy())
            
        return
        
    if lst[indx] <= target:
        arr.append(lst[indx])
        combSum(indx+1, target-lst[indx], lst, arr, n)
        arr.pop()
        
    combSum(indx+1, target, lst, arr, n)
     
 
 
if __name__ == "__main__":
    
    arr = []
    lst = [2, 3, 5, 4, 2]
    
    lst = set(lst)
    lst = list(lst)
    n = len(lst)
    combSum(0, 7, lst, arr, n)
    print(res)
    
