'''
# Minimum Jumps

Given an array arr[] of non-negative integers. Each array element represents the maximum 
length of the jumps that can be made forward from that element. This means if arr[i] = x, 
then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array starting from the first 
element. If an element is 0, then you cannot move through that element.
Note:  Return -1 if you can't reach the end of the array.

Examples : 

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 
Explanation:First jump from 1st element to 2nd element with value 3. From here we jump to 
5th element with value 9, and from here we will jump to the last. 
Input: arr = {1, 4, 3, 2, 6, 7}
Output: 2 
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.
Input: arr = {0, 10, 20}
Output: -1
Explanation: We cannot go anywhere from the 1st element.


'''

def minJumps(arr):
    #code here
    n = len(arr)
    jump = 1
    max_reach = arr[0]
    step = arr[0]
    
    if n == 1:
        return 0
    
    elif arr[0] == 0:
        return -1
    
    else:
        for i in range(1, n):
            if i == n-1:
                return jump
            max_reach = max(max_reach, i+arr[i])
            step -= 1
            if step == 0:
                jump += 1
                if i>=max_reach :
                    return -1
                step = max_reach-i
                    
if __name__ == "__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    
    print("Minimum no of jumps to reach the end of the array: ", minJumps(arr))

