
"""
DFS Traversal in Python
----------------------
This script demonstrates Depth-First Search (DFS) on a graph represented as an adjacency list.

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
Space Complexity: O(V), due to the recursion stack and visited set.

Author: abdullah salman
"""

def dfs(graph, start, visited=None):
    """
    Perform DFS traversal on a graph from a starting node.
    Args:
        graph (dict): Adjacency list of the graph.
        start: Starting node for DFS.
        visited (set): Set of already visited nodes.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def main():
    # Example graph as adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }

    print("DFS Traversal starting from node A:")
    dfs(graph, 'A')


if __name__ == "__main__":
    main()