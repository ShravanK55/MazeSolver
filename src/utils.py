"""
Maze Solver - Utilies

This module implements utility methods for the maze solver modules.

Author: shravan@usc.edu (5451873903)

"""

from graph import Graph, Node
from vector import Vector


def generate_maze(file_contents):
    """
    Method to get the parameters of the maze from the contents of the input file.

    Args:
        file_contents(list): List of lines from the input file.

    Returns:
        (algorithm, start, end, graph): Returns the algorithm to use, the starting position in the graph, the ending
            position and the graph of the maze.

    """
    algorithm = file_contents[0].split('\n')[0]
    bounds = Vector.from_str(file_contents[1].split('\n')[0])
    start = Vector.from_str(file_contents[2].split('\n')[0])
    end = Vector.from_str(file_contents[3].split('\n')[0])
    num_points = int(file_contents[4].split('\n')[0])

    start_idx = 5
    nodes = []
    for offset in range(num_points):
        coords = file_contents[start_idx + offset].split('\n')[0].split(' ')
        point = Vector(int(coords[0]), int(coords[1]), int(coords[2]))
        actions = [int(coord) for coord in coords[3:]]
        node = Node(point, actions)
        nodes.append(node)

    graph = Graph(nodes, bounds)
    return algorithm, start, end, graph