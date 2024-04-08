"""
403. Frog Jump ----> Leetcode

A frog is crossing a river. The river is divided into some number of units, 
and at each unit, there may or may not exist a stone. The frog can jump on 
a stone, but it must not jump into the water.

Given a list of stones positions (in units) in sorted ascending order, determine 
if the frog can cross the river by landing on the last stone. Initially, the frog
is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. 
The frog can only jump in the forward direction.

 

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, 
then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
"""

def canCross(stones):
    # Create a set to store the positions of stones for quick lookup
    stone_set = set(stones)
    # Create a dictionary to store the possible jumps for each stone
    dp = {}
    # Iterate through the stones and initialize the possible jumps for each stone
    for stone in stones:
        dp[stone] = set()
    dp[0].add(0)  # The frog starts at position 0 with initial jump 0
    
    # Iterate through the stones and check if the frog can reach the next stones
    for stone in stones:
        for k in dp[stone]:
            for next_k in [k - 1, k, k + 1]:
                if next_k > 0 and stone + next_k in stone_set:
                    dp[stone + next_k].add(next_k)
                    
    # print(dp[stones[-1]])
    
    # If the frog can reach any position of the last stone, return True
    return bool(dp[stones[-1]])
    
    
if __name__ == "__main__":
    stones = [0,1,3,5,6,8,12,17]
    res = canCross(stones)
    print("if the frog can cross the river by landing on the last stone or not: ", res)
    
    
