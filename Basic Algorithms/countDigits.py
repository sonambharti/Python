"""
# Find the count of digits 
"""

def count_digits_1(N):
    count = 1

    while (N := N // 10) >= 1: # The := (walrus operator) allows updating N while checking the condition.
        count += 1  
    print(count)


def count_digits(n):
    count = 0
    while n:
        n //= 10  # Remove the last digit
        count += 1
    return count


def count_digits_str(n):
    # Using len() with String Conversion
    return len(str(abs(n)))  # Convert number to string and count characters


num = 2345
print("Count digits using while loop: ", count_digits(num))  # Output: 4
print("Convert number to string and count characters: ", count_digits_str(num)) 
count_digits_1(num)
