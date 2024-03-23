"""
You are given a stack st of n integers and an element x. 
You have to insert x at the bottom of the given stack. 

Note: Everywhere in this problem, the bottommost element 
of the stack is shown first while priniting the stack.

Example 1:

Input:
n = 5
x = 2
st = {4,3,2,1,8}
Output:
{2,4,3,2,1,8}
Explanation:
After insertion of 2, the final stack will be {2,4,3,2,1,8}.
"""

def insertAtBottom(st, x):
    # code here
    n = len(st)
    res_st = []
    while st:
        el = st.pop()
        res_st.append(el)
    
    st.append(x)
    while res_st:
        el = res_st.pop()
        st.append(el)
    return st
    
    
if __name__ == "__main__":
    n = 5
    x = 2
    st = [4,3,2,1,8]
    
    res = insertAtBottom(st, x)
    print(f"Inserting {x} in the given stack at bottom: ", res)
