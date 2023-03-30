import os
from time import sleep
import gui
import program_classes as pc
import numpy as np
import maze_file_input_output as mfio
import constants as c
import time


class MazeSolverProgram:

    __maze_file_path: str

    def __init__(self, h,  path_to_maze_file: str = None, display_step_size=1):
        self.__h = h  # pick the given heuristic
        if (path_to_maze_file == None):
            __location__ = os.path.realpath(os.path.join(
                os.getcwd(), os.path.dirname(__file__)))
            self.__maze_file_path = os.path.join(__location__, "maze0.txt")
        else:
            self.__maze_file_path = path_to_maze_file
        self.__clear_steps_and_path()
        self.__display_step_size = display_step_size

    def __clear_steps_and_path(self):
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

    def __locate_start_and_end_tiles(self):
        self.start_tile_np_arr = np.argwhere(self.__maze == c.MAZE_START)
        self.end_tile_np_arr = np.argwhere(self.__maze == c.MAZE_END)
        self.__end_tile = pc.Tile(
            self.end_tile_np_arr[0][0], self.end_tile_np_arr[0][1])
        self.__start_tile: pc.Tile = pc.Tile(
            self.start_tile_np_arr[0][0], self.start_tile_np_arr[0][1])

    __end_tile: pc.Tile
    __start_tile: pc.Tile

    # ----- Stepping of the algorithm
    # array containing steps
    __steps: list[pc.Step] = []
    # keep track which step's outcome is displayed
    __current_step: int
    __display_step_size: int = 1
    # array containing path
    __path: list[pc.Tile] = []
    # current path tile (displayed by gui)
    __current_path_tile: int

    __solution_time: float  # solution time in seconds
    __solution_steps: int
    __path_length: int

    def __solve_maze_with_measurements(self):
        self.__clear_steps_and_path()
        start_time = time.time()
        self.__solve_maze()
        end_time = time.time()
        self.__solution_time = end_time - start_time
        self.__solution_steps = len(self.__steps)
        self.__path_length = len(self.__path)

    # the algorithm

    def __solve_maze(self):
        # initializing algorithm lists
        # 'frontier' is not a "queue.priorityQueue" because priorityQueue is not iterable: so we would not be able to check if the item is already in the queue easily
        frontier = [self.__start_tile]
        explored = []
        new_frontiers: list[pc.Tile] = []

        # create a two-dimensional table for tiles, where each tile will store coordinates to their predecessor
        paths_map: list[list[pc.Tile]] = []
        # populate the paths array with elements
        for row in self.__maze:
            temp_row = []
            for tile in row:
                temp_row.append(pc.Tile(-1, -1))
            paths_map.append(temp_row)

        # main algorithm loop (runs as long as there are tiles to check)
        def applied_heuristic(x): return self.__h(x, self.__end_tile)
        while len(frontier) > 0:
            # find the tile to check with the smallest heuristic value
            checked_tile = min(frontier, key=applied_heuristic)
            # check if we reached the end of the maze
            if checked_tile == self.__end_tile:
                new_frontiers.clear()
                self.__add_new_step(checked_tile, list(new_frontiers))
                # ----- Generate final path
                # generate the final path array
                final_path = [self.__end_tile]
                current_tile = paths_map[self.__end_tile.y][self.__end_tile.x]
                while current_tile != self.__start_tile:
                    final_path.append(pc.Tile(current_tile.y, current_tile.x))
                    current_tile = paths_map[current_tile.y][current_tile.x]
                # reverse it to get list from beginning to the end
                final_path.reverse()
                for tile in final_path:
                    # add tile to the drawing system
                    self.__add_new_path_to_tile(tile)
                break

            # move current tile from frontier to explored
            explored.append(checked_tile)
            frontier.remove(checked_tile)

            # collect neighbors
            neighbors: list[pc.Tile] = []
            # up tile
            if (checked_tile.x > 0 and self.__maze[checked_tile.y][checked_tile.x-1] != c.MAZE_WALL):
                neighbors.append(pc.Tile(x=checked_tile.x-1, y=checked_tile.y))
            # down tile
            if (checked_tile.x < self.__maze.shape[1]-1 and self.__maze[checked_tile.y][checked_tile.x+1] != c.MAZE_WALL):
                neighbors.append(pc.Tile(x=checked_tile.x+1, y=checked_tile.y))
            # left tile
            if (checked_tile.y > 0 and self.__maze[checked_tile.y-1][checked_tile.x] != c.MAZE_WALL):
                neighbors.append(pc.Tile(x=checked_tile.x, y=checked_tile.y-1))
            # right tile
            if (checked_tile.y < self.__maze.shape[0]-1 and self.__maze[checked_tile.y+1][checked_tile.x] != c.MAZE_WALL):
                neighbors.append(pc.Tile(x=checked_tile.x, y=checked_tile.y+1))

            new_frontiers.clear()

            # check neighboring tiles
            for tile in neighbors:
                # add tile to frontier if it was not in there already and if it has not been explored
                if (tile not in frontier):
                    if (tile not in explored):
                        frontier.append(tile)
                        new_frontiers.append(tile)
                        paths_map[tile.y][tile.x].x = checked_tile.x
                        paths_map[tile.y][tile.x].y = checked_tile.y
                # also move up node present in frontier if its heuristic is better than the currently checked one
                elif (applied_heuristic(tile) < applied_heuristic(checked_tile)):
                    frontier.remove(tile)
                    frontier.append(tile)
                    new_frontiers.append(tile)
                    paths_map[tile.y][tile.x].x = checked_tile.x
                    paths_map[tile.y][tile.x].y = checked_tile.y

            self.__add_new_step(checked_tile, list(new_frontiers))

    # gui functions and data
    def __prerender_solved_maze(self):
        self.__solved_maze = np.array(self.__maze)
        for step in self.__steps:
            self.__solved_maze = gui.apply_search_step_to_maze(
                self.__solved_maze, step)

        for path_marking in self.__path:
            self.__solved_maze = gui.apply_path_marking_to_maze(
                self.__solved_maze, path_marking)

    # the maze state which is displayed by the program
    __displayed_maze: np.array
    __playing_forwards: bool = False
    __drawing_path: bool = False

    # function to add new steps
    def __add_new_step(self, current_tile: pc.Tile, new_states: list[pc.Tile]):
        self.__steps.append(pc.Step(current_tile, new_states))

    # function to add new path to tile
    def __add_new_path_to_tile(self, tileToAdd: pc.Tile):
        self.__path.append(tileToAdd)

    # helper functions to set the state of display
    def __display_unsolved_maze(self):
        self.__current_step = 0
        self.__displayed_maze = np.array(self.__maze)

    def __display_solved_maze(self):
        self.__current_step = len(self.__steps)
        self.__displayed_maze = np.array(self.__solved_maze)

    def __calculate_next_displayed_state(self):
        for x in range(self.__display_step_size):
            if (not self.__drawing_path and self.__current_step >= len(self.__steps)):
                self.__drawing_path = True
                break
            if (self.__drawing_path and self.__current_path_tile >= len(self.__path)):
                self.__playing_forwards = False
                self.__drawing_path = False
                break

            if not self.__drawing_path:
                step = self.__steps[self.__current_step]
                self.__displayed_maze = gui.apply_search_step_to_maze(
                    self.__displayed_maze, step)
                self.__current_step += 1

            else:  # draw path in one step
                for y in range(self.__path_length):
                    path_tile = self.__path[self.__current_path_tile]
                    self.__displayed_maze = gui.apply_path_marking_to_maze(
                        self.__displayed_maze, path_tile)
                    self.__current_path_tile += 1
        sleep(0.1)

    # main function

    def run(self):
        gui.init_console()
        # load unsolved maze from file
        self.load_maze_file()

        # solve the maze (generating steps)
        self.__solve_maze_with_measurements()

        # start with showing unsolved maze
        self.__prerender_solved_maze()
        self.__display_unsolved_maze()

        while True:
            gui.clear_console()
            print("Maze overview:")
            gui.print_maze(self.__displayed_maze)
            gui.print_solution_measurements(
                self.__solution_time, self.__solution_steps, self.__path_length)
            if (not self.__playing_forwards):
                input = gui.console_get_option_int()
                match input:
                    case 1:  # show loaded maze
                        self.__display_unsolved_maze()
                    case 2:  # show solved maze
                        self.__display_solved_maze()
                    case 3:  # show step by step solution
                        self.__display_unsolved_maze()
                        self.__current_path_tile = 0
                        self.__playing_forwards = True
                        self.__drawing_path = False

            else:
                self.__calculate_next_displayed_state()

    def load_maze_file(self):
        self.__maze = mfio.load_maze(self.__maze_file_path)
        self.__locate_start_and_end_tiles()

    # solve the maze and return solution statistics
    def solve(self):
        # load unsolved maze from file
        self.load_maze_file()
        # solve the maze (generating steps)
        self.__solve_maze_with_measurements()
        return [self.__solution_time, self.__solution_steps, self.__path_length]


# p = MazeSolverProgram()
# p.run()
