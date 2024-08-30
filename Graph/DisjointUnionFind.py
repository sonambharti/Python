'''
# Disjoint set (Union-Find)

Given an array A[] that stores all number from 1 to N (both inclusive and sorted) and K queries.

The task is to do the following operations on array elements :

1. UNION X Z : Perform union of X and Z i.e. parent of Z will become the parent of X.
2. FIND X: Find the ultimate parent of X and print it.

Note: Initially all are the parent of themselves.The ultimate parent is the topmost node such that par[node]=node.

Input:
N = 5, K = 4
queries[] = {{find 4},
             {find 1},
             {unionSet 3 1},
             {find 3}}
Output:
4 1 1
Explanation:
1. The parent of 4 is 4. Hence the output is 4.
2. The parent of 1 is 1. Hence the output is 1.
3. After performing unionSet 3 1, parent of 3 becomes 1,
   since, parent of 1 is currently 1 itself.
4. The parent of 3 is now 1. Hence, the output is 1.

Your Task:  
You don't need to read input or print anything. Your task is to complete the functions- find() which 
takes an array A[] and an integer X as an input parameter and return the parent of X and the function
unionSet() which takes an array A[] and two integers X and Z and performs the union of X and Z.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

'''

# function should return parent of x
def find(parentArr, X):
    # Code here
    if X == parentArr[X - 1]:
        return X
    parentArr[X - 1] = find(parentArr, parentArr[X-1])
    return parentArr[X - 1]

# function shouldn't return or print anything
def unionSet(parentArr, X, Z):
    # Code here
    pu = find(parentArr, X)
    pv = find(parentArr, Z)
    
    parentArr[pu - 1] = pv



if __name__=='__main__':
    
    # parentArr = [0, 0, 1, 1, 3, 5, 7, 5]
   
    n,k = list(map(int, input().strip().split()))
    parentArr = [x for x in range(1, n+1)]
    s = input().strip().split()
    i = 0
    while i<len(s):
        if s[i]=='FIND':
            print(find(parentArr, int(s[i+1])), end=" ")
            i+=2
        elif s[i]=='UNION':
            unionSet(parentArr, int(s[i+1]), int(s[i+2]))
            i+=3
    
