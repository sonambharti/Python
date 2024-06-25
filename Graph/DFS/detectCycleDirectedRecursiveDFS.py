# Recursive approach to find cycle in a directed graph using DFS traversal


from collections import deque

def create_adj(edges):
    print("\nCreating directed adjacency Matrix")
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    adj = [[0] * numOfNodes for _ in range(numOfNodes)]
    
    for e in edges:
        adj[e[0]][e[1]] = 1 
    
    return adj
    
    
def dfs_recursive_path(adj, vis, path, el):
    vis.add(el)
    path.add(el)
    for adjel in range(len(adj)):
        if adj[el][adjel]:
            if adjel not in vis:
                if dfs_recursive_path(adj, vis, path, adjel):
                    return True
            elif adjel in path:
                print(f"cycle found at {el} - {adjel}")
                return True
    
    path.remove(el)
    return False
            
    
    

def detect_cycle_directed_recursive_dfs(adjMat_dir):
    vis = set()
    n = len(adjMat_dir)
    
    for i in range(n):
        if i in vis:
            continue
        if dfs_recursive_path(adjMat_dir, vis, set(), i):
            # return
            continue
    print("no cycle")
    

if __name__ == "__main__":
    
    adjMat_dir = create_adj([[0,1], [1,2], [1,3], [1,4], [3,4], [4,6], [5,7], [6,5]])
    print("\n\nDirected Adjecency Matrix....\n")
    for x in adjMat_dir:
        print(x)
        

    
    print("\n\nChecking if graph has cycle or not....\n")
        
    detect_cycle_directed_recursive_dfs(adjMat_dir)
    
    
    adjMat_dir = create_adj([[0,1], [1,2], [1,3], [1,4], [3,4], [4,6], [5,7], [7,6], [6,5]])
    
    print("\n\nDirected Adjecency Matrix for 2nd graph....\n")
    for x in adjMat_dir:
        print(x)
        

    
    print("\n\nChecking if 2nd graph has cycle or not....\n")
        
    detect_cycle_directed_recursive_dfs(adjMat_dir)
    
    adjMat_dir = create_adj([[0,1], [1,2], [1,3], [4,1], [3,4], [4,6], [5,7], [7,6], [6,5]])
    
    print("\n\nDirected Adjecency Matrix for 3rd graph....\n")
    for x in adjMat_dir:
        print(x)
        

    
    print("\n\nChecking if 3rd graph has cycle or not....\n")
        
    detect_cycle_directed_recursive_dfs(adjMat_dir)
            
    
