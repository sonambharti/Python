'''
# 1235. Maximum Profit in Job Scheduling

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i],
obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you 
can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that 
starts at time X.

 

Example 1:

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:

Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

'''

from typing import List, Tuple

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine the startTime, endTime, and profit into a list of tuples
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        
        # print("jobs = ", jobs)
        
        # Initialize dp array where dp[i] will store the maximum profit by considering jobs[0] to jobs[i]
        dp = [(0, 0)]  # Initial job with end time 0 and profit 0
        
        
        # Function to find the last job which doesn't conflict with the current job using binary search
        def binary_search(job_end_time: int) -> int:
            lo, hi = 0, len(dp) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if dp[mid][0] <= job_end_time:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo - 1
        
        for s, e, p in jobs:
            # Find the last job which doesn't conflict with the current job
            index = binary_search(s)
            current_profit = dp[index][1] + p
            # If the current job can increase the profit, add it to the dp array
            if current_profit > dp[-1][1]:
                dp.append((e, current_profit))
        
        return dp[-1][1]


if __name__ == "__main__":
    # Example usage:
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    sol = Solution()
    print(sol.jobScheduling(startTime, endTime, profit))  # Output: 120

