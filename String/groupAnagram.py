"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original 
letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""


from collections import defaultdict

def groupAnagram(strs):
    
    # lst = []
    # slst = []
    # n = len(strs)

    # for i in strs:
    #     el1 = "".join(sorted(i))
    #     slst = []
    #     slst.append(i)
    #     strs.remove(i)
    #     for el in strs:
    #         el2 = "".join(sorted(el))
    #         if len(el1) != len(el2):
    #             break
    #         else:
    #             if el1 != el2:
    #                 break
    #             else:
    #                 slst.append(el)
    #                 strs.remove(el)
        
    #     lst.append(slst)
    # if len(strs) != 0:
    #     lst.append(strs)

    # return lst
    
    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
        # print(anagram_map)
    
    return list(anagram_map.values())


if __name__ == "__main__":
    # s = ["eat","tea","tan","ate","nat","bat"]
    s = ["","","bat"]
   
    res = groupAnagram(s)
    print("Anagram groups: \n", res)
    
