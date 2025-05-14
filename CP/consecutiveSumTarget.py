"""
# Consecutive sum to target

Find if there is any subarray possible to get a target sum.
Example:
Input 1
arr = [1, 2, 3, 5, 2], target = 8, 
Output: True
Explanation: 3 + 5 = 8

"""
# Sliding Window Approach

def consecutiveSumTarget(arr, target):
    i, j = 0, 0
    summ = 0
    n = len(arr)
    while j < n:
        summ += arr[j]
        while summ > target and i <= j:
            summ -= arr[i]
            i += 1
        if summ == target:
            return True
        j += 1
    return False
  
  
if __name__ == "__main__":
  arr = [1,2,3,5,2]
  target = 8
  print("If consecutive sum to target is possible or not:", consecutiveSumTarget(arr, target))
