'''
# Postfix to Infix conversion

You are given a string that represents the postfix form of a valid mathematical expression.
Convert it to its infix form.

Example:

Input:
ab*c+ 
Output: 
((a*b)+c)
Explanation: 
The above output is its valid infix form.
Your Task:

Complete the function string postToInfix(string post_exp), which takes a postfix string as
input and returns its infix form.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).


'''

def operanPrecedence(op):
    if op == '^':
        return 3
    if op == ['*', '/']:
        return 2
    if op == ['+', '-']:
        return 1
    return -1
    
    
def postfixToInfix(post_exp):
    # Code here
    
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
            exp = str('('+ b + post_exp[i] + a + ')')
            st.append(exp)
    return st.pop()
    
if __name__ == "__main__":
    s = "ab*c+ "
    print(f'Postfix expressions: {postfixToInfix(s)}')
            
