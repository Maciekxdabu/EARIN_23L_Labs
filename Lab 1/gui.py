import os
import numpy


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def consoleGetInt(inputName="") -> str:
    test = None
    while test == None:
        inputText = "".join(["Give integer for: ", inputName, " = "])
        given = input(inputText)
        try:
            test = int(given)
        except ValueError:
            print("INCORRECT INPUT TYPE OF:", given)
            print("TRY AGAIN (give an integer)")
            test = None
    return test


def printMaze(maze: numpy.array):
    lines = []
    for row in maze:
        lines.append(' '.join(str(x) for x in row))
    print('\n'.join(lines))


def printMazeWithFrame(maze: numpy.array):
    # get max length of item in array
    padding = len(max(maze.flatten(), key=len))

    lines = []
    lines.append('-'.join('-' for x in maze[0]))
    for row in maze:
        lines.append(' '.join(str(x).ljust(padding) for x in row))
    lines.append('-'.join('-'*padding for x in maze[0]))
    print('\n'.join(lines))
