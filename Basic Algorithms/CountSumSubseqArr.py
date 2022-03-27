# Brute Force Method....

n = int(input("Enter the size of array: "))
arr = []
print("Enter the elements of array: ")
for i in range(0, n):
    l = int(input())
    arr.append(l)
    
count = 0
t_sum = int(input("Enter the target sum: "))
for start in range(0, n-1):
    end = start + 1 
    sum = start + end
    while (sum < t_sum):
        end = start + 1 
        sum = sum + end
    if (sum == t_sum):
        count = count+1
        
print(count)
        

