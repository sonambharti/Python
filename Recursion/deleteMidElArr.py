# Delete Middle Ellement from a stack
# Time Complexity: O(n)
# Space Complexity: O(n)

def solve(st, k):
    if k==1:
        st.pop()
        return
    
    temp = st.pop()
    solve(st, k-1)
    st.append(temp)
    return
    
def deleteMidElArr(st, n):
    if len(st) == 0:
        return
    k = n//2 + 1
    solve(st, k)
    return
    
    
if __name__ == "__main__":
    st = [2,7,3,5]
    deleteMidElArr(st, len(st))
    print(st)
