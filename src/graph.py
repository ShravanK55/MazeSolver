"""
Maze Solver - Graph

This module implements a graph data structure used to represent the maze.

Author: shravan@usc.edu (5451873903)

"""

from vector import Vector


class Graph(object):
    """
    A module that implements a graph data structure which represents the maze to solve.
    """

    def __init__(self, nodes=None, bounds=None):
        """
        Method to initialize the graph.

        Args:
            nodes(list): List of nodes in the graph. Defaults to None.
            bounds(Vector): Bounds of the graph. Defaults to None.

        """
        self.nodes = {}
        self.bounds = bounds
        if nodes is not None:
            for node in nodes:
                self.nodes[str(node)] = node

    def __repr__(self):
        """
        Method to represent a graph as a string.

        Returns:
            (str): String representation of a graph.

        """
        base_str = "Bounds: {}, Nodes: {}"
        points = [str(node) for node in self.nodes]
        return base_str.format(self.bounds, "  ".join(points))

    def add_node(self, node):
        """
        Method to add a node to the graph.

        Args:
            node(Node): Node to add to the graph.

        """
        self.nodes[str(node)] = node

    def get_node(self, point):
        """
        Method to get the node for a given point.

        Args:
            point(Vector): Point to get the node for.

        Returns:
            (node): Node at the given point.

        """
        return self.nodes[str(point)] if self.is_valid(point) else None

    def is_valid(self, point):
        """
        Method to check if a point is valid (within the graph's bounds).

        Args:
            point(Vector): Point to check.

        Returns:
            (is_valid): Whether the point is valid or not.

        """
        return ((point.x >= 0 and point.x < self.bounds.x) and
                (point.y >= 0 and point.y < self.bounds.y) and
                (point.z >= 0 and point.z < self.bounds.z))


class Node(object):
    """
    A class that implements a node in a graph.
    """

    def __init__(self, point, actions=None):
        """
        Method to initialize the graph.

        Args:
            point(Vector): Position vector of the node.
            actions(list): List of actions we can take at the node.

        """
        self.point = point
        self.neighbours = {}

        if actions is not None:
            for action in actions:
                self.neighbours[action] = get_neighbour(point, action)

    def __repr__(self):
        """
        Method to represent a node as a string.

        Returns:
            (str): String representation of a node.

        """
        return str(self.point)

    def add_neighbours(self, actions):
        """
        Method to add neighbours to the node.

        Args:
            actions(list): List of actions we can take at the node.

        """
        for action in actions:
            self.neighbours[action] = get_neighbour(self.point, action)


def get_neighbour(point, action):
    """
    Method to get the neighbour for a point from an action.

    Args:
        point(Vector): Point at which we have to get the neighbours for.
        action(int): Action to take to get the neighbour.

    Returns:
        (neighbour): Vector of the neighbour.

    """
    action_map = {
        1:  Vector(point.x + 1, point.y, point.z),
        2:  Vector(point.x - 1, point.y, point.z),
        3:  Vector(point.x, point.y + 1, point.z),
        4:  Vector(point.x, point.y - 1, point.z),
        5:  Vector(point.x, point.y, point.z + 1),
        6:  Vector(point.x, point.y, point.z - 1),
        7:  Vector(point.x + 1, point.y + 1, point.z),
        8:  Vector(point.x + 1, point.y - 1, point.z),
        9:  Vector(point.x - 1, point.y + 1, point.z),
        10: Vector(point.x - 1, point.y - 1, point.z),
        11: Vector(point.x + 1, point.y, point.z + 1),
        12: Vector(point.x + 1, point.y, point.z - 1),
        13: Vector(point.x - 1, point.y, point.z + 1),
        14: Vector(point.x - 1, point.y, point.z - 1),
        15: Vector(point.x, point.y + 1, point.z + 1),
        16: Vector(point.x, point.y + 1, point.z - 1),
        17: Vector(point.x, point.y - 1, point.z + 1),
        18: Vector(point.x, point.y - 1, point.z - 1)
    }

    return action_map[action]


def get_action_cost(action):
    """
    Method to get the cost of an action. The cost is 10 for axial movement (along the cardinal axes) and 14 for
    diagonal movement (along the planes).

    Args:
        action(int): Action to get the cost for.

    Returns:
        (cost): Cost of the action.

    """
    return 14 if action > 6 else 10
