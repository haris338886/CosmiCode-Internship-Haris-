def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited
    visited.add(start)
    print(start, end=' ')

    # Recur for all the adjacent vertices
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal starting from node A:")
dfs(graph, 'A')
