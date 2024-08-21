'''
# Check if 2 line segments Intersects

Given the coordinates of the endpoints(p1,q1, and p2,q2) of the two line segments. 
Check if they intersect or not. If the Line segments intersect return true otherwise 
return false.

Note: Please check the intersection lies within the line segments.

Examples

Input: p1=(1,1), q1=(10,1), p2=(1,2), q2=(10,2)
Output: false
Explanation:The two line segments formed by p1-q1 and p2-q2 do not intersect.

Input: p1=(10,0), q1=(0,10), p2=(0,0), q2=(10,10)
Output: true
Explanation: The two line segments formed by p1-q1 and p2-q2 intersect.

Input: p1=(5,-2), q1=(13,2), p2=(2,-3), q2=(3,0)
Output: false
Explanation: The two line segments formed by p1-q1 and p2-q2 are intersecting beyond 
endpoints, so it is not considerable.

'''



class Solution:
    def direction(self, p, q, r):

        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        if val == 0:

            return 0

        return 1 if val > 0 else -1
        
            

    def onSegment(self, p, q, r):

        return q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])



    def doIntersect(self, p1, q1, p2, q2):

        d1 = self.direction(p1, q1, p2)

        d2 = self.direction(p1, q1, q2)

        d3 = self.direction(p2, q2, p1)

        d4 = self.direction(p2, q2, q1)

        if d1 != d2 and d3 != d4:

            return "true"

        if d1 == 0 and self.onSegment(p1, p2, q1):

            return "true"

        if d2 == 0 and self.onSegment(p1, q2, q1):

           return "true"

        if d3 == 0 and self.onSegment(p2, p1, q2):

            return "true"

        if d4 == 0 and self.onSegment(p2, q1, q2):

            return "true"

        return "false"
        
if __name__ == "__main__":
    p1=(10,0)
    q1=(0,10)
    p2=(0,0)
    q2=(10,10)
    
    res = Solution().doIntersect(p1, q1, p2, q2)
    
    print("Check if 2 line segments Intersects: ", res)
    
