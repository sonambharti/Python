'''
# Find H-index

Given an integer array citations[], where citations[i] is the number of citations a researcher 
received for the ith paper. The task is to find the H-index.

H-Index is the largest value such that the researcher has at least H papers that have been 
cited at least H times.

Examples:

Input: citations[] = [3, 0, 5, 3, 0]
Output: 3
Explanation: There are at least 3 papers (3, 5, 3) with at least 3 citations.

Input: citations[] = [5, 1, 2, 4, 1]
Output: 2
Explanation: There are 3 papers (with citation counts of 5, 2, and 4) that have 2 or more citations.
However, the H-Index cannot be 3 because there aren't 3 papers with 3 or more citations.

Input: citations[] = [0, 0]
Output: 0

'''


def hIndex(citations):
    #code here
    citations.sort(reverse=True)
    h=0
    for i,cit in enumerate(citations):
        # print(f"i = {i}, cit = {cit}")
        if cit >= i +1:
            h = i+1
        else:
            break
    return h 
    
    
    
if __name__ == "__main__":
    citations = [3, 0, 5, 3, 0]
    print(hIndex(citations))
    
    
