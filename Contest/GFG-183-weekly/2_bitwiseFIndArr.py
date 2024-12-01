'''
# Bitwise Operations

Geek has an array of size n, initialized with 0. He is given k operations, where
each operation j is represented as op[j] [L,R,X]. Each operation updates the elements
of the array arr[] in the following way:
For each i in the range L <= i <= R(1-based index), perform the operation arr[i] =arr[i]^X,
where ^ represents the bitwise XOR operation.
Determine the final array arr[] after processing all operations and return it.

Input: n = 4, k = 3, ops[][] = [[1,3,2],[2,4,4],[1,4,6]]
Output: [4,0,0,2]
'''

def findArr_apply_operations_brute(n, k, ops):
    # Initialize the array with 0s
    arr = [0] * n

    # Process each operation
    for op in ops:
        L, R, X = op
        # Perform the XOR operation for each index in the range L to R (1-based index)
        for i in range(L - 1, R):
            arr[i] ^= X

    return arr

def findArr_apply_operations(n, k, ops):
    # Initialize an array and a difference array
    arr = [0] * (n + 1)

    # Apply the difference array approach for each operation
    for op in ops:
        L, R, X = op
        arr[L - 1] ^= X  # Apply XOR at the start of the range (convert to 0-based index)
        if R < n:
            arr[R] ^= X  # Revert XOR after the end of the range

    # Calculate the final array using prefix XOR
    result = [0] * n
    current_xor = 0
    for i in range(n):
        current_xor ^= arr[i]
        result[i] = current_xor

    return result
    
if __name__ == "__main__":
    n = 4
    k = 3
    ops = [[1, 3, 2], [2, 4, 4], [1, 4, 6]]
    result = findArr_apply_operations_brute(n, k, ops)
    print(result)

    result = findArr_apply_operations(n, k, ops)
    print(result)
