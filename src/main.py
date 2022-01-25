"""
Maze Solver - A program which solves a maze read from an input file.

This module implements the main program that runs the pathfinding algorithms (BFS, UCS and A*) on a maze defined by an
input file, and writes the optimal path to an output file.

Usage: python main.py

Author: shravan@usc.edu (5451873903)

"""

import argparse

from utils import generate_maze


if __name__ == "__main__":
    # Getting args.
    parser = argparse.ArgumentParser(description='Module to compute the sequence alignment of two strings.')
    parser.add_argument("input", nargs='?', type=str, default="input.txt",
                        help="Input file path containing the string generator arguments.")
    parser.add_argument("-o", "--output", type=str, default="output.txt",
                        help="Output file to store the results of the algorithm.")
    args = parser.parse_args()

    input_file_path = args.input
    output_file_path = args.output

    # Reading input file.
    input_file_contents = []
    with open(input_file_path, 'r') as f:
        input_file_contents = f.readlines()

    # Generating input.
    algorithm, start, end, graph = generate_maze(input_file_contents)
    print("Algorithm: {}, Start: {}, End: {}".format(algorithm, start, end))
    print("Graph: {}".format(graph))

    """
    # Running the algorithm.
    tracemalloc.start()
    start_time = time.perf_counter()
    output_str_1, output_str_2, cost = get_minimum_sequence_alignment(input_str_1, input_str_2)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    _, memory_usage = tracemalloc.get_traced_memory()
    memory_usage = memory_usage / 1024
    tracemalloc.stop()

    # Writing to output file.
    with open(output_file_path, 'w') as f:
        f.truncate(0)
        f.write("{}\n".format(output_str_1[:50] + ' ' + output_str_1[-50:]))
        f.write("{}\n".format(output_str_2[:50] + ' ' + output_str_2[-50:]))
        f.write("{}\n".format(cost))
        f.write("{}\n".format(elapsed_time))
        f.write("{}\n".format(memory_usage))
    """
