"""
count the frequency of each element in a given array...
arr = [1,2,3,2,2,4,1,3]
"""
def solve(arr):
    res = {}
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] in res:
            x = res[arr[i]]
            x += 1
            res[arr[i]] = x
            
        else:
            count = 1
            res[arr[i]] = count
            
            
    return res

if __name__ == "__main__":
    #arr = [1,2,3,2,2,4,1,3]
    arr = [1,2,3,2,2,4,1,3,3,3,3,3,3,3]
    ans = solve(arr)
    print(ans)
