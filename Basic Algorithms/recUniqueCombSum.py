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
    

"""
res = []
class Solution:
    def combSum(self, indx, target, lst, arr, n):
        global res
        if indx == n:
            if target == 0:
                #print(arr)
                if list(arr) not in res:
                    res.append(list(arr))
            return
            
        if lst[indx] <= target:
            arr.append(lst[indx])
            self.combSum(indx+1, target-lst[indx], lst, arr, n)
            arr.remove(arr[len(arr)-1])
            
        self.combSum(indx+1, target, lst, arr, n)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        global res
        res = []
        candidates.sort()
        n = len(candidates)
        self.combSum(0, target, candidates, arr, n)
        return res
    """
