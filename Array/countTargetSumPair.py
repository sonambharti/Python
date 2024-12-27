'''
# Count pairs with given sum

Given an array arr[] and an integer target. You have to find numbers of pairs in array arr[] 
which sums up to given target.

Examples:

Input: arr[] = [1, 5, 7, -1, 5], target = 6 
Output: 3
Explanation: Pairs with sum 6 are (1, 5), (7, -1) and (1, 5). 

Input: arr[] = [1, 1, 1, 1], target = 2 
Output: 6
Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).

Input: arr[] = [10, 12, 10, 15, -1], target = 125
Output: 0
'''

def countPairs(arr, target):
    #Your code here
    d = {}
    total_pairs = 0
    for i in arr:
        r = target - i
        total_pairs += d.get(r, 0)
        d[i] = d.get(i, 0) + 1
    return total_pairs

    
if __name__ == "__main__":
    arr = [1, 5, 7, -1, 5]
    target = 8
            
    print("Count pairs with given sum: ", countPairs(arr, target))
    
