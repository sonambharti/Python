'''
# Aggressive Cows

You are given an array with unique elements of stalls[], which denote the position of a stall. You are 
also given an integer k which denotes the number of aggressive cows. Your task is to assign stalls to 
k cows such that the minimum distance between any two of them is the maximum possible.

Examples :

Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.

Input: stalls[] = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[4].
The minimum distance between cows, in this case, is 4, which also is the largest among all possible ways.

Input: stalls[] = [2, 12, 11, 3, 26, 7], k = 5
Output: 1
Explanation: Each cow can be placed in any of the stalls, as the no. of stalls are exactly equal to the 
number of cows.
The minimum distance between cows, in this case, is 1, which also is the largest among all possible ways.
'''

def isPossible(m):
    count=1
    lcow=stalls[0]
    for i in stalls:
        if i-lcow>=m:
            count+=1
            if count==k:
                return 1
            lcow=i
    return 0
    

def aggressiveCows(stalls, k):
    l,r=0,max(stalls)
    stalls.sort()
    
    while l<=r:
        m=l+(r-l)//2
        if isPossible(m):
            ans=m
            l=m+1
        else:
            r=m-1
    return ans
    
    
if __name__ == "__main__":
    stalls = [2, 12, 11, 3, 26, 7]
    k = 5
    
    res = aggressiveCows(stalls, k)
    print("The largest minimum distance between cows: ", res)
