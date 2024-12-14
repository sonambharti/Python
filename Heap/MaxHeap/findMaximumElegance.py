'''

# Maximum Elegance of K-length Subsequence

You are given a 0-indexed 2D integer array items of length n and an integer k.

items[i] = [profiti, categoryi], where profit_i and category_i denote the profit and category
of the ith item respectively.

Let's define the elegance of a subsequence of items as total_profit + distinct_categories2,
where total_profit is the sum of all profits in the subsequence, and distinct_categories is 
the number of distinct categories from all the categories in the selected subsequence.

Your task is to find the maximum elegance from all subsequences of size k in items.

Return an integer denoting the maximum elegance of a subsequence of items with size exactly k.

Note: A subsequence of an array is a new array generated from the original array by deleting some
elements (possibly none) without changing the remaining elements' relative order.

 

Example 1:

Input: items = [[3,2],[5,1],[10,1]], k = 2
Output: 17
Explanation: In this example, we have to select a subsequence of size 2.
We can select items[0] = [3,2] and items[2] = [10,1].
The total profit in this subsequence is 3 + 10 = 13, and the subsequence contains 2 distinct categories [2,1].
Hence, the elegance is 13 + 22 = 17, and we can show that it is the maximum achievable elegance. 

Example 2:

Input: items = [[3,1],[3,1],[2,2],[5,3]], k = 3
Output: 19
Explanation: In this example, we have to select a subsequence of size 3. 
We can select items[0] = [3,1], items[2] = [2,2], and items[3] = [5,3]. 
The total profit in this subsequence is 3 + 2 + 5 = 10, and the subsequence contains 3 distinct categories [1,2,3]. 
Hence, the elegance is 10 + 32 = 19, and we can show that it is the maximum achievable elegance.

Example 3:

Input: items = [[1,1],[2,1],[3,1]], k = 3
Output: 7
Explanation: In this example, we have to select a subsequence of size 3. 
We should select all the items. 
The total profit will be 1 + 2 + 3 = 6, and the subsequence contains 1 distinct category [1]. 
Hence, the maximum elegance is 6 + 12 = 7.  

'''

from collections import defaultdict
from heapq import *


def findMaximumElegance(items, k):
    n = len(items)
    items = sorted(items, key=lambda x : -x[0])
    t_sum = 0
    d = defaultdict()
    heap = []

    #calculating for top k (top k profit, same category element maybe there).
    for i in range(k):
        t_sum += items[i][0]
        d[items[i][1]] = d.get(items[i][1], 0) + 1
        heappush(heap, items[i])
    ans = t_sum + len(d)**2

    for i in range(k, n):
        #a bigger profit element of same category is aready in heap.
        if items[i][1] in d:
            continue
            
        #pop element which is only element of that catgory so dont  subtract it from t_sum because it may be part of soluition.
        while heap and d[heap[0][1]]==1:
            heappop(heap)

        #multiple elements belongs to same category so we can remove least of them and add new category element to increate profit.
        if heap:
            profit,idx=heapq.heappop(heap)
            d[idx]-=1
            t_sum+=items[i][0]-profit
            d[items[i][1]]=1
            ans=max(ans,t_sum+len(d)**2)
        # nothing to replace in heap so cant get beter then previous profits
        else: 
            break
    return ans
    
if __name__ == "__main__":
    items = [[1,1],[2,1],[3,1]]
    k = 3
    
    res = findMaximumElegance(items, k)
    print(res)

