'''
# Q2. Minimum Time to burst balloons (weekly contest-182)

Geek wants to burst exactly k gallons placed at given position coordinates 
of number line in position array. Geek start from coordinate 0 and can move 
left and right on the coordinate number line at a speed of 1 unit per second. 
Find the number of minimum time taken to burst k ballons

Input:
k = 2, positions = [2, -1, 4]
Output: 4
'''


from itertools import combinations

def minTimeToBurstBalloons(k, positions):
    # Sort the positions by absolute distance from 0
    positions.sort()
    
    min_time = float('inf')
    
    # Generate all combinations of k positions
    for subset in combinations(positions, k):
        leftmost = subset[0]
        rightmost = subset[-1]
        
        # Compute time for this subset
        time = min(abs(leftmost), abs(rightmost)) + (abs(rightmost - leftmost))
        min_time = min(min_time, time)
    
    return min_time
    
    

def minTimeToBurstBalloons_slidingWindow(k, positions):
    # Sort the positions by their values
    positions.sort()
    
    min_time = float('inf')
    
    # Sliding window of size k
    for i in range(len(positions) - k + 1):
        leftmost = positions[i]
        rightmost = positions[i + k - 1]
        
        # Two possible cases:
        # Case 1: Start from leftmost, go to rightmost
        time_left_to_right = abs(leftmost) + abs(rightmost - leftmost)
        
        # Case 2: Start from rightmost, go to leftmost
        time_right_to_left = abs(rightmost) + abs(rightmost - leftmost)
        
        # Take the minimum of both cases
        min_time = min(min_time, time_left_to_right, time_right_to_left)
    
    return min_time
    
    

if __name__ == "__main__":
    k = 2
    positions = [2, -1, 4]
    print(minTimeToBurstBalloons(k, positions))  # Output: 4
    
    print(minTimeToBurstBalloons_slidingWindow(k, positions))  # Output: 4
    
    
    
