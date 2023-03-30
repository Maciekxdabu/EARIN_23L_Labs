import maze_solver_program
import maze_generator
import maze_file_input_output
import heuristics

import numpy as np
import pandas as pd


def compare():
    # START Config
    # dimensions of the mazes to solve
    maze_width = 101
    maze_height = 101
    # how many mazes to solve and get results of
    maze_count = 1000
    # END config

    results = []
    for x in range(maze_count):
        print(f"Comparing maze {x+1}/{maze_count}")
        maze_file_name = f"maze{x}.txt"
        maze_file = maze_file_input_output.get_maze_save_path(maze_file_name)
        maze_generator.generate_maze(maze_width, maze_height, maze_file)
        p1 = maze_solver_program.MazeSolverProgram(heuristics.h1,
                                                   path_to_maze_file=maze_file)
        p2 = maze_solver_program.MazeSolverProgram(heuristics.h2,
                                                   path_to_maze_file=maze_file)
        results1 = p1.solve()
        results2 = p2.solve()
        results.append(results1 + results2)
        print(f"    So1/So2: {np.divide(results1,results2)}")
        print(f"    Solver1: {results1} ")
        print(f"    Solver2: {results2} ")

    # Save results to xlsx
    # Specify column names
    column_names = ["Heuristic 1 Time", "Number of steps", "length of path",
                    "Heuristic 2 Time", "Number of steps", "length of path"]
    # create a DataFrame from the array
    df = pd.DataFrame(results, columns=column_names)

    # write the DataFrame to an Excel file
    df.to_excel("output.xlsx", index=False)


compare()
