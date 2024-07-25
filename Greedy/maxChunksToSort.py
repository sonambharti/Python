"""
# 768. Max Chunks To Make Sorted II
You are given an integer array arr.

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. 
After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Example 1:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.

"""

def max_chunks_to_sorted(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # Initialize the max_left and min_right arrays
    max_left = [0] * n
    min_right = [0] * n
    
    # Fill the max_left array
    max_left[0] = arr[0]
    # stores the maximum value from the start of the array to the index 'i'
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], arr[i])
    
    # Fill the min_right array
    min_right[n - 1] = arr[n - 1]
    # stores the minimum value from the index i to the end of the array.
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], arr[i])
    
    # Count the number of chunks
    count = 0
    # For each index i, if max_left[i] <= min_right[i + 1], it means you can make a partition after index i.
    for i in range(n - 1):
        if max_left[i] <= min_right[i + 1]:
            count += 1
    
    # Add the last chunk
    return count + 1


if __name__ == "__main__":
    # Example usage
    arr = [5, 4, 3, 2, 1]
    print("The largest number of chunks we can make to sort the array is:", max_chunks_to_sorted(arr))
