"""
Maze Solver - Uniform Cost Search (UCS) Algorithm

A module implementing the UCS algorithm to solve mazes.

Author: shravan@usc.edu (5451873903)

"""

import heapq


def ucs(graph, start, end):
    """
    This is a function implementing the Uniform Cost Search algorithm to find paths in a graph, given a start and end
    node.

    Args:
        graph(Graph): Graph to perform the pathfinding on.
        start(Vector): Position to start the search at.
        end(Vector): Position to find a path to in the graph.

    Returns:
        (success, path, cost): Whether a path was found, path from the start node to the end node in the graph and the
            cost of each point in the path.

    """
    # Get the start and end nodes from the graph.
    start_node = graph.get_node(start)
    end_node = graph.get_node(end)

    if (start_node is None) or (end_node is None):
        return False, None, None

    # Initialize the UCS priority queue.
    ucs_queue = [start_node]
    heapq.heapify(ucs_queue)
    visited = {str(start_node): True}
    parents = {}

    # Searching the graph for the end node.
    while len(ucs_queue) != 0:
        node = heapq.heappop(ucs_queue)

        if node == end_node:
            break

        neighbours = graph.get_neighbours_with_costs(node)
        for neighbour, cost in neighbours.items():
            if not visited.get(str(neighbour), False):
                # Cost of traversing each node in UCS is the cost of traversing to the neighbour + cost of getting
                # to the parent.
                neighbour.cost = cost + node.cost
                heapq.heappush(ucs_queue, neighbour)
                parents[neighbour] = node
                visited[str(neighbour)] = True

    # If the UCS queue is empty without finding the end node, then we can't reach it.
    else:
        return False, None, None

    # Getting the path from the end node to the source by traversing the parents.
    node = parents.get(end_node)
    path = [end_node]
    while node is not None:
        path.insert(0, node)
        node = parents.get(node)

    return True, path, end_node.cost
