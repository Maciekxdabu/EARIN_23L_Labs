import os
from time import sleep
import gui
import program_classes as pc
import numpy as np
import mazeFileInputOutput as mfio
import constants as c
import time


class MazeSolverProgram:

    __mazeFilePath: str

    def __init__(self, pathToMazeFile: str = None):
        if (pathToMazeFile == None):
            __location__ = os.path.realpath(os.path.join(
                os.getcwd(), os.path.dirname(__file__)))
            self.__mazeFilePath = os.path.join(__location__, "maze0.txt")
        else:
            self.__mazeFilePath = pathToMazeFile
        self.__clearStepsAndPath()

    def __clearStepsAndPath(self):
        self.__path.clear()
        self.__steps.clear()

        # O - empty, X - wall, S - start, E - end
    __maze = np.array([[c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL],
                       [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE,
                        c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                       [c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL,
                        c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                       [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE,
                        c.MAZE_START, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                       [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL,
                        c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL],
                       [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE,
                        c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                       [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL,
                        c.MAZE_EMPTY_SPACE, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                       [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE,
                        c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                       [c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_END, c.MAZE_EMPTY_SPACE,
                        c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                       [c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL,
                        c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL],
                       [c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL]])

    # temp: should be obtained by running the algorithm
    __solved_maze: np.array
    # get start and end tiles

    def __locateStartAndEndTiles(self):
        self.start_tile_np_arr = np.argwhere(self.__maze == c.MAZE_START)
        self.end_tile_np_arr = np.argwhere(self.__maze == c.MAZE_END)
        self.__end_tile = pc.tile(
            self.end_tile_np_arr[0][0], self.end_tile_np_arr[0][1])
        self.__start_tile: pc.tile = pc.tile(
            self.start_tile_np_arr[0][0], self.start_tile_np_arr[0][1])

    # start_tile_np_arr: np.ndarray[np.intp]
    # end_tile_np_arr: np.ndarray[np.intp]
    __end_tile: pc.tile
    __start_tile: pc.tile
    # TEMP idk what this is for but ok
    # print(self.h(state=self.startState))

    # Heuristic definition

    def __h1(self, state: pc.tile):
        return abs(state.x - self.__end_tile.x) + abs(state.y - self.__end_tile.y)

    # ----- Stepping of the algorithm

    # array containing steps
    __steps: list[pc.step] = []
    # keep track which step's outcome is displayed
    __currentStep: int
    # array containing path
    __path: list[pc.tile] = []
    # current path tile (displayed by gui)
    __currentPathTile: int

    __solutionTime: float  # solution time in seconds
    __solutionSteps: int
    __pathLength: int

    def __solveMazeWithMeasurements(self):
        self.__clearStepsAndPath()
        start_time = time.time()
        self.__solveMaze()
        end_time = time.time()
        self.__solutionTime = end_time - start_time
        self.__solutionSteps = len(self.__steps)
        self.__pathLength = len(self.__path)

    # the algorithm

    def __solveMaze(self):
        # initializing algorithm lists
        # 'frontier' is not a "queue.priorityQueue" because priorityQueue is not iterable: so we would not be able to check if the item is already in the queue easily
        frontier = [self.__start_tile]
        explored = []
        newFrontiers: list[pc.tile] = []

        # create a two-dimensional table for tiles, where each tile will store coordinates to their predecessor
        pathsMap: list[list[pc.tile]] = []
        # populate the paths array with elements
        for row in self.__maze:
            tempRow = []
            for tile in row:
                tempRow.append(pc.tile(-1, -1))
            pathsMap.append(tempRow)

        # main algorithm loop (runs as long as there are tiles to check)
        while len(frontier) > 0:
            # find the tile to check with the smallest heuristic value
            checkedTile = min(frontier, key=self.__h1)
            # check if we reached the end of the maze
            if checkedTile == self.__end_tile:
                newFrontiers.clear()
                self.__addNewStep(checkedTile, list(newFrontiers))
                # ----- Generate final path
                # generate the final path array
                finalPath = [self.__end_tile]
                currentTile = pathsMap[self.__end_tile.y][self.__end_tile.x]
                while currentTile != self.__start_tile:
                    finalPath.append(pc.tile(currentTile.y, currentTile.x))
                    currentTile = pathsMap[currentTile.y][currentTile.x]
                # reverse it to get list from beginning to the end
                finalPath.reverse()
                for tile in finalPath:
                    # add tile to the drawing system
                    self.__addNewPathToTile(tile)
                break

            # move current tile from frontier to explored
            explored.append(checkedTile)
            frontier.remove(checkedTile)

            # collect neighbors
            neighbors: list[pc.tile] = []
            # up tile
            if (checkedTile.x > 0 and self.__maze[checkedTile.y][checkedTile.x-1] != c.MAZE_WALL):
                neighbors.append(pc.tile(x=checkedTile.x-1, y=checkedTile.y))
            # down tile
            if (checkedTile.x < self.__maze.shape[1]-1 and self.__maze[checkedTile.y][checkedTile.x+1] != c.MAZE_WALL):
                neighbors.append(pc.tile(x=checkedTile.x+1, y=checkedTile.y))
            # left tile
            if (checkedTile.y > 0 and self.__maze[checkedTile.y-1][checkedTile.x] != c.MAZE_WALL):
                neighbors.append(pc.tile(x=checkedTile.x, y=checkedTile.y-1))
            # right tile
            if (checkedTile.y < self.__maze.shape[0]-1 and self.__maze[checkedTile.y+1][checkedTile.x] != c.MAZE_WALL):
                neighbors.append(pc.tile(x=checkedTile.x, y=checkedTile.y+1))

            newFrontiers.clear()

            # check neighboring tiles
            for tile in neighbors:
                # add tile to frontier if it was not in there already and if it has not been explored
                if (tile not in frontier):
                    if (tile not in explored):
                        frontier.append(tile)
                        newFrontiers.append(tile)
                        pathsMap[tile.y][tile.x].x = checkedTile.x
                        pathsMap[tile.y][tile.x].y = checkedTile.y
                # also move up node present in frontier if its heuristic is better than the currently checked one
                elif (self.__h1(tile) < self.__h1(checkedTile)):
                    frontier.remove(tile)
                    frontier.append(tile)
                    newFrontiers.append(tile)
                    pathsMap[tile.y][tile.x].x = checkedTile.x
                    pathsMap[tile.y][tile.x].y = checkedTile.y

            self.__addNewStep(checkedTile, list(newFrontiers))

    # gui functions and data
    def __prerenderSolvedMaze(self):
        self.__solved_maze = np.array(self.__maze)
        for step in self.__steps:
            self.__solved_maze = gui.applySearchStepToMaze(
                self.__solved_maze, step)

        for pathMarking in self.__path:
            self.__solved_maze = gui.applyPathMarkingToMaze(
                self.__solved_maze, pathMarking)

    # the maze state which is displayed by the program
    __displayed_maze: np.array
    __playing_forwards: bool = False
    __drawing_path: bool = False

    # function to add new steps
    def __addNewStep(self, currentTile: pc.tile, newStates: list[pc.tile]):
        self.__steps.append(pc.step(currentTile, newStates))

    # function to add new path to tile
    def __addNewPathToTile(self, tileToAdd: pc.tile):
        self.__path.append(tileToAdd)

    # helper functions to set the state of display
    def __displayUnsolvedMaze(self):
        self.__currentStep = 0
        self.__displayed_maze = np.array(self.__maze)

    def __displaySolvedMaze(self):
        self.__currentStep = len(self.__steps)
        self.__displayed_maze = np.array(self.__solved_maze)

    def __calculateNextDisplayedState(self):
        if not self.__drawing_path:
            step = self.__steps[self.__currentStep]
            self.__displayed_maze = gui.applySearchStepToMaze(
                self.__displayed_maze, step)
            self.__currentStep += 1
            sleep(0.1)

        else:
            pathTile = self.__path[self.__currentPathTile]
            self.__displayed_maze = gui.applyPathMarkingToMaze(
                self.__displayed_maze, pathTile)
            self.__currentPathTile += 1
            sleep(0.05)

    # main function

    def run(self):
        gui.initConsole()
        # load unsolved maze from file
        self.loadMazeFile()

        # solve the maze (generating steps)
        self.__solveMazeWithMeasurements()

        # start with showing unsolved maze
        self.__prerenderSolvedMaze()
        self.__displayUnsolvedMaze()

        while True:
            gui.clearConsole()
            print("Maze overview:")
            gui.printMazeWithFrame(self.__displayed_maze)
            gui.printSolutionMeasurements(
                self.__solutionTime, self.__solutionSteps, self.__pathLength)
            if (not self.__playing_forwards):
                input = gui.consoleGetOptionInt()
                match input:
                    case 1:  # show loaded maze
                        self.__displayUnsolvedMaze()
                    case 2:  # show solved maze
                        self.__displaySolvedMaze()
                    case 3:  # show step by step solution
                        self.__displayUnsolvedMaze()
                        self.__currentPathTile = 0
                        self.__playing_forwards = True
                        self.__drawing_path = False

            else:
                if (not self.__drawing_path and self.__currentStep >= len(self.__steps)):
                    self.__drawing_path = True
                if (self.__drawing_path and self.__currentPathTile >= len(self.__path)):
                    self.__playing_forwards = False
                    self.__drawing_path = False
                    continue
                self.__calculateNextDisplayedState()

    def loadMazeFile(self):
        self.__maze = mfio.loadMaze(self.__mazeFilePath)
        self.__locateStartAndEndTiles()

    # solve the maze and return solution statistics
    def solve(self):
        # load unsolved maze from file
        self.loadMazeFile()
        # solve the maze (generating steps)
        self.__solveMazeWithMeasurements()
        return [self.__solutionTime, self.__solutionSteps, self.__pathLength]


# p = MazeSolverProgram()
# p.run()
