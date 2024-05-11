"""
Given an array arr[ ] of length N consisting cost of N toys and an integer K 
depicting the amount with you. Your task is to find maximum number of toys 
you can buy with K amount. 

Example 1:

Input: 
N = 7 
K = 50
arr[] = {1, 12, 5, 111, 200, 1000, 10}
Output: 4
Explaination: The costs of the toys 
you can buy are 1, 12, 5 and 10.
"""

def max_toys(arr, K):
    arr.sort()  # Sort the array in non-decreasing order
    max_toys = 0
    amount_spent = 0

    # Iterate through the sorted array and buy toys until the amount spent exceeds K
    for toy_cost in arr:
        if amount_spent + toy_cost <= K:
            amount_spent += toy_cost
            max_toys += 1
        else:
            break

    return max_toys



if __name__ == "__main__":
    # Example usage:
    arr = [1, 12, 5, 111, 200, 1000, 10]
    K = 50
    print(max_toys(arr, K))  # Output: 4
