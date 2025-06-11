'''
# Prefix to Infix conversion

You are given a string S of size N that represents the prefix form of a valid mathematical expression.
The string S contains only lowercase and uppercase alphabets as operands and the operators are 
+, -, *, /, %, and ^.Convert it to its infix form.

Example 1:

Input: 
*-A/BC-/AKL
Output: 
((A-(B/C))*((A/K)-L))
Explanation: 
The above output is its valid infix form.

Your Task:

Your task is to complete the function string preToInfix(string pre_exp), which takes a prefix string as
input and return its infix form.

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
    
    
def preToInfix(pre_exp):
    # Code here
    
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
            exp = str('('+ a + pre_exp[i] + b + ')')
            st.append(exp)
    return st.pop()
    
if __name__ == "__main__":
    s = "*-A/BC-/AKL"
    print(f'Prefix expressions: {preToInfix(s)}')
            
