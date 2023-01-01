#Reverse an array using recursion

def revers(arr, l, r):
    
    if l >= r:
        return
    
    arr[l], arr[r] = arr[r], arr[l]
    revers(arr, l+1, r-1)
        
        
    
    
arr = [1, 2, 3, 4, 5, 6, 7]
revers(arr, 0, 6)
print(arr)
