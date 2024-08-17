'''
Given an array of integers arr, return true if it is possible to split it in two subarrays 
(without reordering the elements), such that the sum of the two subarrays are equal. If it 
is not possible then return false.

Examples:

Input: arr = [1, 2, 3, 4, 5, 5]
Output: true
Explanation: In the above example, we can divide the array into two subarrays with eqaul sum. 
The two subarrays are: [1, 2, 3, 4] and [5, 5]. The sum of both the subarrays are 10. Hence, 
the answer is true.
Input: arr = [4, 3, 2, 1]
Output: false
Explanation: In the above example, we cannot divide the array into two subarrays with eqaul sum.
Hence, the answer is false.

'''

# 2 pointers approach

def canSplit_2pointers(arr):
    #code here
    n = len(arr)
    if n==1:
        return False
    if n==2:
        return arr[0]==arr[1]
        
    i, j = 1, n-2
    leftSum, rightSum = arr[0], arr[n-1]
    
    while i <= j:
        if leftSum < rightSum:
            leftSum += arr[i]
            i+=1
        else:
            rightSum += arr[j]
            j -= 1
    
    return leftSum==rightSum
    
    
# prefix-postfix 
def canSplit(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False
    else:
        pre_sum = 0
        post_sum = total_sum
        for i in range(0, len(arr)-1):
            pre_sum += arr[i]
            post_sum -= arr[i]
            if pre_sum == post_sum:
                return True
        return False
        
        
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 5]
    res = canSplit_2pointers(arr)
    print("sum of the two subarrays are equal or not: ", res)
