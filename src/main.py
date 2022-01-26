"""
Maze Solver - A program which solves a maze read from an input file.

This module implements the main program that runs the pathfinding algorithms (BFS, UCS and A*) on a maze defined by an
input file, and writes the optimal path to an output file.

Usage: python main.py

Author: shravan@usc.edu (5451873903)

"""

import argparse

from a_star import a_star
from bfs import bfs
from ucs import ucs
from utils import generate_maze


if __name__ == "__main__":
    # Getting args.
    parser = argparse.ArgumentParser(description='Module to perform pathfinding in graphs using different algorithms.')
    parser.add_argument("input", nargs='?', type=str, default="input.txt",
                        help="Input file path containing the graph and node information.")
    parser.add_argument("-o", "--output", type=str, default="output.txt",
                        help="Output file to store the results of the pathfinding algorithms.")
    args = parser.parse_args()

    input_file_path = args.input
    output_file_path = args.output

    # Reading input file.
    input_file_contents = []
    with open(input_file_path, 'r') as f:
        input_file_contents = f.readlines()

    # Generating the maze.
    algorithm, start, end, graph = generate_maze(input_file_contents)
    print("Algorithm: {}, Start: {}, End: {}".format(algorithm, start, end))

    # Running the pathfinding algorithms.
    success, path, cost = False, None, None
    if algorithm == "BFS":
        success, path, cost = bfs(graph, start, end)
        print("Sucess: {}".format(success))
        print("Cost: {}".format(cost))
        print("Path Length: {}".format(len(path)))

    elif algorithm == "UCS":
        success, path, cost = ucs(graph, start, end)
        print("Sucess: {}".format(success))
        print("Cost: {}".format(cost))
        print("Path Length: {}".format(len(path)))

    elif algorithm == "A*":
        success, path, cost = a_star(graph, start, end)
        print("Sucess: {}".format(success))
        print("Cost: {}".format(cost))
        print("Path Length: {}".format(len(path)))

    # Writing the path to the output file.
    if success:
        with open(output_file_path, 'w') as f:
            f.truncate(0)
            f.write("{}\n".format(cost))
            f.write("{}\n".format(len(path)))

            last_cost = 0
            for node in path:
                f.write("{} {} {} {}\n".format(node.position.x, node.position.y, node.position.z,
                                               node.cost - last_cost))
                last_cost = node.cost
    else:
        with open(output_file_path, 'w') as f:
            f.truncate(0)
            f.write("FAIL\n")
