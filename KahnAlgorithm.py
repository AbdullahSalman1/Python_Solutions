"""
KAHN'S ALGORITHM (BFS) - TOPOLOGICAL SORT
-----------------------------------------

What is this algorithm?
-----------------------
Kahn’s Algorithm is used to perform Topological Sorting of a Directed Acyclic Graph (DAG).

Topological sorting means:
→ Ordering nodes such that for every directed edge A → B, A appears before B.

-----------------------------------------
STEPS OF THE ALGORITHM:
-----------------------------------------

1. Compute indegree of every node
   - indegree = number of incoming edges

2. Initialize a queue
   - Add all nodes with indegree = 0 (no dependencies)

3. Process the queue (BFS style)
   - Pop a node from queue
   - Add it to result (final ordering)
   - Reduce indegree of its neighbors
   - If any neighbor becomes indegree = 0, add it to queue

4. Repeat until queue is empty

-----------------------------------------
TIME COMPLEXITY:
-----------------------------------------
O(V + E)

Where:
V = number of vertices (nodes)
E = number of edges

Each node and edge is processed exactly once.

-----------------------------------------
SPACE COMPLEXITY:
-----------------------------------------
O(V + E)
(for indegree map, queue, and result list)
"""

from collections import deque


def topological_sort(graph):
    """
    Performs topological sorting using Kahn's Algorithm (BFS approach).

    Parameters:
    -----------
    graph : dict
        Adjacency list representation of DAG
        Example:
        {
            '1': ['2', '3'],
            '2': ['4', '5'],
            ...
        }

    Returns:
    --------
    list
        A valid topological ordering of nodes
    """

    # Step 1: Initialize indegree of all nodes to 0
    indegree = {node: 0 for node in graph}

    # Step 2: Compute indegree of each node
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    # Step 3: Add all nodes with indegree 0 to queue
    queue = deque()
    for node in graph:
        if indegree[node] == 0:
            queue.append(node)

    result = []

    # Step 4: Process queue (BFS)
    while queue:
        node = queue.popleft()
        result.append(node)

        # Reduce indegree of neighbors
        for neighbor in graph[node]:
            indegree[neighbor] -= 1

            # If indegree becomes 0, add to queue
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result


# -----------------------------
# MAIN FUNCTION (ENTRY POINT)
# -----------------------------
if __name__ == "__main__":

    graph = {
        '1': ['2', '3'],
        '2': ['4', '5'],
        '3': ['5'],
        '4': [],
        '5': []
    }

    print("Topological Sort Order:")
    print(topological_sort(graph))