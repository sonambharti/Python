# DFS using adjacency List and recursion

adjList = []
def create_dir_adj_list(edges, numOfNodes):
    global adjList
    # numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    adjList = [[]*numOfNodes for _ in range(numOfNodes)]
    for i in range(len(edges)):
        adjList[edges[i][0]].append(edges[i][1]) # directed
        # adjList[edges[i][1]].append(edges[i][0]) # undirected
    # print(adjList)
    # return adjList
    
st = []
vis = []
def dfs_recursion(adj_list, node):
    global st, vis
    vis[node] = True
    st.append(node)
    for i in adj_list[node]:
        if vis[i]==False:
            dfs_recursion(adj_list, i)
            
    return

        

if __name__ == "__main__":
    edges = [[0,1], [1,2], [1,3], [1,4], [3,4], [5,7], [7,6]]
    numOfNodes = 1 + max([el[1] for el in edges] + [el[0] for el in edges])
    create_dir_adj_list(edges, numOfNodes)
    print("Directed Adjecency List....\n")
    print(adjList)
    vis = [False]*numOfNodes
    for i in range(numOfNodes):
        if vis[i]==False:
            dfs_recursion(adjList, i)
    print("DFS Traversal using recursion:\n", st)
    
