import heapq
 
class Graph:
    def __init__(self):
        self.nodes=set()
        self.edges={}
        self.distances={}
    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []  
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))
        self.edges[to_node].append((from_node, distance))
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

    def __str__(self):
        result = "Graph:\n"
        result += f"Nodes: {self.nodes}\n"
        result += f"Edges: {self.edges}\n"
        result += f"Distances: {self.distances}\n"
        return result

def create_graph():
    g = Graph()
    nodes = ['Food_Pickup_Location', 'PlaceA', 'PlaceB', 'PlaceC', 'PlaceD', 'PlaceE', 'PlaceF']
    for node in nodes:
        g.add_node(node)
    edges = [
        ('Food_Pickup_Location', 'PlaceA', 25),
        ('Food_Pickup_Location', 'PlaceB', 17),
        ('PlaceA', 'PlaceC', 30),
        ('PlaceB', 'PlaceD', 18),
        ('PlaceC', 'PlaceE', 9),
        ('PlaceD', 'PlaceF', 14),
        ('PlaceE', 'PlaceF', 40)]
    for from_node, to_node, weight in edges:
        g.add_edge(from_node, to_node, weight)
    #print (f'Print Graph: {g}')
    return g

def dijkstra(graph, start='Food_Pickup_Location'):
    pq = [(0, start)]
    #example structure [(5, 'PlaceA'), (7, 'PlaceB')] current_node with smallest distance popped first.
    distances = {node: float('inf') for node in graph.nodes} 
    # for unweighted graphs where there is no distance, visited should be checked. Courier case is weighted. 
    distances[start] = 0
    #keeps track of the shortest known distance from the starting node to each node
    #{'Food_Pickup_Location': 0, 'PlaceA': 5, 'PlaceB': 7, ...}
    previous_nodes = {node: None for node in graph.nodes}
    #track our route
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        #priority queue pops the smallest tentative distance and saves them in variables.
        #It guarantees that the next node popped is the one with the shortest tentative distance across all nodes. 
        #Not restricting to neigbhours of the last node; Allows for cases where shorter paths are discovered through a different node.
        if current_distance> distances[current_node]:
            continue
        #The distances dictionary acts as a filter, processing only the shortest distances.
        for neighbour, dist in graph.edges[current_node]:
            if (current_node, neighbour) in traffic:                 
                dist *= (1 + traffic[(current_node, neighbour)])
            distance= current_distance + dist

            if distance < distances[neighbour]:
                distances[neighbour]=distance
                previous_nodes[neighbour] = current_node 
                heapq.heappush(pq, (distance, neighbour))
                
    return distances, previous_nodes

def shortest_path(previous_nodes, destination):
    path = []
    current= destination

    while current is not None:
        path.append(current)
        current = previous_nodes[current]

    path.reverse()  # Reverse the path to get it from start to destination
    return path

def print_graph(graph):
    print("Places for courier to visit:", sorted(graph.nodes))

    print("\nTravel times between places (minutes):")
    for from_node, edges in graph.edges.items():
        for to_node, weight in edges:
            print(f"{from_node} --({weight})--> {to_node}")

def print_shortest_path(graph, previous_nodes, destination):
    path = shortest_path(previous_nodes, destination)
    total_weight = 0
    print(f"Shortest path to {destination} for our courier: ", end="")
    for i in range(len(path) - 1):
        from_node = path[i]
        to_node = path[i + 1]
        weight = graph.distances[(from_node, to_node)]
        total_weight += weight
        print(f"{from_node} --({weight})--> ", end="")
    print(f"{path[-1]}")
    print(f"Total travel time of the shortest path: {total_weight} minutes--food delivered hot and fresh!")

if __name__ == "__main__":
    g=create_graph()
    print_graph(g)
    destination='PlaceF' 
    traffic = {
        ('PlaceA', 'PlaceB'): 0.2,  # 20% increase in travel time
        ('PlaceB', 'PlaceD'): 0.1,      # 10% increase
    }
    if g is not None:  # Check if the graph was successfully created
        try:
            distances, previous_nodes =dijkstra(g)  # Run Dijkstra's algorithm on the graph
            print("Shortest distances:", distances)
            #print("Previous nodes:", previous_nodes)            
            print_shortest_path(g, previous_nodes, destination)
        except Exception as e:
            print(f"Error during Dijkstra's algorithm: {e}")
    else:
        print('Graph is not initiated!')
    
    