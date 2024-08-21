'''
# 1232. Check if it's a straight line or not

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents 
the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true


'''

def checkStraightLine(coordinates):
    n = len(coordinates)
    if n == 2:
        return True
    
    x1 = coordinates[0][0]
    y1 = coordinates[0][1]
    x2 = coordinates[1][0]
    y2 = coordinates[1][1]

    # since, Eq : (y-y1)*(x2-x1) = (y2-y1)*(x-x1)
    # st line : y = mx +c 

    for i in range(2, n):
        if (((coordinates[i][1] - y1) * (x2 - x1)) != ((y2 - y1) * (coordinates[i][0] - x1))):
            return False
    return True
    


if __name__ == '__main__':
	coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
	print("it's a straight line or not: ", checkStraightLine(coordinates))
