'''
# 451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.


Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 
'''

import heapq
def frequencySort(s):
    freq_dict = {}
    # Step 1: Count frequencies of elements in nums
    for element in s:
        # Get the current frequency of the element, default to 0 if it's not present
        freq_dict[element] = freq_dict.get(element, 0) + 1

    # Step 2: Build a min-heap of size k based on frequency
    max_heap = []
    
    for s, freq in freq_dict.items():
        heapq.heappush(max_heap, (-1 * freq, s))
    # print(max_heap)
    
    # Step 3: Build the result string by popping from the heap
    result = []
    while max_heap:
        count, char = heapq.heappop(max_heap)
        result.append(char * (-count))  # Multiply character by its frequency
    
    return ''.join(result)



# Example usage:
if __name__ == "__main__":
    string = "tree"
    print(frequencySort(string))
