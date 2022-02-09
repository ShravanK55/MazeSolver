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

    def get_node(self, position):
        """
        Method to get the node for a given point.

        Args:
            position(Vector): Position at which we need to get the node.

        Returns:
            (node): Node at the given position.

        """
        return self.nodes.get(str(position)) if self.is_valid(position) else None

    def get_neighbours(self, node):
        """
        Method to get the neighbours for a given node.

        Args:
            node(Node): Node to get the neighbours for.

        Returns:
            (neighbours): List of valid neighbours for the node.

        """
        return [self.get_node(neighbour) for neighbour in node.neighbours.values()]

    def get_neighbours_with_costs(self, node):
        """
        Method to get the neighbours and their costss. for a given node.

        Args:
            node(Node): Node to get the neighbours for.

        Returns:
            (neighbour_cost_map): Map of valid neighbours with their costs for each node.

        """
        neighbour_cost_map = {}

        for action, neighbour in node.neighbours.items():
            neighbour_node = self.get_node(neighbour)
            cost = get_action_cost(action)
            neighbour_cost_map[neighbour_node] = cost

        return neighbour_cost_map

    def is_valid(self, position):
        """
        Method to check if a position is valid (within the graph's bounds).

        Args:
            position(Vector): Position to check.

        Returns:
            (is_valid): Whether the position is valid or not.

        """
        return ((position.x >= 0 and position.x < self.bounds.x) and
                (position.y >= 0 and position.y < self.bounds.y) and
                (position.z >= 0 and position.z < self.bounds.z))


class Node(object):
    """
    A class that implements a node in a graph.
    """

    def __init__(self, position, actions=None, cost=0, heuristic=0, parent=None):
        """
        Method to initialize the graph.

        Args:
            position(Vector): Position vector of the node.
            actions(list): List of actions we can take at the node.
            cost(int): Cost to reach the node. Only for use in pathfinding. Defaults to 0.
            heuristic(int): Heuristic to reach the target node. Only for use in pathfinding. Defaults to 0.
            parent(Node): Parent/neighbour of the node. Only for use in pathfinding. Defaults to None.

        """
        self.position = position
        self.neighbours = {}
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent
        self.visited = False

        if actions is not None:
            for action in actions:
                self.neighbours[action] = get_neighbour(position, action)

    def __repr__(self):
        """
        Method to represent a node as a string.

        Returns:
            (str): String representation of a node.

        """
        return str(self.position)

    def __eq__(self, other):
        """
        Method to check whether two nodes are equal.

        Args:
            other(Node): Other node to compare to.

        Returns:
            (bool): Whether the two nodes are equal.

        """
        return self.position == other.position

    def __lt__(self, other):
        """
        Method to compare the costs of two nodes. This is primarily used for comparison of nodes for operations in
        a priority queue, such as for the UCS and A* algorithms.
        NOTE: The setting of cost and heuristic must be taken care of by the algorithm.

        Args:
            other(Node): Other node to compare to.

        Returns:
            (bool): Whether the node's cost is lesser than the other node's.

        """
        return self.total_cost < other.total_cost

    def __hash__(self):
        """
        Method to get the hash of a node.

        Returns:
            (hash): Returns the hash of the node.

        """
        return hash(str(self))

    @property
    def total_cost(self):
        """
        Method to get the total cost (Current + Heuristic) of a node.

        Returns:
            (total_cost): Total cost of the node.

        """
        return self.cost + self.heuristic

    def add_neighbours(self, actions):
        """
        Method to add neighbours to the node.

        Args:
            actions(list): List of actions we can take at the node.

        """
        for action in actions:
            self.neighbours[action] = get_neighbour(self.position, action)


def get_neighbour(position, action):
    """
    Method to get the neighbour for a position from an action.

    Args:
        position(Vector): Position at which we have to get the neighbours for.
        action(int): Action to take to get the neighbour.

    Returns:
        (neighbour): Vector of the neighbour.

    """
    action_map = {
        1:  Vector(position.x + 1, position.y, position.z),
        2:  Vector(position.x - 1, position.y, position.z),
        3:  Vector(position.x, position.y + 1, position.z),
        4:  Vector(position.x, position.y - 1, position.z),
        5:  Vector(position.x, position.y, position.z + 1),
        6:  Vector(position.x, position.y, position.z - 1),
        7:  Vector(position.x + 1, position.y + 1, position.z),
        8:  Vector(position.x + 1, position.y - 1, position.z),
        9:  Vector(position.x - 1, position.y + 1, position.z),
        10: Vector(position.x - 1, position.y - 1, position.z),
        11: Vector(position.x + 1, position.y, position.z + 1),
        12: Vector(position.x + 1, position.y, position.z - 1),
        13: Vector(position.x - 1, position.y, position.z + 1),
        14: Vector(position.x - 1, position.y, position.z - 1),
        15: Vector(position.x, position.y + 1, position.z + 1),
        16: Vector(position.x, position.y + 1, position.z - 1),
        17: Vector(position.x, position.y - 1, position.z + 1),
        18: Vector(position.x, position.y - 1, position.z - 1)
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
    return 10 if action < 7 else 14
