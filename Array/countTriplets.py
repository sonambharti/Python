'''
# Count all triplets with given sum in sorted array

Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, 
such that arr[i] + arr[j] + arr[k] = target and i < j < k.

Examples:

Input: arr[] = [-3, -1, -1, 0, 1, 2], target = -2
Output: 4
Explanation: Two triplets that add up to -2 are:
arr[0] + arr[3] + arr[4] = (-3) + 0 + (1) = -2
arr[0] + arr[1] + arr[5] = (-3) + (-1) + (2) = -2
arr[0] + arr[2] + arr[5] = (-3) + (-1) + (2) = -2
arr[1] + arr[2] + arr[3] = (-1) + (-1) + (0) = -2

Input: arr[] = [-2, 0, 1, 1, 5], target = 1
Output: 0
Explanation: There is no triplet whose sum is equal to 1. 

'''
# Using Hash
def countTriplets_hash(arr, target):
    # code here
    n = len(arr)
    if n<3:
        return 0
    count = 0
    
    for i in range(n - 2):
        rem = target - arr[i]
        freq = {}

        for j in range(i + 1, n):
            diff = rem - arr[j]
            if diff in freq:
                count += freq[diff]

            # freq[arr[j]] = freq.get(arr[j], 0) + 1
            if arr[j] not in freq:
                freq[arr[j]] = 1
            else:
                freq[arr[j]] += 1

    return count


# Using 2 pointer
def countTriplets_loop(arr, target):
    # code here
    n = len(arr)
    if n<3:
        return 0
    count = 0
    
    for i in range(n-2):
        k = n-1
        j = i+1
        while j < k:
            summ = arr[j] + arr[k] + arr[i]

            if summ == target:
                count += 1
                tk = k - 1
                tj = j + 1
                while tj < k and arr[tj] == arr[j]:
                    count += 1
                    tj += 1
                while tk > j and arr[tk] == arr[k]:
                    count += 1
                    tk -= 1
                j += 1
                k -= 1
                
            elif summ < target:
                j += 1
            
            else:
                k -= 1
    return count
    
if __name__ == "__main__":
    # Input array
    arr = [-3, -1, -1, 0, 1, 2]
    target = -2
    
    # Sorting the array
    res = countTriplets_hash(arr, target)
    print("Count all triplets with given sum in sorted array: ", res)
    print("Count all triplets with given sum in sorted array: ", countTriplets_loop(arr, target))
