# run this file to open the interactive version of the maze solver program
# do not forget to generate a maze file and put it in the mazes directory
import maze_solver_program
import maze_file_input_output
import heuristics
import maze_generator

# START config
# if True, will create/overwrite a maze file with given maze_file_name
do_generate_new_maze = True
maze_file_name = "maze1.txt"
# dimensions of the maze (if generating new maze)
maze_width = 25
maze_height = 25
# choose heuristic that will be used by the algorithm
used_heuristic = heuristics.h2
# how many steps per display frame should be shown by the "step by step solution" option
display_step_size = 1
# END config

maze_file_path = maze_file_input_output.get_maze_save_path(maze_file_name)

if do_generate_new_maze:
    maze_generator.generate_maze(maze_width, maze_height, maze_file_path)

p = maze_solver_program.MazeSolverProgram(
    used_heuristic, maze_file_path, display_step_size)
p.run()
