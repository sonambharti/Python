"""
Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

Example 1:

Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.


Example 2:

Input:
txt = aabaabaa
pat = aaba
Output: 4
Explanation: aaba is present 4 times in txt.
"""



def search_anagram_count(pat, txt):
    # code here
    word_count = {}
        
    for word in pat:
        word_count[word] = 1 + word_count.get(word, 0)
    i, j, ans = 0, 0, 0
    n = len(pat)
    count = len(word_count)
    while j < len(txt):
        if txt[j] in word_count:
            word_count[txt[j]] -= 1
            if word_count[txt[j]] == 0:
                count -= 1
        if j - i + 1 == n:
            if count == 0:
                ans += 1
            if txt[i] in word_count:
                word_count[txt[i]] += 1
                if word_count[txt[i]] == 1:
                    count += 1
            i += 1
        j += 1
    return ans


if __name__ == "__main__":
    txt = "forxxorfxdofr"
    pat = "for"
    res = search_anagram_count(pat, txt)
    print("Count of anagrams available: ", res)
