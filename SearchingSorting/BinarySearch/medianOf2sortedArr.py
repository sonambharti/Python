'''
# Median of 2 sorted arrays of different sizes

Given two sorted arrays a[] and b[], . You need to find and return the median of the combined array after merging them into
a single sorted array.

Examples:

Input: a[] = [-5, 3, 6, 12, 15], b[] = [-12, -10, -6, -3, 4, 10]
Output: 3
Explanation: The merged array is [-12, -10, -6, -5, -3, 3, 4, 6, 10, 12, 15]. So the median of the merged array is 3.

Input: a[] = [2, 3, 5, 8], b[] = [10, 12, 14, 16, 18, 20]
Output: 11
Explanation: The merged array is [2, 3, 5, 8, 10, 12, 14, 16, 18, 20]. So the median of the merged array is (10 + 12) / 2 = 11.

Input: a[] = [], b[] = [2, 4, 5, 6]
Output: 4.5
Explanation: The merged array is [2, 4, 5, 6]. So the median of the merged array is (4 + 5) / 2 = 4.5.
'''

import statistics

def medianOf2(array1, array2):
    #code here
    i,j=0,0
    lst=[]
    while i < len(array1) and j < len(array2):
        if array1[i]<=array2[j]:
            lst.append(array1[i])
            i+=1
        elif array1[i]>array2[j]:
            lst.append(array2[j])
            j+=1
    while i < len(array1):
        lst.append(array1[i])
        i+=1
    while j < len(array2):
        lst.append(array2[j])
        j+=1
    ans=statistics.median(lst)
    if ans%1==0:
        return int(ans)
    else:
        return ans
        
            
if __name__ == "__main__":
    array1 = [-5, 3, 6, 12, 15]
    array2 = [-12, -10, -6, -3, 4, 10]
    res = medianOf2(array1, array2)
    
    print("the median of the combined array after merging: ", res)
