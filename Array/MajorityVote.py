"""
# Majority Vote 

You are given an array of integer nums[] where each number represents a vote to a candidate. Return 
the candidates that have votes greater than one-third of the total votes, If there's not a majority 
vote, return -1. 

Examples:

Input: nums = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.
Input: nums = [1, 2, 3, 4, 5]
Output: [-1]
Explanation: no candidate occur more than n/3 times.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

"""

'''
You can solve this problem using Boyer-Moore Voting Algorithm (an optimized algorithm for finding 
majority elements):

Candidate Selection Phase: First, select two potential majority candidates by iterating through 
the list. Use two counters to track these candidates.
Validation Phase: Verify whether these two candidates actually appear more than n/3 times in the list.


# Code Explanation:

Step 1: Candidate Selection:
We are looking for at most two candidates that can appear more than n/3 times.
We maintain two candidates and two counters, and update them based on the elements in the array.
Step 2: Validation:
Once two candidates are found, count their occurrences in a second pass over the array to confirm if
they really appear more than n/3 times.
'''

def findMajority(nums):
    #Your Code goes here.
    if not nums:
        return [-1]
    
    # Step 1: Find two potential candidates
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0
    
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    
    # Step 2: Validate candidates
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    
    n = len(nums)
    res = []
    
    if count1 > n // 3:
        res.append(candidate1)
    if count2 > n // 3:
        res.append(candidate2)
    
    return res if res else [-1]
    
    
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    ans = findMajority(arr)
    print("The resultant arr: ", ans)
    
    
    
    
    
