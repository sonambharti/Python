'''
# Count distinct elements in every window

Given an integer array arr[] and a number k. Find the count of distinct elements in every window of 
size k in the array.

Examples:

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output:  [3, 4, 4, 3]
Explanation: Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.

Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]
Explanation: Window 1 of size k = 2 is 4 1. Number of distinct elements in this window are 2. 
Window 2 of size k = 2 is 1 1. Number of distinct elements in this window is 1. 

Input: arr[] = [1, 1, 1, 1, 1], k = 3
Output: [1, 1, 1]
'''
def countDistinct(arr, k):
    # Code here
    n = len(arr)
    res = []
    for i in range(n-k+1):
        subarr = arr[i:i+k]
        # print(subarr)
        setSub = set(subarr)
        res.append(len(setSub))
    return res
    
    
if __name__ == "__main__":
    # Input array
    arr = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    
    # Sorting the array
    res = countDistinct(arr, k)
    print("Count distinct elements in every window: ", res)
    
    
