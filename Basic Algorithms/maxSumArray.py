# Python program to find maximum sum of contiguous subarray using Kaden's algorithm

from sys import maxint


def maxSubArraySum(a, size):

	maxmSum = -maxint - 1
	current_sum = 0

	for i in range(0, size):
		current_sum = current_sum + a[i]
		if (maxmSum < current_sum):
			maxmSum = current_sum

		if current_sum < 0:
			current_sum = 0
	return maxmSum

# Driver function to check the above function

if __name__ == "__main__":
  a = [-2, -3, 4, -1, -2, 1, 5, -3]
  
  print "Maximum contiguous sum is", maxSubArraySum(a, len(a))
