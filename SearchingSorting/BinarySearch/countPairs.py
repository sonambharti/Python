'''
# Number of Pairs

Given two positive integer arrays arr and brr, find the number of pairs such that x^y > y^x 
(raised to power of) where x is an element from arr and y is an element from brr.

Examples :

Input: arr[] = [2, 1, 6], brr[] = [1, 5]
Output: 3
Explanation: The pairs which follow x^y > y^x are: 21 > 12,  25 > 52 and 61 > 16 .
Input: arr[] = [2 3 4 5], brr[] = [1 2 3]
Output: 5
Explanation: The pairs which follow x^y > y^x are: 21 > 12 , 31 > 13 , 32 > 23 , 41 > 14 , 51 > 15 .

'''

# Brute Force Approach

def countPairs_BruteForce(arr, brr):
    count = 0
    for el1 in arr:
        for el2 in brr:
            temp1 = el1 ** el2
            temp2 = el2 ** el1
            
            if temp1 > temp2:
                count += 1
    return count
    

def binarySearch(key, brr):
    low, high = 0, len(brr) - 1
    index = -1
    while low <= high:
        mid = low + (high - low) // 2
        
        if brr[mid] <= key:
            index = mid
            low = mid + 1
        else:
            high = mid - 1
            
            
    return index
    
#Function to count number of pairs such that x^y is greater than y^x.     
def countPairs(arr,brr):
    #code here
    n = len(arr)
    m = len(brr)
    
    # Binary Search
    # x^y > y^x, if and only if y > x
    brr.sort()
    resCount, count1, count2, count34 = 0, 0, 0, 0
    
    for el in brr:
        if el == 1:
            count1 += 1
        elif el == 2:
            count2 += 1
        elif el == 3 or el == 4:
            count34 += 1
            
    for el in arr:
        if el != 1:
            resCount += count1
            if el == 2:
                resCount -= count34
            if el == 3:
                resCount += count2
            index = binarySearch(el, brr)
            resCount += m - index - 1
    return resCount
        
    
        
	
if __name__ == "__main__":
    arr = [2, 1, 6]
    brr = [1, 5]
    
    res = countPairs_BruteForce(arr, brr)
    
    print("The number of pairs such that x^y > y^x: ", res)


    res1 = countPairs(arr, brr)
    
    print("The number of pairs such that x^y > y^x: ", res1)
