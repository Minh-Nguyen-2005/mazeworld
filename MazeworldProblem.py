# Author: Minh Nguyen, Date: 10/15/2025

from Maze import Maze
from time import sleep

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        self.start_state = (0,) + tuple(maze.robot_locations)  # (robot turn, robot1 col, robot1 row, ...)
        self.num_robots = len(maze.robot_locations) // 2

    # return a list of (successor_state, step_cost) pairs
    # robot can move in 4 directions or stay in place
    # constraint: robots cannot collide with walls or each other
    def get_successors(self, state):
        successors = []

        # robot's turn + its locations 
        robot_turn = state[0]
        robot_col= state[1 + robot_turn * 2]
        robot_row = state[2 + robot_turn * 2]
        
        possible_moves = [ (0,1), (1,0), (0,-1), (-1,0), (0,0) ]  # up, right, down, left, stay
        for move in possible_moves:
            new_col = robot_col + move[0]
            new_row = robot_row + move[1]

            # check for collisions with other robots
            robot_collision = False
            for r in range(self.num_robots):
                if r != robot_turn:
                    other_robot_col = state[1 + r * 2]
                    other_robot_row = state[2 + r * 2]
                    if new_col == other_robot_col and new_row == other_robot_row:
                        robot_collision = True
                        break
            
            # if successor is legal, add to successors
            if self.maze.is_floor(new_col, new_row) and not robot_collision:
                new_state = list(state)
                new_state[0] = (robot_turn + 1) % self.num_robots  # next robot's turn
                new_state[1 + robot_turn * 2] = new_col
                new_state[2 + robot_turn * 2] = new_row
                if move != (0,0):  # only add if robot actually moved
                    successors.append( (tuple(new_state), 1) )  # move has a cost of 1
                else:
                    successors.append( (tuple(new_state), 0) )  # staying in place has no cost

        return successors
    
    # return True if all robots are at their goal locations
    def is_goal(self, state):
        for r in range(self.num_robots):
            if state[1 + r * 2] != self.goal_locations[r * 2] or state[2 + r * 2] != self.goal_locations[r * 2 + 1]:
                return False
        return True
    
    # Manhattan distance heuristic: sum of manhattan distances of each robot to its goal
    def manhattan_heuristic(self, state):
        total_distance = 0
        for r in range(self.num_robots):
            robot_col = state[1 + r * 2]
            robot_row = state[2 + r * 2]
            goal_col = self.goal_locations[r * 2]
            goal_row = self.goal_locations[r * 2 + 1]
            total_distance += abs(robot_col - goal_col) + abs(robot_row - goal_row)
        return total_distance


    def __str__(self):
        string =  "Mazeworld problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)
        
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robot_locations = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robot_locations = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
