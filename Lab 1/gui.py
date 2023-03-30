import os
import numpy
from colorama import init as colorama_init
from colorama import Back
from colorama import Fore
from colorama import Style
import program_classes as pc
import constants as c


def init_console():
    colorama_init()


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_solution_measurements(solutionTime: float,  stepsCount: int, pathLength: int):
    print(
        f"Maze solved in: {(1000*solutionTime):.6f} miliseconds. It took {stepsCount} steps to find the {pathLength} tiles long path")


def console_get_option_int() -> str:
    input_name = "option"
    test = None
    while test == None:
        print("0. quit program")
        print("1. show unsolved maze")
        print("2. show solved maze")
        print("3. show step by step solution")
        input_text = "".join(["Give integer for: ", input_name, " = "])
        given = input(input_text)
        try:
            test = int(given)
            if (test < 1):
                quit()
            if test > 3:
                raise ValueError()
        except ValueError:
            print("INCORRECT INPUT:", given)
            print("TRY AGAIN (give an integer from 0 to 3 - inclusive)")
            test = None
    return test


def apply_search_step_to_maze(maze: numpy.array, step: pc.Step):
    # TEMP do not overwrite the start or end of tile path
    if (not (maze[step.evaluated_tile.y][step.evaluated_tile.x] == c.MAZE_START or maze[step.evaluated_tile.y][step.evaluated_tile.x] == c.MAZE_END)):
        maze[step.evaluated_tile.y][step.evaluated_tile.x] = c.ALG_EXPLORED
    for new_frontier in step.new_frontier_tiles:
        # TEMP do not overwrite the start or end tile path
        if (not (maze[new_frontier.y][new_frontier.x] == c.MAZE_START or maze[new_frontier.y][new_frontier.x] == c.MAZE_END)):
            maze[new_frontier.y][new_frontier.x] = c.ALG_FRONTIER
    return maze


def apply_path_marking_to_maze(maze: numpy.array, pathTile: pc.Tile):
    # TEMP do not overwrite the start or end tile path
    if (not (maze[pathTile.y][pathTile.x] == c.MAZE_START or maze[pathTile.y][pathTile.x] == c.MAZE_END)):
        maze[pathTile.y][pathTile.x] = c.ALG_PATH
    return maze


def print_maze(maze: numpy.array):
    # get max length of item in array
    horizontal_maze_border_line = horizontal_maze_border(maze)

    lines = []
    lines.append(horizontal_maze_border_line)
    for row in maze:
        lines.append(
            wrap_in_maze_border(
                ''.join(color_tile_back(str(x)) for x in row)))
    lines.append(remove_style(horizontal_maze_border_line))
    print('\n'.join(lines))


def horizontal_maze_border(maze: numpy.array):
    return wrap_in_maze_border(color_white_back(''.join('--' for x in maze[0])))


def wrap_in_maze_border(s: str):
    return color_white_back('|') + s + color_white_back('|')


def color_tile_back(s: str):
    if (s == c.MAZE_EMPTY_SPACE):
        return color_white_back(s+' ')
    if (s == c.MAZE_START):
        return color_green_back(s+' ')
    if (s == c.MAZE_END):
        return color_red_back(s+' ')
    if (s == c.ALG_EXPLORED):
        return color_blue_back(s+' ')
    if (s == c.ALG_PATH):
        return color_yellow_back(s+' ')
    if (s == c.ALG_FRONTIER):
        return color_cyan_back(s+' ')
    return color_black_back(s+' ')


def color_black_back(s: str):
    return add_color(f'{Back.BLACK}', s)


def color_white_back(s: str):
    return add_color(f'{Back.WHITE}', s)


def color_blue_back(s: str):
    return add_color(f'{Back.BLUE}', s)


def color_cyan_back(s: str):
    return add_color(f'{Back.CYAN}', s)


def color_green_back(s: str):
    return add_color(f'{Back.GREEN}', s)


def color_yellow_back(s: str):
    return add_color(f'{Back.YELLOW}', s)


def color_red_back(s: str):
    return add_color(f'{Back.RED}', s)


def add_color(color, s: str):
    result = str(color) + s
    return result


def remove_style(s: str):
    result = s + str(f'{Style.RESET_ALL}')
    return result
