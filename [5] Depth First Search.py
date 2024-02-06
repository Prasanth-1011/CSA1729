def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def create_graph():
    graph = {}
    for _ in range(int(input("Enter Number of Edges: "))):
        source, destination = input("Enter Edge (Format 'Source Destination'): ").split()
        graph.setdefault(source, []).append(destination)
        graph.setdefault(destination, [])
    return graph

if __name__ == "__main__":
    graph = create_graph()
    print("Graph =", graph)
    start_node = input("Enter the Starting Node For DFS Traversal: ")
    print("DFS Traversal:")
    dfs(graph, start_node)
