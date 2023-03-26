import mazeSolverProgram
import maze_generator
import mazeFileInputOutput
import heuristics

import numpy as np
import pandas as pd


def compare():
    mazeWidth = 101
    mazeHeight = 101
    results = []
    mazeCount = 1000
    for x in range(mazeCount):
        print(f"Comparing maze {x+1}/{mazeCount}")
        # wrzucić do folderu a nie luzem
        mazeFileName = f"maze{x}.txt"
        maze_file = mazeFileInputOutput.getMazeSavePath(mazeFileName)
        maze_generator.generate_maze(mazeWidth, mazeHeight, maze_file)
        p1 = mazeSolverProgram.MazeSolverProgram(heuristics.h1,
                                                 pathToMazeFile=maze_file)
        p2 = mazeSolverProgram.MazeSolverProgram(heuristics.h2,
                                                 pathToMazeFile=maze_file)
        results1 = p1.solve()
        results2 = p2.solve()
        results.append(results1 + results2)
        print(f"    So1/So2: {np.divide(results1,results2)}")
        print(f"    Solver1: {results1} ")
        print(f"    Solver2: {results2} ")
        # por res1.stepNumber / res2StepNumber
        # res1.time / res2.time

    # Save results to xlsx
    # Specify column names
    column_names = ["Heuristic 1 Time", "Number of steps", "length of path",
                    "Heuristic 2 Time", "Number of steps", "length of path"]
    # create a DataFrame from the array
    df = pd.DataFrame(results, columns=column_names)

    # write the DataFrame to an Excel file
    df.to_excel("output.xlsx", index=False)


compare()
