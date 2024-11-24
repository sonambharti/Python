'''
# Q3. Count Valid pairs (weekly contest-182)

Given a graph with n nodes, where each node i has a weight w[i]. 
Undirected edges are present between 2 nodes i and j (i!=j) if
and only if: w[i] & w[j] != 0, where "&" represents the bitwise and operation.
The task is to find the total number of valid pairs in the graph. A pair
of nodes(i, j), wher i<j is called aa vaid pair if there exists a path 
between the nodes i and j.
 
Input:
 w = [1, 2, 3]
Output: 3
'''


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def countValidPairs(weights):
    n = len(weights)
    uf = UnionFind(n)

    # Map each bit position to indices in weights
    bit_map = {}
    for i, weight in enumerate(weights):
        bit = 0
        while weight:
            if weight & 1:
                if bit not in bit_map:
                    bit_map[bit] = []
                bit_map[bit].append(i)
            weight >>= 1
            bit += 1

    # Union nodes based on shared bits
    for indices in bit_map.values():
        for i in range(1, len(indices)):
            uf.union(indices[0], indices[i])

    # Count sizes of connected components
    component_size = {}
    for i in range(n):
        root = uf.find(i)
        component_size[root] = component_size.get(root, 0) + 1

    # Calculate valid pairs
    valid_pairs = 0
    for size in component_size.values():
        valid_pairs += size * (size - 1) // 2

    return valid_pairs


if __name__ == "__main__":
    w = [1, 2, 3]
    print(countValidPairs(w))  # Output: 3
