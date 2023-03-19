from time import sleep
import gui
import program_classes as pc
import numpy as np


class MazeSolver_Program:

    # O - empty, X - wall, S - start, E - end
    maze = np.array([['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                    ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
                    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X'],
                    ['X', 'O', 'O', 'O', 'O', 'S', 'O', 'O', 'O', 'X'],
                    ['X', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X'],
                    ['X', 'O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
                    ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
                    ['X', 'O', 'O', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
                    ['X', 'X', 'X', 'X', 'E', 'O', 'O', 'O', 'O', 'X'],
                    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])

    # temp: should be obtained by running the algorithm
    # O - empty, X - wall, S - start, E - end, P - empty_on_path
    solved_maze = np.array([['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                            ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
                            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X'],
                            ['X', 'O', 'O', 'F', 'C', 'S', 'F', 'O', 'O', 'X'],
                            ['X', 'O', 'X', 'X', 'X', 'P', 'X', 'X', 'X', 'X'],
                            ['X', 'O', 'X', 'F', 'C', 'P', 'F', 'O', 'O', 'X'],
                            ['X', 'O', 'X', 'O', 'X', 'P', 'X', 'X', 'O', 'X'],
                            ['X', 'O', 'O', 'O', 'X', 'P', 'X', 'X', 'O', 'X'],
                            ['X', 'X', 'X', 'X', 'E', 'P', 'F', 'O', 'O', 'X'],
                            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']])

    # get start and end tiles
    start_tile_np_arr = np.argwhere(maze == 'S')
    end_tile_np_arr = np.argwhere(maze == 'E')
    end_tile = pc.tile(end_tile_np_arr[0][0], end_tile_np_arr[0][1])
    start_tile: pc.tile = pc.tile(
        start_tile_np_arr[0][0], start_tile_np_arr[0][1])

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

    # frontier = [startState]
    # explored = []

    # the algorithm
    def solveMaze(self):
        # temp (need to actually solve the maze)
        self.solved_maze = self.solved_maze

        # add algorithm steps (make sure to append them in real order, so they are displayed properly)
        # do not forget to add the start tile into step
        newFrontier: list[pc.tile] = []
        newFrontier.append(
            pc.tile(x=self.start_tile.x+1, y=self.start_tile.y))
        newFrontier.append(
            pc.tile(x=self.start_tile.x-1, y=self.start_tile.y))
        newFrontier.append(
            pc.tile(x=self.start_tile.x, y=self.start_tile.y+1))
        self.AddNewStep(self.start_tile, list(newFrontier))

        newFrontier.clear()
        newFrontier.append(
            pc.tile(x=self.start_tile.x-2, y=self.start_tile.y))
        self.AddNewStep(pc.tile(x=self.start_tile.x-1,
                        y=self.start_tile.y), list(newFrontier))

        newFrontier.clear()
        newFrontier.append(
            pc.tile(x=self.start_tile.x, y=self.start_tile.y+2))
        self.AddNewStep(pc.tile(x=self.start_tile.x,
                        y=self.start_tile.y+1), list(newFrontier))

        newFrontier.clear()
        newFrontier.append(
            pc.tile(x=self.start_tile.x, y=self.start_tile.y+3))
        newFrontier.append(
            pc.tile(x=self.start_tile.x+1, y=self.start_tile.y+2))
        newFrontier.append(
            pc.tile(x=self.start_tile.x-1, y=self.start_tile.y+2))
        self.AddNewStep(pc.tile(x=self.start_tile.x,
                        y=self.start_tile.y+2), list(newFrontier))

        newFrontier.clear()
        newFrontier.append(
            pc.tile(x=self.start_tile.x-2, y=self.start_tile.y+2))
        self.AddNewStep(pc.tile(x=self.start_tile.x-1,
                        y=self.start_tile.y+2), list(newFrontier))

        newFrontier.clear()
        newFrontier.append(
            pc.tile(x=self.start_tile.x, y=self.start_tile.y+4))
        self.AddNewStep(pc.tile(x=self.start_tile.x,
                        y=self.start_tile.y+3), list(newFrontier))

        newFrontier.clear()
        newFrontier.append(
            pc.tile(x=self.start_tile.x, y=self.start_tile.y+5))
        self.AddNewStep(pc.tile(x=self.start_tile.x,
                        y=self.start_tile.y+4), list(newFrontier))

        newFrontier.clear()
        newFrontier.append(
            pc.tile(x=self.start_tile.x-1, y=self.start_tile.y+5))
        newFrontier.append(
            pc.tile(x=self.start_tile.x+1, y=self.start_tile.y+5))
        self.AddNewStep(pc.tile(x=self.start_tile.x,
                        y=self.start_tile.y+5), list(newFrontier))

        # do not forget to add the end tile into step
        newFrontier.clear()
        self.AddNewStep(pc.tile(x=self.end_tile.x,
                        y=self.end_tile.y), list(newFrontier))
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
            # todo draw path in gui
            pathTile = self.path[self.currentPathTile]
            self.displayed_maze = gui.applyPathMarkingToMaze(
                self.displayed_maze, pathTile)
            self.currentPathTile += 1
            sleep(0.05)

    # main function

    def run(self):
        gui.initConsole()
        # TODO: load unsolved maze from file

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
