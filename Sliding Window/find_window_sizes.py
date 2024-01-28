"""
Given an array of integers, and a sum. 
Find the window sizes which contains the required 
sum of  the array elements present in the subarray of array. 

Example:
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4 
Output: 28
"""

def find_window_sizes_bruteforce(arr, target_sum):
    n = len(arr)
    window_sizes = []

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == target_sum:
                window_sizes.append((i, j))

    return window_sizes


def find_window_sizes_sliding_window(arr, target_sum):
    n = len(arr)
    window_sizes = []
    left = 0
    current_sum = 0

    for right in range(n):
        current_sum += arr[right]

        while current_sum > target_sum:
            current_sum -= arr[left]
            left += 1

        if current_sum == target_sum:
            window_sizes.append((left, right))

    return window_sizes
    

if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    target_sum = 12
    result_bruteforce = find_window_sizes_bruteforce(arr, target_sum)
    print("Window Sizes (Brute Force):", result_bruteforce)
    
    result_slidingWindow = find_window_sizes_bruteforce(arr, target_sum)
    print("Maximum Sum (sliding window):", result_slidingWindow)
