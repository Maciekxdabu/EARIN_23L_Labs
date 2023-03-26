import mazeSolverProgram
import mazeFileInputOutput
import heuristics

mazeFileName = "maze96.txt"
mazeFilePath = mazeFileInputOutput.getMazeSavePath(mazeFileName)

p = mazeSolverProgram.MazeSolverProgram(heuristics.h2, mazeFilePath)
p.run()
