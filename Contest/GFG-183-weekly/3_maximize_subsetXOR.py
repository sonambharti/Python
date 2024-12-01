'''
# Subset XOR

Select a subset of integers from 1 to n (both inclusive), where each integer
can be chosen at most once, such that:
    - XOR of all elements in the subset is equat to n
    - size of the subset is maximized
    
if there are multiple subsets that satisfy these conditions, choose the subset 
that has the lexicographical smallest order

Examples:

Input: n = 4
Output: [1, 2, 3, 4]

Input: n = 3
Output: [1, 2]

Input: n = 2
Output: [2]


'''

def maximize_subset(n):
    # Start with an empty subset and a variable to track XOR
    subset = []
    current_xor = 0

    # Traverse numbers from 1 to n
    for i in range(1, n + 1):
        # Add the number to the subset
        subset.append(i)
        current_xor ^= i

        # If the XOR matches n, we're done
        if current_xor == n:
            return subset

    # If the XOR does not match n, check to fix it
    if current_xor != n:
        # The number to remove to fix XOR mismatch
        fix_number = current_xor ^ n
        # Ensure the number to remove is in the subset and is valid
        if fix_number in subset:
            subset.remove(fix_number)

    return subset



if __name__ == "__main__":
    n = 3
    output = maximize_subset(n)
    print(output)
