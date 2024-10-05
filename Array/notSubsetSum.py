""" 
# Not a Subset sum

Given a sorted array arr[] of positive integers, find the smallest positive integer such 
that it cannot be represented as the sum of elements of any subset of the given array set.

Examples:

Input: arr[] = [1, 2, 3]
Output: 7
Explanation: 7 is the smallest positive number for which no subset is there with sum 7.
Input: arr[] = [3, 6, 9, 10, 20, 28]
Output: 1
Explanation: 1 is the smallest positive number for which no subset is there with sum 1.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)


"""

def findSmallest(arr):
    # code here
    ans = 1
    n = len(arr)
    for i in range(n):
        if arr[i] > ans:
            return ans
        else:
            ans += arr[i]
    return ans
        

if __name__ == "__main__":
    
    arr = [3, 6, 9, 10, 20, 28]
    res = findSmallest(arr)
    print("The smallest positive int which is not a Subset sum : ", res)
