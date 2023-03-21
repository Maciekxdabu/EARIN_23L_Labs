from time import sleep
import gui
import program_classes as pc
import numpy as np
import file_loading as fl
import constants as c


class MazeSolver_Program:
    # O - empty, X - wall, S - start, E - end
    maze = np.array([[c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL],
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
    # O - empty, X - wall, S - start, E - end, P - empty_on_path
    solved_maze = np.array([[c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL],
                            [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE,
                                c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                            [c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL,
                                c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                            [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.ALG_FRONTIER, c.ALG_EXPLORED,
                                c.MAZE_START, c.ALG_FRONTIER, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                            [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL, c.MAZE_WALL,
                                c.MAZE_WALL, c.ALG_PATH, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL],
                            [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL, c.ALG_FRONTIER, c.ALG_EXPLORED, c.ALG_PATH, c.ALG_FRONTIER,
                                c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                            [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL, c.MAZE_EMPTY_SPACE,
                                c.MAZE_WALL, c.ALG_PATH, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                            [c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE,
                                c.MAZE_WALL, c.ALG_PATH, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                            [c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_END,
                                c.ALG_PATH, c.ALG_FRONTIER, c.MAZE_EMPTY_SPACE, c.MAZE_EMPTY_SPACE, c.MAZE_WALL],
                            [c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL,
                                c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL],
                            [c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL, c.MAZE_WALL]])

    # get start and end tiles
    def locateStartAndEndTiles(self):
        self.start_tile_np_arr = np.argwhere(self.maze == c.MAZE_START)
        self.end_tile_np_arr = np.argwhere(self.maze == c.MAZE_END)
        self.end_tile = pc.tile(
            self.end_tile_np_arr[0][0], self.end_tile_np_arr[0][1])
        self.start_tile: pc.tile = pc.tile(
            self.start_tile_np_arr[0][0], self.start_tile_np_arr[0][1])

    start_tile_np_arr: np.ndarray[np.intp]
    end_tile_np_arr: np.ndarray[np.intp]
    end_tile: pc.tile
    start_tile: pc.tile
    # TEMP idk what this is for but ok
    # print(self.h(state=self.startState))

    # Heuristic definition

    def h(self, state: pc.tile):
        return abs(state.x - self.end_tile.x) + abs(state.y - self.end_tile.y)

    # ----- Stepping of the algorithm

    # array containing steps
    steps: list[pc.step] = []
    # keep track which step's outcome is displayed
    currentStep: int
    # array containing path
    path: list[pc.tile] = []
    # current path tile (displayed by gui)
    currentPathTile: int

    # the maze state which is displayed by the program
    displayed_maze: np.array
    playing_forwards: bool = False
    drawing_path: bool = False

    # function to add new steps
    def AddNewStep(self, currentTile: pc.tile, newStates: list[pc.tile]):
        self.steps.append(pc.step(currentTile, newStates))

    # function to add new path to tile
    def AddNewPathToTile(self, tileToAdd: pc.tile):
        self.path.append(tileToAdd)

    # the algorithm
    def solveMaze(self):
        # temp (need to actually solve the maze)
        self.solved_maze = self.solved_maze

        # initializing algorithm lists
        # 'frontier' is not a "queue.priorityQueue" because priorityQueue is not iterable: so we would not be able to check if the item is already in the queue easily
        frontier = [self.start_tile]
        explored = []
        newFrontiers: list[pc.tile] = []

        # main algorithm loop (runs as long as there are tiles to check)
        while len(frontier) > 0:
            # find the tile to check with the smallest heuristic value
            checkedTile = min(frontier, key=self.h)
            # check if we reached the end of the maze
            if checkedTile == self.end_tile:
                newFrontiers.clear()
                self.AddNewStep(checkedTile, list(newFrontiers))
                # TODO - Generate final path
                break

            # move current tile from frontier to explored
            explored.append(checkedTile)
            frontier.remove(checkedTile)

            # collect neighbors
            neighbors: list[pc.tile] = []
            # up tile
            if (checkedTile.x > 0 and self.maze[checkedTile.y][checkedTile.x-1] != c.MAZE_WALL):
                neighbors.append(pc.tile(x=checkedTile.x-1, y=checkedTile.y))
            # down tile
            if (checkedTile.x < self.maze.shape[1]-1 and self.maze[checkedTile.y][checkedTile.x+1] != c.MAZE_WALL):
                neighbors.append(pc.tile(x=checkedTile.x+1, y=checkedTile.y))
            # left tile
            if (checkedTile.y > 0 and self.maze[checkedTile.y-1][checkedTile.x] != c.MAZE_WALL):
                neighbors.append(pc.tile(x=checkedTile.x, y=checkedTile.y-1))
            # right tile
            if (checkedTile.y < self.maze.shape[0]-1 and self.maze[checkedTile.y+1][checkedTile.x] != c.MAZE_WALL):
                neighbors.append(pc.tile(x=checkedTile.x, y=checkedTile.y+1))

            newFrontiers.clear()

            # check neighboring tiles
            for tile in neighbors:
                # add tile to frontier if it was not in there already and if it has not been explored
                if (tile not in frontier):
                    if (tile not in explored):
                        frontier.append(tile)
                        newFrontiers.append(tile)
                # also move up node present in frontier if its heuristic is better than the currently checked one
                elif (self.h(tile) < self.h(checkedTile)):
                    frontier.remove(tile)
                    frontier.append(tile)
                    newFrontiers.append(tile)

            self.AddNewStep(checkedTile, list(newFrontiers))

        # TODO - REMOVE static code when done with algorithm

        # # add algorithm steps (make sure to append them in real order, so they are displayed properly)
        # # do not forget to add the start tile into step
        # newFrontier: list[pc.tile] = []
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x+1, y=self.start_tile.y))
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x-1, y=self.start_tile.y))
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x, y=self.start_tile.y+1))
        # self.AddNewStep(self.start_tile, list(newFrontier))

        # newFrontier.clear()
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x-2, y=self.start_tile.y))
        # self.AddNewStep(pc.tile(x=self.start_tile.x-1,
        #                 y=self.start_tile.y), list(newFrontier))

        # newFrontier.clear()
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x, y=self.start_tile.y+2))
        # self.AddNewStep(pc.tile(x=self.start_tile.x,
        #                 y=self.start_tile.y+1), list(newFrontier))

        # newFrontier.clear()
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x, y=self.start_tile.y+3))
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x+1, y=self.start_tile.y+2))
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x-1, y=self.start_tile.y+2))
        # self.AddNewStep(pc.tile(x=self.start_tile.x,
        #                 y=self.start_tile.y+2), list(newFrontier))

        # newFrontier.clear()
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x-2, y=self.start_tile.y+2))
        # self.AddNewStep(pc.tile(x=self.start_tile.x-1,
        #                 y=self.start_tile.y+2), list(newFrontier))

        # newFrontier.clear()
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x, y=self.start_tile.y+4))
        # self.AddNewStep(pc.tile(x=self.start_tile.x,
        #                 y=self.start_tile.y+3), list(newFrontier))

        # newFrontier.clear()
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x, y=self.start_tile.y+5))
        # self.AddNewStep(pc.tile(x=self.start_tile.x,
        #                 y=self.start_tile.y+4), list(newFrontier))

        # newFrontier.clear()
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x-1, y=self.start_tile.y+5))
        # newFrontier.append(
        #     pc.tile(x=self.start_tile.x+1, y=self.start_tile.y+5))
        # self.AddNewStep(pc.tile(x=self.start_tile.x,
        #                 y=self.start_tile.y+5), list(newFrontier))

        # # do not forget to add the end tile into step
        # newFrontier.clear()
        # self.AddNewStep(pc.tile(x=self.end_tile.x,
        #                 y=self.end_tile.y), list(newFrontier))

        # add path (make sure that list is ordered from start to finish for animation to be from start to finish)
        self.AddNewPathToTile(self.start_tile)
        self.AddNewPathToTile(
            pc.tile(x=self.start_tile.x, y=self.start_tile.y+1))
        self.AddNewPathToTile(
            pc.tile(x=self.start_tile.x, y=self.start_tile.y+2))
        self.AddNewPathToTile(
            pc.tile(x=self.start_tile.x, y=self.start_tile.y+3))
        self.AddNewPathToTile(
            pc.tile(x=self.start_tile.x, y=self.start_tile.y+4))
        self.AddNewPathToTile(
            pc.tile(x=self.start_tile.x, y=self.start_tile.y+5))
        self.AddNewPathToTile(
            pc.tile(x=self.end_tile.x, y=self.end_tile.y))

    # helper functions to set the state of display
    def displayUnsolvedMaze(self):
        self.currentStep = 0
        self.displayed_maze = np.array(self.maze)

    def displaySolvedMaze(self):
        self.currentStep = len(self.steps)
        self.displayed_maze = np.array(self.solved_maze)

    def calculateNextDisplayedState(self):
        if not self.drawing_path:
            step = self.steps[self.currentStep]
            self.displayed_maze = gui.applySearchStepToMaze(
                self.displayed_maze, step)
            self.currentStep += 1
            sleep(0.1)

        else:
            pathTile = self.path[self.currentPathTile]
            self.displayed_maze = gui.applyPathMarkingToMaze(
                self.displayed_maze, pathTile)
            self.currentPathTile += 1
            sleep(0.05)

    # main function

    def run(self):
        gui.initConsole()
        # TODO: load unsolved maze from file
        self.maze = fl.loadMaze()
        self.locateStartAndEndTiles()
        # TODO: solve the maze (generating steps)
        self.solveMaze()

        # start with showing unsolved maze
        self.displayUnsolvedMaze()

        while True:
            gui.clearConsole()
            print("Maze overview:")
            gui.printMazeWithFrame(self.displayed_maze)

            if (not self.playing_forwards):
                input = gui.consoleGetOptionInt()
                match input:
                    case 1:  # show loaded maze
                        self.displayUnsolvedMaze()
                    case 2:  # show solved maze
                        self.displaySolvedMaze()
                    case 3:  # show step by step solution
                        self.displayUnsolvedMaze()
                        self.currentPathTile = 0
                        self.playing_forwards = True
                        self.drawing_path = False

            else:
                if (not self.drawing_path and self.currentStep >= len(self.steps)):
                    self.drawing_path = True
                if (self.drawing_path and self.currentPathTile >= len(self.path)):
                    self.playing_forwards = False
                    self.drawing_path = False
                    continue
                self.calculateNextDisplayedState()


p = MazeSolver_Program()
p.run()
