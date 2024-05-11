"""
904. Fruit Into Baskets
You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] is the type of fruit 
the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules 
that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There 
is no limit on the amount of fruit each basket can hold. Starting from any tree of your
choice, you must pick exactly one fruit from every tree (including the start tree) while
moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
"""
def max_fruits_brute_force(fruits):
    max_fruits = 0

    # Iterate through each tree as a potential starting point
    for i in range(len(fruits)):
        basket1 = None
        basket2 = None
        count = 0

        # Traverse to the right from the current starting point
        for j in range(i, len(fruits)):
            # Check if the current fruit can be added to basket1
            if basket1 is None or fruits[j] == basket1:
                basket1 = fruits[j]
                count += 1
            # Check if the current fruit can be added to basket2
            elif basket2 is None or fruits[j] == basket2:
                basket2 = fruits[j]
                count += 1
            # If the current fruit cannot be added to either basket, stop
            else:
                break

        # Update the maximum number of fruits collected
        max_fruits = max(max_fruits, count)

    return max_fruits


def max_fruits_sliding_window(fruits):
    max_fruits = 0
    basket = {}
    left = 0

    # Iterate through each tree with a sliding window
    for right in range(len(fruits)):
        fruit = fruits[right]

        # Add the current fruit to the basket and update its count
        basket[fruit] = basket.get(fruit, 0) + 1

        # Shrink the window from the left while maintaining the rules
        while len(basket) > 2:
            left_fruit = fruits[left]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            left += 1

        # Update the maximum number of fruits collected
        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits
    
if __name__ == "__main__":
    fruits = [1, 2, 1, 2, 3]
    print("Brute Force Approach: ", max_fruits_brute_force(fruits))
    print("Sliding Window Approach: ", max_fruits_sliding_window(fruits))
