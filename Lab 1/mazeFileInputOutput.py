import numpy as np


def loadMaze(filePath: str) -> np.array:
    mazeFile = loadedMaze = open(filePath, "r")
    loadedMaze = mazeFile.read()
    mazeFile.close()
    loadedMaze = loadedMaze.split("\n")
    listOfLists = []

    for x in loadedMaze:
        # split the line into single character elements
        listOfLists.append(list(x))

    finalMaze = np.array(listOfLists)

    return finalMaze
