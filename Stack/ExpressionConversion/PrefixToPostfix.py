'''
# Prefix to Postfix conversion

You are given a string that represents the prefix form of a valid mathematical expression. Convert it to its postfix form.

Example:

Input: 
*-A/BC-/AKL
Output: 
ABC/-AK/L-*
Explanation: 
The above output is its valid postfix form.
Your Task:

Complete the function preToPost(string pre_exp), which takes a prefix string as input and returns its postfix form.

 

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
    
def preToPost(pre_exp):
            
    n = len(pre_exp)
    res = ''
    st = []
    operator = ['^', '*', '/', '+', '-']
    
    for i in range(n-1, -1, -1):
        if pre_exp[i].isalnum():
            st.append(pre_exp[i])
        if pre_exp[i] in operator:
            a = st.pop()
            b = st.pop()
            exp = str(a + b +  pre_exp[i])
            st.append(exp)
    return st.pop()
    
if __name__ == "__main__":
    s = "*-A/BC-/AKL"
    print(f'Postfix expressions: {preToPost(s)}')
            
