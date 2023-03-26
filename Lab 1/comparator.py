import mazeSolverProgram
import maze_generator
import mazeFileInputOutput
import heuristics

import numpy as np


def compare():
    mazeWidth = 47
    mazeHeight = 47
    results = []
    mazeCount = 100
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
        results.append([results1, results2])
        print(f"    So1/So2: {np.divide(results1,results2)}")
        print(f"    Solver1: {results1} ")
        print(f"    Solver2: {results2} ")
        # TODO save results to xlsx
        # a w excelu
        # por res1.stepNumber / res2StepNumber
        # res1.time / res2.time


compare()
