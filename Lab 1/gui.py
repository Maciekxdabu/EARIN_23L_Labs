import os
import numpy
from colorama import init as colorama_init
from colorama import Back
from colorama import Fore
from colorama import Style
import program_classes as pc
import constants as c


def initConsole():
    colorama_init()


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def consoleGetOptionInt() -> str:
    inputName = "option"
    test = None
    while test == None:
        print("0. quit program")
        print("1. show unsolved maze")
        print("2. show solved maze")
        print("3. show step by step solution")
        inputText = "".join(["Give integer for: ", inputName, " = "])
        given = input(inputText)
        try:
            test = int(given)
            if (test < 1):
                quit()
        except ValueError:
            print("INCORRECT INPUT TYPE OF:", given)
            print("TRY AGAIN (give an integer from 0 to 3 - inclusive)")
            test = None
    return test


def applySearchStepToMaze(maze: numpy.array, step: pc.step):
    # TEMP do not overwrite the start or end of tile path
    if (not (maze[step.evaluatedTile.y][step.evaluatedTile.x] == c.MAZE_START or maze[step.evaluatedTile.y][step.evaluatedTile.x] == c.MAZE_END)):
        maze[step.evaluatedTile.y][step.evaluatedTile.x] = c.ALG_EXPLORED
    for newFrontier in step.newFrontierTiles:
        # TEMP do not overwrite the start or end tile path
        if (not (maze[newFrontier.y][newFrontier.x] == c.MAZE_START or maze[newFrontier.y][newFrontier.x] == c.MAZE_END)):
            maze[newFrontier.y][newFrontier.x] = c.ALG_FRONTIER
    return maze


def applyPathMarkingToMaze(maze: numpy.array, pathTile: pc.tile):
    # TEMP do not overwrite the start or end tile path
    if (not (maze[pathTile.y][pathTile.x] == c.MAZE_START or maze[pathTile.y][pathTile.x] == c.MAZE_END)):
        maze[pathTile.y][pathTile.x] = c.ALG_PATH
    return maze


def printMazeWithFrame(maze: numpy.array):
    # get max length of item in array
    horizontalMazeBorderLine = horizontalMazeBorder(maze)

    lines = []
    lines.append(horizontalMazeBorderLine)
    for row in maze:
        lines.append(
            wrapInMazeBorder(
                ''.join(colorTileBack(str(x)) for x in row)))
    lines.append(removeStyle(horizontalMazeBorderLine))
    print('\n'.join(lines))


def horizontalMazeBorder(maze: numpy.array):
    return wrapInMazeBorder(colorWhiteBack(''.join('--' for x in maze[0])))


def wrapInMazeBorder(s: str):
    return colorWhiteBack('|') + s + colorWhiteBack('|')


def colorGrayBack(s: str):
    return addColor(f'{Back.WHITE}', s)


# TODO: make Start/End tiles have their background be the same as C/F/O but have their Fore be indicative of their function (start: green, end: red)
def colorTileBack(s: str):
    if (s == c.MAZE_EMPTY_SPACE):
        return colorWhiteBack(s+' ')
    if (s == c.MAZE_START):
        return colorGreenBack(s+' ')
    if (s == c.MAZE_END):
        return colorRedBack(s+' ')
    if (s == c.ALG_EXPLORED):
        return colorBlueBack(s+' ')
    if (s == c.ALG_PATH):
        return colorYellowBack(s+' ')
    if (s == c.ALG_FRONTIER):
        return colorCyanBack(s+' ')
    return colorBlackBack(s+' ')


def colorBlackBack(s: str):
    return addColor(f'{Back.BLACK}', s)


def colorWhiteBack(s: str):
    return addColor(f'{Back.WHITE}', s)


def colorBlueBack(s: str):
    return addColor(f'{Back.BLUE}', s)


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
