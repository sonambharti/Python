'''
# Q2. Construct the Minimum Bitwise Array II

You are given an array nums consisting of n prime integers.

You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and 
ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].

Additionally, you must minimize each value of ans[i] in the resulting array.

If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.

Example 1:

Input: nums = [2,3,5,7]

Output: [-1,1,4,3]

Explanation:
For i = 0, as there is no value for ans[0] that satisfies ans[0] OR (ans[0] + 1) = 2, so ans[0] = -1.
For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 3 is 1, because 1 OR (1 + 1) = 3.
For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 5 is 4, because 4 OR (4 + 1) = 5.
For i = 3, the smallest ans[3] that satisfies ans[3] OR (ans[3] + 1) = 7 is 3, because 3 OR (3 + 1) = 7.

Example 2:

Input: nums = [11,13,31]

Output: [9,12,15]

Explanation:
For i = 0, the smallest ans[0] that satisfies ans[0] OR (ans[0] + 1) = 11 is 9, because 9 OR (9 + 1) = 11.
For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 13 is 12, because 12 OR (12 + 1) = 13.
For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 31 is 15, because 15 OR (15 + 1) = 31.

Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
'''


def minBitwiseArray(nums):
    """
    Explaination of this approach: Let's, y = nums[i]
    For y = 5:
    (x | (x + 1)) = (100 | (100 + 1)) = (100 | 101) = 101
    {means, adding 1 in any binary no. is from right hand
    till we get 1st zero, each bit will be flipped.
    Then, y will have the binary value where each bit will be flipped 
    till we get 1st 1 from the right.
    }
    Now, taking it in reverse way:
    In this case possible x value can be any binary value where we can 
    flip any one of the consecutive 1's from y. (i.e. unset the set bit).
    So to select the minm, choose the one with MSB 0 bit.
    """
    
    # Initialize the result array
    n = len(nums)
    ans = []

    for i in range(n):
        if nums[i] == 2:
            ans.append(-1)
            continue
        for x in range(1, 31): # traversing through each bit of the number nums[i]
            if (nums[i] & (1 << x)):
                continue
            ans.append(nums[i] ^ (1 << (x - 1))) # using bitwise XOR
            break

    return ans
                    
            
    
if __name__ == "__main__":
    nums = [2,3,5,7]
    print(minBitwiseArray(nums))
