"""
Given an array of integers, and an integer k. 
Find the maximum sum of  the array elements 
present in the subarray of array of k size. 

Example:
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4 
Output: 28
"""

def max_sum_bruteforce(arr, k):
    n = len(arr)
    if k > n:
        return "Invalid input: k is greater than the array length."

    max_sum = float('-inf')

    for i in range(n - k + 1):
        current_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, current_sum)

    return max_sum

def max_sum_sliding_window(arr, k):
    n = len(arr)
    if k > n:
        return "Invalid input: k is greater than the array length."

    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum   
    
if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 3
    result_bruteforce = max_sum_bruteforce(arr, k)
    print("Maximum Sum (Brute Force):", result_bruteforce)
    
    result_slidingWindow = max_sum_sliding_window(arr, k)
    print("Maximum Sum (sliding window):", result_slidingWindow)
