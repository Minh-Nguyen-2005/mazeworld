# Author: Minh Nguyen, Date: 10/15/2025

# You write this:
import Maze 
from SensorlessProblem import SensorlessProblem
from astar_search import astar_search

# Test 1: Sensorless Problem on small maze with obstacles 
maze1 = Maze.Maze("maze1sensorless.maz")
sp1 = SensorlessProblem(maze1)
result = astar_search(sp1, sp1.sensorless_heuristic)
print(result)
sp1.animate_path(result.path)

# Test 2: Sensorless Problem on small maze with more open space
maze2 = Maze.Maze("maze2sensorless.maz")
sp2 = SensorlessProblem(maze2)
result = astar_search(sp2, sp2.sensorless_heuristic)
print(result)
sp2.animate_path(result.path)

# Test 3: Sensorless Problem on larger maze
maze3 = Maze.Maze("maze3sensorless.maz")
sp3 = SensorlessProblem(maze3)
result = astar_search(sp3, sp3.sensorless_heuristic)
print(result)
sp3.animate_path(result.path)