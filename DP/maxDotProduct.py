"""
# Max Dot Product of 2 subsequences
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

 

Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.

"""
# Brute Force Approach
def maxDotProductBruteForce(nums1, nums2):
    # Define a recursive function to explore all possible subsequences
    def dotProduct(i, j):
        # Base case: if either i or j reaches the end of the array, return 0
        if i == len(nums1) or j == len(nums2):
            return 0
        # Calculate the dot product if we include nums1[i] and nums2[j]
        product_with_current = nums1[i] * nums2[j] + dotProduct(i + 1, j + 1)
        # Calculate the dot product if we skip nums1[i]
        product_without_current1 = dotProduct(i + 1, j)
        # Calculate the dot product if we skip nums2[j]
        product_without_current2 = dotProduct(i, j + 1)
        # Return the maximum dot product among all possibilities
        return max(product_with_current, product_without_current1, product_without_current2)
    
    # Start exploring all possible subsequences from the beginning of both arrays
    return dotProduct(0, 0)

# Dynamic Programming Approach
def maxDotProductDP(nums1, nums2):
    # Initialize a 2D DP array to store the maximum dot product for each prefix of nums1 and nums2
    dp = [[float('-inf')] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
    # Iterate through the arrays and calculate the maximum dot product using dynamic programming
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            # Calculate the dot product if we include nums1[i] and nums2[j]
            product_with_current = nums1[i] * nums2[j]
            # Update the maximum dot product for the current prefix
            dp[i + 1][j + 1] = max(product_with_current, product_with_current + dp[i][j], dp[i][j + 1], dp[i + 1][j])
    # The maximum dot product is at the bottom-right corner of the DP array
    return dp[len(nums1)][len(nums2)]


    

if __name__ == "__main__":
    # Example usage and comparison of approaches
    
    nums1 = [2, 3, -2, 4]
    nums2 = [3, -2, 1, -4]
    # Brute Force Approach
    print("Brute Force Approach:")
    print("Maximum dot product between non-empty subsequences:", maxDotProductBruteForce(nums1, nums2))
    # Dynamic Programming Approach
    print("Dynamic Programming Approach:")
    print("Maximum dot product between non-empty subsequences:", maxDotProductDP(nums1, nums2))
