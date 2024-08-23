"""
# 735. Asteorid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive meaning right, negative meaning left). Each asteroid moves 
at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. Two 
asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

"""


def asteroidCollision(asteroids):
    st = []
    for a in asteroids:
        while st and a < 0 and st[-1] > 0:
            summ = a + st[-1]

            if summ < 0:
                st.pop()
            elif summ > 0:
                a = 0
            else: # In case summ = 0
                st.pop()
                a = 0
        if a != 0: # If the 1st el is negative then too it ll not collide.
            st.append(a)

    return st
    
if __name__ == "__main__":
    asteroids = [10,2,-5]
    res = asteroidCollision(asteroids)
    print("The remaining asteorid: ", res)
