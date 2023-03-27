import maze_solver_program
import maze_file_input_output
import heuristics

mazeFileName = "maze96.txt"
mazeFilePath = maze_file_input_output.getMazeSavePath(mazeFileName)

p = maze_solver_program.MazeSolverProgram(heuristics.h2, mazeFilePath)
p.run()
