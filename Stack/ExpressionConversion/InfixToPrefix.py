"""
# Python program to convert infix to prefix

Step by step approach:

1.  Reverse the infix expression. Note while reversing each '(' will become ')' and each ')' becomes '('.
2.  Convert the reversed infix expression to postfix expression.
    -  Initialize an empty stack to store operators and an empty string for the postfix expression.
    -  Scan the infix expression from left to right.
    -  If the character is an operand, append it to the postfix expression.
    -  If the character is '(', push it onto the stack.
    -  If the character is ')', pop from the stack and append to the postfix expression until '(' is found, then pop '(' without appending.
    -  If the character is an operator, pop and append operators from the stack until the stack is empty or a lower precedence operator is found, then push the current operator onto the stack.
    -  After scanning the expression, pop and append all remaining operators from the stack to the postfix expression.
3.  Reverse the postfix expression and return it.
"""
# Check if character is an operator
def isOperator(ch):
    return ch in ['+', '-', '*', '/', '^']

# Get precedence of operators
def operatorPrecedence(op):
    if op == '^':
        return 3
    if op in ['*', '/']:
        return 2
    if op in ['+', '-']:
        return 1
    return -1



# Convert infix expression to postfix notation
def convertInfixToPostfix(s):
    st = []
    res = ""
    sz = len(s)

    for i in range(sz):
        if s[i].isalnum():
            res += s[i]
        elif s[i] == '(':
            st.append(s[i])
        elif s[i] == ')':
            while st and st[-1] != '(':
                res += st.pop()
            st.pop()
        else:
            while st and operatorPrecedence(s[i]) <= operatorPrecedence(st[-1]):
                res += st.pop()
            st.append(s[i])

    while st:
        res += st.pop()

    return res

# Convert infix expression to prefix notation
def convertToPrefix(infix):
    infix = infix[::-1]
    infix = ''.join(['(' if ch == ')' else ')' if ch == '(' else ch for ch in infix])
    
    postfix = convertInfixToPostfix(infix)
    return postfix[::-1]


if __name__ == "__main__":
    s = "(a-b/c)*(a/k-l)"
    print("Prefix", convertToPrefix(s))
