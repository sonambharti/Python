# DFS implementation using Doubly-end-Queue (Deque)...

from collections import deque

def create_adj(edges):
    print("Creating directed adjacency Matrix")
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    adj = [[0] * numOfNodes for _ in range(numOfNodes)]
    
    for e in edges:
        adj[e[0]][e[1]] = 1 
    
    return adj
    
    
def create_adj_undirected(edges):
    print("Creating directed adjacency Matrix")
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    adj = [[0] * numOfNodes for _ in range(numOfNodes)]
    
    for e in edges:
        adj[e[0]][e[1]] = adj[e[1]][e[0]] = 1 
    
    return adj

def dfs(adjMat):
    # using DFS
    print("DFS Traversal: \n")
    vis = set()
    adj = adjMat
    n = len(adj)
    
    for i in range(n):
        if i in vis:
            continue
        
        vis.add(i)
        st = deque([i])
        while st:
            el = st.pop()
            print(el, end=" ")
            for adjel in range(n):
                if adj[el][adjel]==1 and adjel not in vis:
                    vis.add(adjel)
                    st.append(adjel)
    print()
    

if __name__ == "__main__":
    adjMat_dir = create_adj([[0,1], [1,2], [1,3], [1,4], [3,4], [5,7], [7,6]])
    print("Directed Adjecency Matrix....\n")
    for x in adjMat_dir:
        print(x)
    
    print("\nPrinting Directed DFS Traversal...\n")
    dfs(adjMat_dir)
    
    
    adjMat_undir = create_adj_undirected([[0,1], [1,2], [1,3], [1,4], [3,4], [5,7], [7,6]])
    print("\n\nUn-directed Adjecency Matrix....\n")
    for x in adjMat_undir:
        print(x)
    
    print("\nPrinting Un-directed DFS Traversal...\n")
    dfs(adjMat_undir)
