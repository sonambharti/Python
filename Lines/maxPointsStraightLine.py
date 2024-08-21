'''
# Count maximum points on same line

Given two arrays X[] and Y[] of points where (Xi, Yi) represents a point on the X-Y plane. 
Your task is to complete the function maxPoints which returns an integer denoting the maximum 
number of points that lie on the same straight line.


Example 1:

Input:
X[] = {1, 2, 3}
Y[] = {1, 2, 3}
Output: 3
Explanation:
The points are (1,1), (2,2) and (3,3).

'''
from collections import defaultdict
from math import gcd

# Helper function to check if three points are on the same straight line
def checkStraightLine(X, Y, coordinates):
    n = len(coordinates)
    if n == 2:
        return True
    
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    # Check for all points if they satisfy the line equation
    for i in range(2, n):
        xi, yi = coordinates[i]
        # Use cross multiplication to avoid division (which can lead to precision issues)
        if (yi - y1) * (x2 - x1) != (y2 - y1) * (xi - x1):
            return False
    
    return True

# Function to calculate the maximum number of points on the same line
def maxPoints(X, Y, n):
    if n <= 2:
        return n
    
    max_points_on_line = 1

    # Iterate through each point and calculate slopes with other points
    for i in range(n):
        slopes = defaultdict(int)
        duplicate_points = 0
        current_max = 0
        
        for j in range(i + 1, n):
            dx = X[j] - X[i]
            dy = Y[j] - Y[i]
            
            # Handle duplicate points
            if dx == 0 and dy == 0:
                duplicate_points += 1
                continue
            
            # Simplify the slope by calculating the greatest common divisor (GCD)
            g = gcd(dx, dy)
            if g != 0:
                dx //= g
                dy //= g
            
            # Normalize the slope to avoid inconsistencies
            if dx < 0:
                dx = -dx
                dy = -dy
            elif dx == 0:
                dy = abs(dy)
            
            slopes[(dx, dy)] += 1
            current_max = max(current_max, slopes[(dx, dy)])
        
        # Update the maximum points on the same line, including duplicates
        max_points_on_line = max(max_points_on_line, current_max + duplicate_points + 1)
    
    return max_points_on_line

# Example usage
if __name__ == '__main__':
    X = [1, 2, 3]
    Y = [1, 2, 3]
    n = len(X)
    print("Maximum number of points on the same line:", maxPoints(X, Y, n))  # Output: 3
