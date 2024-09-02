'''
# 40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

'''
    
def combinationSum2(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            res.append(list(path))
            return
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # Prune the recursion if the candidate is greater than the remaining target
            if candidates[i] > target:
                break
            # Include the candidate in the path and move forward
            path.append(candidates[i])
            backtrack(i + 1, target - candidates[i], path)
            # Backtrack
            path.pop()

    candidates.sort()
    res = []
    backtrack(0, target, [])
    return res
            

# Example usage:
if __name__ == "__main__":
    candidates = [2,5,2,1,2]
    target = 5
    print("All unique combinations in candidates where the candidate numbers sum to target: ", combinationSum2(candidates, target))
    
    
