from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)  # Process the node
            visited.add(node)
            neighbors = graph.get(node, [])  # Get neighbors or an empty list if node is not in graph
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

def create_graph():
    graph = {}
    num_edges = int(input("Enter Number of Edges: "))
    print("Enter Edges (Format 'Source White_Space Destination'):")
    for _ in range(num_edges):
        edge = input().split()
        source, destination = edge
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []
        graph[source].append(destination)
    return graph

if __name__ == "__main__":
    graph = create_graph()
    print("Graph = ", graph)
    start_node = input("Enter the Starting Node For BFS Traversal : ")
    print("BFS Traversal : ")
    bfs(graph, start_node)

# Enter Number of Edges: 6 | Enter Edges (Format 'Source White_Space Destination'):
# A B | A C | B D | B E | C F | E F
# Enter the Starting Node For DFS Traversal: A
