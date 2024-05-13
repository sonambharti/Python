"""
Count the elements -> GFG 
Given two arrays a and b both of size n. Given q queries in an array query each having a positive integer x denoting 
an index of the array a. For each query, your task is to find all the elements less than or equal to a[x] in the array b.

Example 1:

Input:
n = 3
a[] = {4,1,2}
b[] = {1,7,3}
q = 2
query[] = {0,1}
Output : 
2
1
Explanation: 
For 1st query, the given index is 0, a[0] = 4. There are 2 elements(1 and 3) which are less than or equal to 4.
For 2nd query, the given index is 1, a[1] = 1. There exists only 1 element(1) which is less than or equal to 1.
"""

def countElements_brute(a, b, n, query, q):
    # code here
    result = []
    for idx in query:
        count = sum(1 for num in b if num <= a[idx])
        result.append(count)
    return result
    

    
def countElements(a, b, n, query, q):
        # code here
        def binarySearchCount(arr, target):
            # Initialize count and binary search pointers
            count = 0
            left, right = 0, len(arr) - 1
            # Perform binary search
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] <= target:
                    count = mid + 1  # Include the current element
                    left = mid + 1   # Search in the right half
                else:
                    right = mid - 1  # Search in the left half
            return count
        
        result = []
        # Sort array b
        b.sort()
        # Perform binary search for each query
        for idx in query:
            count = binarySearchCount(b, a[idx])
            result.append(count)
        return result


if __name__ == "__main__":
  n = int(input("Enter size of arrays a & b: "))
  a = []
  b = []
  print(f"Enter element of a of size {n}: ")
  for i in range(n):
    el =  int(input())
    a.append(el)

  print(f"Enter element of b of size {n}: ")
  for i in range(n):
    el =  int(input())
    b.append(el)

  q = int(input("Enter size of querys: "))
  query = []
  print(f"Enter element of query of size {q}: ")
  for i in range(q):
    el =  int(input())
    query.append(el)

  res = countElements_brute(a, b, n, query, q)
  print("Printing results for the required query: ")
  for els in res:
    print(els)
    
  res1 = countElements(a, b, n, query, q)
  print("Printing results for the required query: ")
  for els1 in res1:
    print(els1)
