"""
Maze Solver - Breadth First Search Algorithm

A module implementing the BFS algorithm to solve mazes.

Author: shravan@usc.edu (5451873903)

"""


def bfs(graph, start, end):
    """
    This is a function implementing the Breadth First Search algorithm to find paths in a graph, given a start and end
    node.

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

    if (start_node is None) or (end_node is None):
        return False, None, None

    bfs_queue = [start_node]
    visited = {str(start_node): True}
    parents = {}

    while len(bfs_queue) != 0:
        node = bfs_queue.pop(0)

        if node == end_node:
            break

        neighbours = graph.get_neighbours(node)

        for neighbour in neighbours:
            if not visited.get(str(neighbour), False):
                bfs_queue.append(neighbour)
                parents[neighbour] = node
                visited[str(neighbour)] = True

    else:
        return False, None, None

    node = parents.get(end_node)
    path = [end_node]
    while node is not None:
        path.insert(0, node)
        node = parents.get(node)

    return True, path, len(path) - 1
