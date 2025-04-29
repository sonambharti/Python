'''
# Zig Zag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''


def convert(s, numRows):
    if numRows <= 1:
        return s
    a = ""
    for i in range(numRows):
        for j in range(i,len(s),2*(numRows-1)):
            a+=s[j]
            if(i>0 and i<numRows-1 and j+2*(numRows-1)-2*i < len(s)):
                a+=s[j+2*(numRows-1)-2*i]
    return a
    
if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 4
    res = convert(s, numRows)
    print("Zig Zag conversion of string: ", res)
