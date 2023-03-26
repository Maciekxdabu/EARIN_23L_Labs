import mazeSolverProgram
import mazeFileInputOutput
import heuristics

mazeFileName = "maze0"
mazeFilePath = mazeFileInputOutput.getMazeSavePath(mazeFileName)

p = mazeSolverProgram.MazeSolverProgram(heuristics.h1, mazeFilePath)
