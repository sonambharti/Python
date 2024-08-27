'''
# Maximum Difference

Given an integer array arr of integers, the task is to find the maximum absolute difference 
and the nearest right smaller element of every element in array arr. If for any component of
the arr, the nearest smaller element doesn't exist then consider it as 0.

Examples :

Input: arr = [2, 1, 8]
Output: 1
Explanation: left smaller array ls = [0, 0, 1], right smaller array rs = [1, 0, 0]. Maximum Diff of 
abs(ls[i] - rs[i]) = 1
Input: arr = [2, 4, 8, 7, 7, 9, 3]
Output: 4
Explanation: left smaller array ls = [0, 2, 4, 4, 4, 7, 2], right smaller rs = [0, 3, 7, 3, 3, 3, 0]. 
Maximum Diff of abs(ls[i] - rs[i]) = abs(7 - 3) = 4
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

'''
def findMaxDiff(arr):
    # code here
    n = len(arr)
    ls = [-1]*n
    rs = [-1]*n
    st = []
    # For left smaller
    for i in range(0, n):
        while len(st) > 0 and st[-1] >= arr[i]:
            st.pop()
        # if st:
        #     ls[i] = st[-1]
        # else:
        #     ls[i] = 0
        ls[i] = 0 if len(st) == 0 else st[-1]
        st.append(arr[i])
    
    # Free Memory used
    while len(st) > 0:
        st.pop()
        
    # For right smaller
    for i in range(n-1, -1, -1):
        while len(st) > 0 and st[-1] >= arr[i]:
            st.pop()
        if st:
            rs[i] = st[-1]
        else:
            rs[i] = 0
        st.append(arr[i])
        
    # print(ls)
    # print(rs)
    
    ans = -float('infinity')
    
    for i in range(n):
        ans = max(ans, abs(ls[i]-rs[i]))
    return ans
    

if __name__ == "__main__":
    arr = [2, 1, 8]
    res = findMaxDiff(arr)
    print("The maximum absolute difference and the nearest right smaller element: ", res)

