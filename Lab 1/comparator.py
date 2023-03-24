import main
import maze_generator


def compare():
    results = []
    for x in range(100):
        # wrzucić do folderu a nie luzem
        maze_file = "maze"+x+".txt"
        maze_generator.generateMaze(maze_file)
        p1 = main.MazeSolver_Program(
            useSecondHeiristic=True, pathToMazeFile=maze_file)
        p2 = main.MazeSolver_Program(
            useSecondHeiristic=False, pathToMazeFile=maze_file)
        results1 = p1.solve(maze_file)
        results2 = p2.solve(maze_file)
        results.append([results1, results2])

        # TODO save results to xlsx
        # a w excelu
        # por res1.stepNumber / res2StepNumber
        # res1.time / res2.time
compare()
