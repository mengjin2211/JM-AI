def dfs(graph, start):
    visited = set()
    stack = [start]
    traversal_order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)   
            stack.extend(graph[node])   
    return traversal_order

from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    traversal_order = []
    while queue:
        node = queue.popleft()   
        traversal_order.append(node)  # Record the order of traversal
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal_order

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
dfs_result = dfs(graph, start_node)
print("DFS Traversal Order:", dfs_result)
bfs_result = bfs(graph, start_node)
print("BFS Traversal Order:", bfs_result)
