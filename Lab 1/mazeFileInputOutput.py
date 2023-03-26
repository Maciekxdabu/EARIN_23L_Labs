import os
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


def saveMaze(filePath: str, maze):
    # Get the directory path
    dir_path = os.path.dirname(filePath)

    # Create the directory if it doesn't exist
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Convert maze to string
    maze_str = ""
    for row in maze:
        maze_str += "".join(row) + "\n"

    # Write maze string to file (since we open file using "with" it closes the file correctly when it ends)
    with open(filePath, "w") as f:
        f.write(maze_str[:-1])


def getMazeSavePath(fileName: str) -> str:
    maze_dir = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    return os.path.join(maze_dir, fileName)
