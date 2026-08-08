# Reverse a stack
# Time Complexity: O(n)
# Space Complexity: O(n)


def insert(st, el):
    if len(st) == 0:
        st.append(el)
        return
    temp = st.pop()
    insert(st, el)
    st.append(temp)
    
def reverse(st):
    if len(st) == 1:
        return
    
    temp = st.pop()
    reverse(st)
    insert(st, temp)
    
    
    
if __name__ == "__main__":
    st = [2,7,3,5, 1, 6]
    reverse(st)
    print(st)
