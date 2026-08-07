# print nos from 1 to n
def print_nos1(lst, indx, n):
    if indx > n:
        return 
    lst.append(indx)
    print_nos(lst, indx+1, n)
    return lst

def print_nos(n):
    if n==1:
        print(n, end =" ")
        return 
    
    print_nos(n - 1)
    print(n, end =" ")

def print_nos3(n):
    if n==1:
        print(n, end =" ")
        return 
    
    print(n, end =" ")
    print_nos(n - 1)
    
if __name__ == "__main__":
    print_nos(5) # print nos from 1 to 5
    res = print_nos1([], 1, 5) # print nos from 1 to 5
    print(res)
    print_nos3(5) # print nos from 5 to 1
    
