#Reverse a string using recusion

def revString(s):
    if len(s)==0:
        return s
    else:
        return revString(s[1:]) + s[0]
        
if __name__ == "__main__":
        
    mystr = "Hello Sonam"
    res = revString(mystr)
    print(res)
