import heapq

def prims_algorithm(graph, start_vertex):
  
    visited = set() 
    min_heap = [(0, start_vertex, None)]  
    mst_edges = [] 
    
    while min_heap:
        weight, current, parent = heapq.heappop(min_heap)
        
        if current not in visited:
            visited.add(current)
            if parent is not None:
                mst_edges.append((parent, current, weight))
            
            for neighbor_weight, neighbor in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (neighbor_weight, neighbor, current))
    
    return mst_edges

#Example
graph = {
    0: [(1, 1), (3, 2)],
    1: [(1, 0), (3, 2), (6, 3)],
    2: [(3, 0), (3, 1), (4, 3)],
    3: [(6, 1), (4, 2)]
}

start_vertex = 0
mst = prims_algorithm(graph, start_vertex)
print("Edges in MST:", mst)
