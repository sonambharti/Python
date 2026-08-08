# sort an array using recursion
# T(n)=O(n^2)

def insert(arr, temp):
    n = len(arr)
    if n == 0 or arr[n-1] <= temp:
        arr.append(temp)
        return
    val = arr.pop()
    insert(arr, temp)
    arr.append(val)
            
def sortArr(arr):
    if len(arr)==1:
        return 
    temp = arr.pop()
    sortArr(arr)
    insert(arr, temp)
    
    
    
if __name__ == "__main__":
    arr = [2,7,3,5]
    sortArr(arr)
    print(arr)
