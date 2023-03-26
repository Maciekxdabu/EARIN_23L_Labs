import mazeSolverProgram
import mazeFileInputOutput
import heuristics

mazeFileName = "maze78.txt"
mazeFilePath = mazeFileInputOutput.getMazeSavePath(mazeFileName)

p = mazeSolverProgram.MazeSolverProgram(heuristics.h2, mazeFilePath)
p.run()
