import mazeSolverProgram
import maze_generator
import mazeFileInputOutput
import heuristics


def compare():
    mazeWidth = 25
    mazeHeight = 25
    results = []
    for x in range(2):
        # wrzucić do folderu a nie luzem
        mazeFileName = f"maze{x}.txt"
        maze_file = mazeFileInputOutput.getMazeSavePath(mazeFileName)
        maze_generator.generate_maze(mazeWidth, mazeHeight, maze_file)
        p1 = mazeSolverProgram.MazeSolverProgram(heuristics.h1,
                                                 # useSecondHeiristic=True,
                                                 pathToMazeFile=maze_file)
        p2 = mazeSolverProgram.MazeSolverProgram(heuristics.h2,
                                                 # useSecondHeiristic=False,
                                                 pathToMazeFile=maze_file)
        results1 = p1.solve()
        results2 = p2.solve()
        results.append([results1, results2])

        # TODO save results to xlsx
        # a w excelu
        # por res1.stepNumber / res2StepNumber
        # res1.time / res2.time

    for run in results:
        print(run)


compare()
