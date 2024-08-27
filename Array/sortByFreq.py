'''
# Sorting Elements of an Array by Frequency

Given an array of integers arr, sort the array according to the frequency of elements, 
i.e. elements that have higher frequency comes first. If the frequencies of two elements 
are the same, then the smaller number comes first.

Examples :

Input: arr[] = [5, 5, 4, 6, 4]
Output: [4, 4, 5, 5, 6]
Explanation: The highest frequency here is 2. Both 5 and 4 have that frequency. Now since 
the frequencies are the same the smaller element comes first. So 4 4 comes first then 
comes 5 5. Finally comes 6. The output is 4 4 5 5 6.
Input: arr[] = [9, 9, 9, 2, 5]
Output: [9, 9, 9, 2, 5]
Explanation: The highest frequency here is 3. Element 9 has the highest frequency So 9 9 9 
comes first. Now both 2 and 5 have the same frequency. So we print smaller elements first.
The output is 9 9 9 2 5.
Expected Time Complexity: O(n*logn)
Expected Space Complexity: O(n)
'''
def sortByFreq(arr):
    #code here
    freq = {}
    res = []
    for el in arr:
        # freq[el] += 1
        freq[el] = freq.get(el, 0) + 1
    print(freq)
    {2: 3, 1: 3, 8: 2}
    [(8, 2), (2, 3), (1, 3)]
    # freq = sorted(freq.items(), key=lambda x: x[1], reverse = True)
    
    '''
    Explanation:
      -x[1]: This sorts the dictionary by the values in descending order (because of the negative sign).
      x[0]: If two values are equal, the sorting will then fall back on the keys, which are sorted in ascending order.
    '''
  
    # Sort by values (descending) and by keys (ascending) if values are equal
    freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    print(freq)
    
    n = len(freq)
    
    for key, value in freq:
        temp = [key] * value
        res += temp
    return res

if __name__ == "__main__":
    arr = [2, 1, 8, 1, 2, 2, 1, 8]
    res = sortByFreq(arr)
    print("Sorting Elements of an Array by Frequency: ", res)
    
