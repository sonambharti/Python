"""
# 874. Walking Robot Simulation

A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive 
a sequence of these three possible types of commands:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). 
If the robot runs into an obstacle, then it will instead stay in its current location and move on 
to the next command.

Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the 
distance is 5, return 25).

Note:

North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
There can be obstacle in [0,0].
 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 3 units to (3, 4).
The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
4. Turn left.
5. Move north 4 units to (1, 8).
The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.
"""

from collections import defaultdict, Counter

def robotSim(commands, obstacles):
    # 0: North, 1: East, 2: South, 3: West
    directions = [[0,1], [1,0], [0, -1], [-1, 0]]
    curr_pos = [0,0]
    curr_dir = 0 # index of the direction list
    res = 0

    # mapping obstactes as key - value_list pair
    obst_dict = {}      # Ex: obst_dict = {2: [4, 3], 1: [4]}
    for sublist in obstacles:
        key = sublist[0]
        value = sublist[1]
        
        # If the key is already in the dictionary, append the value to the list
        if key in obst_dict:
            obst_dict[key].append(value)
        else:
            # If the key is not in the dictionary, create a new list for that key
            obst_dict[key] = [value]
            
    
    for command in commands:
        # turn 90 degree right
        if command == -1:
            curr_dir = (curr_dir + 1) % 4
            continue

        # turn 90 degree left
        if command == -2:
            curr_dir = curr_dir - 1
            if curr_dir == -1:
                curr_dir = 3
            continue

        # Move Forward
        direction = directions[curr_dir]

        for step in range(command):
            next_X = curr_pos[0] + direction[0]
            next_Y = curr_pos[1] + direction[1]

            if next_X in obst_dict.keys():
                if next_Y in obst_dict[next_X]:
                    break
            
            curr_pos[0] = next_X
            curr_pos[1] = next_Y

        res = max(res, curr_pos[0]*curr_pos[0] + curr_pos[1]*curr_pos[1] )

    return res

    
# Example usage:
if __name__ == "__main__":
    commands = [4,-1,4,-2,4]
    obstacles = [[2,4]]
    print("The maximum Euclidean distance that the robot ever gets from the origin squared: ", robotSim(commands, obstacles))  # Output: 65
