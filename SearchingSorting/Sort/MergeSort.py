'''
# Merge Sort

Sort the given array using merge sort.

Example:

Input: n = 6, arr = [0, 2, 1, 5, 3, 4]
Output: [0, 1, 2, 3, 4, 5]


'''

def mergeSort(arr):
    # CODE HERE
    left = []
    right = []
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
    
    lptr = rptr = arrptr = 0
    
    while lptr < len(left) and rptr < len(right):
        if left[lptr] < right[rptr]:
            arr[arrptr] = left[lptr]
            lptr += 1
        else:
            arr[arrptr] = right[rptr]
            rptr += 1
        arrptr += 1 
    
    while lptr < len(left):
        arr[arrptr] = left[lptr]
        lptr += 1 
        arrptr += 1 
        
    while rptr < len(right):
        arr[arrptr] = right[rptr]
        rptr += 1 
        arrptr += 1 
        
        
if __name__ == '__main__':
	arr = list(map(int, input().split()))
	mergeSort(arr)
	print(arr)
