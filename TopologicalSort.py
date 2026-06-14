
"""
Topological Sort using Depth-First Search (DFS)
------------------------------------------------

What is Topological Sort?
------------------------
Topological sorting for Directed Acyclic Graphs (DAGs) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
It is used in scenarios like task scheduling, course prerequisite ordering, build systems, and more.

Algorithm:
----------
This implementation uses DFS. We recursively visit all neighbors of a node, and after visiting all descendants, we add the node to a stack. The reverse of this stack gives the topological order.

Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
Space Complexity: O(V), for the visited set and recursion stack.

Example:
--------
Given the following graph:

    A
   / \
  B   C
 / \ / \
D  E F  G

Possible topological orderings: [A, C, G, F, B, E, D], [A, B, E, D, C, F, G], etc.

Usage:
------
Run this file directly to see the topological sort of the example graph.
"""



def dfs(graph, node, visited, stack):
    """
    Recursive helper function for DFS traversal.
    Adds nodes to stack after visiting all descendants.
    """
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    stack.append(node)  # Append node after visiting all its neighbors


def topological_sort(graph):
    """
    Returns a list of nodes in topological order for the given DAG.
    """
    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, stack)
    return stack[::-1]  # Reverse the stack to get the order



if __name__ == "__main__":
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

    print("Adjacency List:")
    for node, neighbors in graph.items():
        print(f"  {node}: {neighbors}")

    order = topological_sort(graph)
    print("\nTopological Sort Order:")
    print(order)