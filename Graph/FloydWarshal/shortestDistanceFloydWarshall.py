"""
# Floyd Warshall

The problem is to find the shortest distances between every pair of vertices in a given 
edge-weighted directed graph. The graph is represented as an adjacency matrix of size n*n. 
Matrix[i][j] denotes the weight of the edge from i to j. If Matrix[i][j]=-1, it means there
is no edge from i to j.
Note : Modify the distances for every pair in-place.

Examples :

Input: matrix = [[0, 25],[-1, 0]]

Output: [[0, 25],[-1, 0]]
"""




def shortest_distance(matrix):
    n = len(matrix)
    
    for via in range(n):
        for u in range(n):
            for v in range(n):
              #  if matrix[u][v] > matrix[u][via] + matrix[via][u]:
                if (matrix[u][via] == -1 or matrix[via][v] == -1):
                    continue
                elif (matrix[u][via] != -1 and matrix[via][v] != -1):
                    if (matrix[u][v] == -1 or (matrix[u][v] > matrix[u][via] + matrix[via][v])):
                        matrix[u][v] = matrix[u][via] + matrix[via][v]
                    # elif(matrix[u][v] > matrix[u][via] + matrix[via][v]):
                    #     matrix[u][v] = matrix[u][via] + matrix[via][v]
    return matrix

if __name__ == "__main__":
    matrix = [[0, 25],[-1, 0]]
    res = shortest_distance(matrix)
    print("find the shortest distances between every pair of vertices: \n", res)
    
    
    
