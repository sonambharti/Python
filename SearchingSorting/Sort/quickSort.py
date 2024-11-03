"""
# Quick Sort 
"""
def quickSort(arr):
    if len(arr) <= 1:
        return arr
        
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    
    return quickSort(less) + [pivot] + quickSort(greater)
    
if __name__ == "__main__":
    arr = [4, 2, 8, 1, 6, 7]
    res = quickSort(arr)
    print("Sorted array is: ", res)
