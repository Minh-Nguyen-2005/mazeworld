# Author: Minh Nguyen, Date: 10/15/2025

from MazeworldProblem import MazeworldProblem
from Maze import Maze
#from uninformed_search import bfs_search
from astar_search import astar_search


# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

# Your additional tests here:

# Test maze corridor with 3 robots
maze_corridor = Maze("maze_corridor.maz")
test_corridor = MazeworldProblem(maze_corridor, (1,1,1,2,1,3))
result1 = astar_search(test_corridor, test_corridor.manhattan_heuristic)
print(result1)
test_corridor.animate_path(result1.path)

# Test maze wrong order with 3 robots at bottom left corner 
maze_wrong_order = Maze("maze_wrong_order.maz")
test_wrong_order = MazeworldProblem(maze_wrong_order, (1,1,2,1,3,1))
result2 = astar_search(test_wrong_order, test_wrong_order.manhattan_heuristic)
print(result2)
test_wrong_order.animate_path(result2.path)

# Test maze corridor wrong order with 3 robots
maze_corridor_wrong_order = Maze("maze_corridor_wrong_order.maz")
test_corridor_wrong_order = MazeworldProblem(maze_corridor_wrong_order, (1,1,2,1,3,1))
result3 = astar_search(test_corridor_wrong_order, test_corridor_wrong_order.manhattan_heuristic)
print(result3)
test_corridor_wrong_order.animate_path(result3.path)


# Test large maze with 1 robot (40x40 map)
maze_large = Maze("maze_large.maz")
test_large = MazeworldProblem(maze_large, (38, 38))  # Changed from (39,39) - that's a wall!
result4 = astar_search(test_large, test_large.manhattan_heuristic)
print(result4)
test_large.animate_path(result4.path)

# Test large maze with 2 robots (40x40 map)
maze_large_2robots = Maze("maze_large2.maz")
test_large_2robots = MazeworldProblem(maze_large_2robots, (38, 38, 1, 1))  # Changed from (39,39,1,1)
result5 = astar_search(test_large_2robots, test_large_2robots.manhattan_heuristic)
print(result5)
test_large_2robots.animate_path(result5.path)