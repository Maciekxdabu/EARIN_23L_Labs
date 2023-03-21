import numpy as np
from colorama import init as colorama_init
from colorama import Back
from colorama import Fore
from colorama import Style
import program_classes as pc
import constants as c
import os


def loadMaze() -> np.array:
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))

    file_path = os.path.join(
        __location__, "maze.txt")

    mazeFile = loadedMaze = open(file_path, "r")
    loadedMaze = mazeFile.read()
    mazeFile.close()
    loadedMaze = loadedMaze.split("\n")
    listOfLists = []

    for x in loadedMaze:
        # split the line into single character elements
        listOfLists.append(list(x))

    finalMaze = np.array(listOfLists)

    return finalMaze
