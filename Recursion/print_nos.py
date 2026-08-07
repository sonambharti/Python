# print nos from 1 to n
def print_nos(lst, indx, n):
    if indx > n:
        return 
    lst.append(indx)
    print_nos(lst, indx+1, n)
    return lst
    
if __name__ == "__main__":
    res = print_nos([], 1, 5) # print nos from 1 to 5
    print(res)
