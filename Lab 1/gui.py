import os
import numpy
from colorama import init as colorama_init
from colorama import Back
from colorama import Style


def initConsole():
    colorama_init()


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
    horizontalMazeBorderLine = horizontalMazeBorder(maze, padding)

    lines = []
    lines.append(horizontalMazeBorderLine)
    for row in maze:
        lines.append(
            wrapInMazeBorder(
                ' '.join(colorTileBack(str(x).ljust(padding)) for x in row)))
    lines.append(removeStyle(horizontalMazeBorderLine))
    print('\n'.join(lines))


def horizontalMazeBorder(maze: numpy.array, padding: int):
    return wrapInMazeBorder(colorWhiteBack('-'.join('-'*padding for x in maze[0])))


def wrapInMazeBorder(s: str):
    return colorWhiteBack('|') + s + colorWhiteBack('|')


def colorGrayBack(s: str):
    return addColor(f'{Back.WHITE}', s)


def colorTileBack(s: str):
    if (s == 'O'):
        return colorCyanBack(s)
    if (s == 'S'):
        return colorGreenBack(s)
    if (s == 'E'):
        return colorRedBack(s)
    if (s == 'P'):
        return colorYellowBack(s)

    return colorBlackBack(s)


def colorBlackBack(s: str):
    return addColor(f'{Back.BLACK}', s)


def colorWhiteBack(s: str):
    return addColor(f'{Back.WHITE}', s)


def colorCyanBack(s: str):
    return addColor(f'{Back.CYAN}', s)


def colorGreenBack(s: str):
    return addColor(f'{Back.GREEN}', s)


def colorYellowBack(s: str):
    return addColor(f'{Back.YELLOW}', s)


def colorRedBack(s: str):
    return addColor(f'{Back.RED}', s)


def addColor(color, s: str):
    result = str(color) + s
    return result


def removeStyle(s: str):
    result = s + str(f'{Style.RESET_ALL}')
    return result
