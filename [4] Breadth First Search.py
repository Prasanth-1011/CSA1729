from collections import deque

def bfs(graph, start):
    visited, queue = set(), deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(set(graph.get(node, [])) - visited)

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
    start_node = input("Enter the Starting Node For BFS Traversal: ")
    print("BFS Traversal:")
    bfs(graph, start_node)
