"""
Print first negative from the K window of an array. And. if there is 
no negative number in a particular window then return 0 for that window.

Example:
Input:
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3 

Output: [-1, -1, -7, -15, -15, 0]
"""

def brute_force_firstNegNo(arr, k):
    res = []
    n = len(arr)
    for i in range(n-k+1):
        sub_arr = arr[i:i+k]
        j = 0
        count = 0
        while j < k:
            if sub_arr[j] < 0:
                res.append(sub_arr[j])
                break
            else:
                count += 1 
            j+=1 
        if count == k:
            res.append(0)
    return res 
    
if __name__ == "__main__":
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3 
    res = brute_force_firstNegNo(arr, k)
    print("Array of first negatives in the window: ", res)
