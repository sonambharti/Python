'''
# Count Subarrays of Length Three With a Condition

Count subarrays of length three whose sum of the first and last element of subarray 
should be equal to the half of the middle element of the subarray.

'''
def count_valid_subarrays(nums):
    k = 3  # Subarray length
    n = len(nums)
    count = 0

    for i in range(n - k + 1):  # Iterate over all possible subarrays of length 3
        subArr = nums[i:i + k]
        if subArr[0] + subArr[2] == subArr[1] / 2:  # Use float division
            count += 1

    return count

# Example usage
if __name__ == "__main__":
    nums = [8, 4, 40, 16, 4, 8]
    print(count_valid_subarrays(nums))  # Output the count
