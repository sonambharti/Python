"""
Find the number of integers x such that x lies between [num1, num2]
and minm_sum <= sum_of-digits_of_x <= maxm_sum.
"""

def digitSumsProblem(min_sum, max_sum, num1, num2):
    res = []
    num1 = int(num1)
    num2 = int(num2)
    for num in range(num1, num2+1):
        sum = 0
        temp = num
        while num>0:
            rem = num%10
            sum += rem
            num //= 10
            
        # print("sum = ",sum)
        if sum >= min_sum and sum <= max_sum:
            res.append(temp)
            
    return res


if __name__ == "__main__":
    min_sum = int(input())
    max_sum = int(input())
    num1 = input()
    num2 = input()
    
    # print(int(num1))
    # print(type(int(num1)))
    
    res = digitSumsProblem(min_sum, max_sum, num1, num2)
    print(res)
    count = len(res)
    print(count)
