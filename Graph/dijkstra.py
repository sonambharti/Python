"""
Dijkstra algo is shortest path algorithm. It finds the shortest
distance between source and destination over a weighte graph.
This a greedy approach.
For example: Google map.
"""

import heapq

def dijkstra(graph, source):
    distance = {node: float('infinity') for node in graph}
    distance[source] = 0
    
    queue = [(0, source)]
    # print(queue)
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distance[current_node]:
            continue
        
        for neighbor, weight in graph[str(current_node)].items():
            distance_through_current_node = current_distance + weight
            if distance_through_current_node < distance[neighbor]:
                distance[neighbor] = distance_through_current_node
                heapq.heappush(queue, (distance[neighbor], neighbor))
                
    return distance

if __name__ == "__main__":
    source = 0
    graph = {
        '0' : {'1': 4, '7': 8},
        '1' : {'0': 4, '2': 8, '7': 11},
        '2' : {'1': 8, '3': 7, '5': 4, '8':2},
        '3' : {'2': 7, '4': 9, '5': 14},
        '4' : {'3': 9, '5': 10},
        '5' : {'2': 4, '3': 14, '4': 10, '6': 2},
        '6' : {'5': 2, '7': 1, '8': 6},
        '7' : {'0': 8, '1': 11, '6': 1, '8': 7},
        '8' : {'2': 2, '6': 6, '7': 7}
    }
    
    res = dijkstra(graph, source)
    print("Shortest distance between source and destination is: ", res)
