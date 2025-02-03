import time
from collections import defaultdict, deque
import random

# Define a large graph for testing
def create_large_graph(num_nodes, num_edges):
    graph = defaultdict(list)
    for _ in range(num_edges):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v and v not in graph[u]:  # Avoid self-loops and duplicate edges
            graph[u].append(v)
            graph[v].append(u)  # Ensure the graph is undirected
    return graph

# DFS Implementation to find the shortest path
def dfs_shortest_path(graph, start, target):
    visited = set()
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == target:
                return path
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

# BFS Implementation to find the shortest path
def bfs_shortest_path(graph, start, target):
    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()
        if node == target:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# Test performance
def test_performance(graph, start_node, target_node):
    print("Testing DFS for shortest path...")
    start_time = time.time()
    dfs_path = dfs_shortest_path(graph, start_node, target_node)
    dfs_time = time.time() - start_time
    print(f"DFS took {dfs_time:.4f} seconds.")
    #print(f"DFS Path: {dfs_path}")
    print("Testing BFS for shortest path...")
    start_time = time.time()
    bfs_path = bfs_shortest_path(graph, start_node, target_node)
    bfs_time = time.time() - start_time
    print(f"BFS took {bfs_time:.4f} seconds.")
    #print(f"BFS Path: {bfs_path}")
    return dfs_path, bfs_path

large_graph = create_large_graph(1000, 5000)

start_node = 0
target_node = 999
for i in range (10):
    dfs_path, bfs_path = test_performance(large_graph, start_node, target_node)

