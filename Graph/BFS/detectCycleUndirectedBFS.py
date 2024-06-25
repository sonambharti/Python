# Detect cycle in undirected BFS implementation....

from collections import deque


def create_adj_undirected(edges):
    print("Creating directed adjacency Matrix")
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    adj = [[0] * numOfNodes for _ in range(numOfNodes)]
    
    for e in edges:
        adj[e[0]][e[1]] = adj[e[1]][e[0]] = 1 
    
    return adj

def bfs(adjMat):
    # using BFS
    print("BFS Traversal: \n")
    vis = set()
    adj = adjMat
    n = len(adj)
    
    for i in range(n):
        if i in vis:
            continue
        
        vis.add(i)
        q = deque([i])
        while q:
            el = q.pop()
            print(el, end=" ")
            for adjel in range(n):
                if adj[el][adjel]==1 and adjel not in vis:
                    vis.add(adjel)
                    q.appendleft(adjel)
    print()
    
    
def detect_cycle_undirected_bfs(adj):
    vis = set()
    n = len(adj)
    
    for i in range(n):
        if i in vis:
            continue
        
        vis.add(i)
        q = deque([[i, -1]])
        while q:
            el, parent = q.pop()
            # print(el, end=" ")
            for adjel in range(n):
                if adj[el][adjel]:
                    if adjel not in vis:
                        vis.add(adjel)
                        q.appendleft([adjel, el])
                    elif adjel != parent:
                        print(f"cycle found at {el} - {adjel}")
                        return
    
    print("No Cycle Found")
    
    

if __name__ == "__main__":
    
    adjMat_undir = create_adj_undirected([[0,1], [1,2], [1,3], [1,4], [3,4], [4,6], [5,7], [7,6]])
    print("\n\nUn-directed Adjecency Matrix....\n")
    for x in adjMat_undir:
        print(x)
    
    print("\nPrinting Un-directed bfs Traversal...\n")
    bfs(adjMat_undir)
    
    print("\n\nChecking if graph has cycle or not....\n")
    detect_cycle_undirected_bfs(adjMat_undir)
