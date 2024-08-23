"""
# 394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square 
brackets are well-formed, etc. Furthermore, you may assume that the original data does not 
contain any digits and that digits are only for those repeat numbers, k. For example, there will
not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

"""

def decodeString(s):
       
    st = []

    for el in s:
        if el != ']':
            st.append(el)
        else:
            temp_char = ""
            while st[-1] != '[':
                temp_char = st.pop() + temp_char
                
            st.pop()
            ch_num = ""
            while st and st[-1].isdigit():
                ch_num = st.pop() + ch_num

            temp_char = int(ch_num) * temp_char
            st.append(temp_char)

    res = "".join(st)
    return res
    
if __name__ == "__main__":
    s = "2[abc]3[cd]ef"
    res = decodeString(s)
    print("Decoded String: ", res)
