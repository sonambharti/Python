'''
# Klee’s Algorithm (Length Of Union Of Segments of a line)

Given starting and ending positions of segments on a line, the task is to take the 
union of all given segments and find length covered by these segments.
Examples:  

Input : segments[] = {{2, 5}, {4, 8}, {9, 12}}
Output : 9 
Explanation:
segment 1 = {2, 5}
segment 2 = {4, 8}
segment 3 = {9, 12}
If we take the union of all the line segments,
we cover distances [2, 8] and [9, 12]. Sum of 
these two distances is 9 (6 + 3)

'''

# Python program for the above approach

def segmentUnionLength(segments):

	# Size of given segments list
	n = len(segments)
	
	# Initialize empty points container
	points = [None] * (n * 2)
	
	# Create a vector to store starting 
	# and ending points
	for i in range(n):
		points[i * 2] = (segments[i][0], False)
		points[i * 2 + 1] = (segments[i][1], True)
		
	# Sorting all points by point value
	points = sorted(points, key=lambda x: x[0])
	
	# Initialize result as 0
	result = 0
	
	# To keep track of counts of current open segments
	# (Starting point is processed, but ending point
	# is not)
	Counter = 0
	
	# Traverse through all points
	for i in range(0, n * 2):
	
		# If there are open points, then we add the
		# difference between previous and current point.
		if (i > 0) & (points[i][0] > points[i - 1][0]) & (Counter > 0):
			result += (points[i][0] - points[i - 1][0])
			
		# If this is an ending point, reduce, count of
		# open points.
		if points[i][1]:
			Counter -= 1
		else:
			Counter += 1
	return result



if __name__ == '__main__':
	segments = [(2, 5), (4, 8), (9, 12)]
	print("Length Of Union Of Segments of a line = ", segmentUnionLength(segments))
