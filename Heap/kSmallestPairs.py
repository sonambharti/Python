'''
373. Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: 
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: 
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

'''

import heapq

def kSmallestPairs(nums1, nums2, k):
    priorityQ = []
    result = []
    n = len(nums1)
    m = len(nums2)

    visited = [[False] * m for _ in range(n)]
    heapq.heappush(priorityQ,(nums1[0] + nums2[0],(0, 0)))
    visited[0][0] = True

    while (k > 0 and priorityQ):
        # Pop the smallest pair
        current_sum, cords = heapq.heappop(priorityQ)
        
        i = cords[0]
        j = cords[1]
        # Append the corresponding pair to the result
        result.append([nums1[i], nums2[j]])

        # push (i, j+1) if possible
        if(j+1 < m and not visited[i][j+1]):
            heapq.heappush(priorityQ, (nums1[i]+nums2[j+1], (i, j+1)))
            visited[i][j+1] = True

        # push (i+1, j) if possible
        if(i+1 < n and not visited[i+1][j]):
            heapq.heappush(priorityQ, (nums1[i+1]+nums2[j], (i+1, j)))
            visited[i+1][j] = True
        
        k -= 1
            

    return result


def optimized_kSmallestPairs(nums1, nums2, k):
    # Initialize the min heap
    min_heap = []
    
    # Populate the initial heap with pairs involving the first element of nums1 and all elements of nums2
    # The heap will store tuples of the form (sum, index1, index2)
    for i in range(min(k, len(nums1))):  # Only need to consider at most k elements from nums1
        heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
    
    # print(min_heap)
    result = []
    
    # Extract the smallest pairs from the heap
    while min_heap and len(result) < k:
        # Pop the smallest pair
        current_sum, i, j = heapq.heappop(min_heap)
        # print(f"current_sum = {current_sum}, i = {i}, j = {j}")
        
        # Append the corresponding pair to the result
        result.append([nums1[i], nums2[j]])
        
        # If there's a next element in nums2, push the next pair involving nums1[i] and nums2[j+1] into the heap
        if j + 1 < len(nums2):
            heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
    
    return result



# Example usage:
if __name__ == "__main__":
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    print(f"Return the {k} pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums:\n", kSmallestPairs(nums1, nums2, k))
    
    print(f"Return the {k} pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums:\n", optimized_kSmallestPairs(nums1, nums2, k))
