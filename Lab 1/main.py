import maze_solver_program
import maze_file_input_output
import heuristics

mazeFileName = "maze1.txt"
mazeFilePath = maze_file_input_output.getMazeSavePath(mazeFileName)
displayStepSize = 1

p = maze_solver_program.MazeSolverProgram(
    heuristics.h2, mazeFilePath, displayStepSize)
p.run()
