def dfs(graph, node, visited):
    visited.add(node)
    print(node)  # Process the node

    neighbors = graph.get(node, [])  # Get neighbors or an empty list if node is not in graph
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def depth_first_search(graph, start):
    visited = set()
    dfs(graph, start, visited)

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
    print("Graph =", graph)
    start_node = input("Enter the Starting Node For DFS Traversal: ")
    print("DFS Traversal:")
    depth_first_search(graph, start_node)
