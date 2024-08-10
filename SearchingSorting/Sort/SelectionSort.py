class Solution: 
    def select(self, arr, i):
        # code here 
        n = len(arr)
        mini = i
      
        for curr in range(i+1,n):
            if(arr[curr] < arr[mini]):
                mini = curr
        return mini
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            min_indx = self.select(arr, i)
            arr[min_indx], arr[i] = arr[i], arr[min_indx]
            
        
            
            
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()

        
"""
def SelectionSort(arr):
    n = len(arr)
    
    for itr in range(n):
        min_indx = itr
        for curr in range(itr+1,n):
            if(arr[min_indx] > arr[curr]):
                min_indx = curr
        arr[min_indx], arr[itr] = arr[itr], arr[min_indx]
        
    return arr
    
n = int(input("Enter size of array: "))
arr = []
print("Enter array element: ")
for i in range(n):
    ele = int(input())
    arr.append(ele)
    
res = SelectionSort(arr)
print(res)
"""
