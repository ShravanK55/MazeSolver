"""
Maze Solver - A-Star (A*) Algorithm

A module implementing the A* algorithm to solve mazes.

Author: shravan@usc.edu (5451873903)

"""

import heapq
from vector import line_distance


def a_star(graph, start, end):
    """
    This is a function implementing the A-Star algorithm to find paths in a graph, given a start and end node.

    Args:
        graph(Graph): Graph to perform the pathfinding on.
        start(Vector): Position to start the search at.
        end(Vector): Position to find a path to in the graph.

    Returns:
        (success, path, cost): Whether a path was found, path from the start node to the end node in the graph and the
            cost of each point in the path.

    """
    start_node = graph.get_node(start)
    end_node = graph.get_node(end)
    start_node.heuristic = int(line_distance(start_node.position, end_node.position))

    if (start_node is None) or (end_node is None):
        return False, None, None

    a_star_queue = [start_node]
    visited = {str(start_node): True}
    parents = {}

    heapq.heapify(a_star_queue)
    while len(a_star_queue) != 0:
        node = heapq.heappop(a_star_queue)

        if node == end_node:
            break

        neighbours = graph.get_neighbours_with_costs(node)

        for neighbour, cost in neighbours.items():
            if not visited.get(str(neighbour), False):
                neighbour.cost = cost + node.cost
                neighbour.heuristic = int(line_distance(neighbour.position, end_node.position))
                heapq.heappush(a_star_queue, neighbour)
                parents[neighbour] = node
                visited[str(neighbour)] = True

    else:
        return False, None, None

    node = parents.get(end_node)
    path = [end_node]
    while node is not None:
        path.insert(0, node)
        node = parents.get(node)

    return True, path, end_node.cost
