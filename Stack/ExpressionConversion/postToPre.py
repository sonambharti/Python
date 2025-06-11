'''
# Postfix To Prefix conversion

You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its prefix form.

Example 1:

Input: 
ABC/-AK/L-*
Output: 
*-A/BC-/AKL
Explanation: 
The above output is its valid prefix form.

Example 2:

Input: 
ab+
Output: 
+ab
Explanation: 
The above output is its valid prefix form.
Your Task:

Complete the function string postToPre(string post_exp), which takes a postfix string as input and returns its prefix form.

Expected Time Complexity: O(post_exp.length()).

Expected Auxiliary Space: O(post_exp.length()).
'''

def operanPrecedence(op):
    if op == '^':
        return 3
    if op == ['*', '/']:
        return 2
    if op == ['+', '-']:
        return 1
    return -1
    
    
def postToPre(post_exp):
    n = len(post_exp)
    res = ''
    st = []
    operator = ['^', '*', '/', '+', '-']
    
    for i in range(n):
        if post_exp[i].isalnum():
            st.append(post_exp[i])
        if post_exp[i] in operator:
            a = st.pop()
            b = st.pop()
            exp = str(post_exp[i] + b  + a)
            st.append(exp)
    return st.pop()
    
if __name__ == "__main__":
    s = "ABC/-AK/L-*"
    print(f'Prefix expressions: {postToPre(s)}')
            
