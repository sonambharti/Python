"""
# Minimum number of steps to reach the target number

Find the minimum number of steps to reach the positive target number from either forward or backward.

Example:
Input 1
n = 5
Output: 5
Explanation: 1 - 2 - 3 + 4 + 5 = 5

Input 2
n = 6
Output: 3
Explanation: 1 + 2 + 3 = 6
"""

def reachNumber(target):
  steps = 0
  summ = 0
  while summ < target or (summ - target) % 2 != 0:
      steps += 1
      summ += steps
  return steps
  
if __name__ == "__main__":
  n = 6
  print("Minimum number of steps to reach the target number:", reachNumber(n))
