# Author: Minh Nguyen, Date: 10/15/2025

from Maze import Maze
from time import sleep

class SensorlessProblem:

    def __init__(self, maze):
        self.maze = maze 
        self.start_state = frozenset(self.get_floors(maze))  # all possible robot locations

    # returns list of all floor positions in the maze
    def get_floors(self, maze):
        floors = []
        for r in range(maze.height):
            for c in range(maze.width):
                if maze.is_floor(c, r):
                    floors.append((c, r))
        return floors
    
    # return True if the belief state has only one possible robot location
    def is_goal(self, state):
        return len(state) == 1
    
    # return a list of (successor_state, step_cost) pairs
    # brute force all robots move in the same direction and see how the belief state changes
    def get_successors(self, state): 
        successors = []
        possible_moves = [ (0,1), (1,0), (0,-1), (-1,0) ]  # up, right, down, left

        for move in possible_moves:
            new_positions = set()

            for (robot_col, robot_row) in state:
                new_col = robot_col + move[0]
                new_row = robot_row + move[1]

                if self.maze.is_floor(new_col, new_row):
                    new_positions.add((new_col, new_row))

                else:
                    new_positions.add((robot_col, robot_row))  # stay in place if hit wall

            successors.append( (frozenset(new_positions), 1) )  # each move has a cost of 1
    
        return successors
    
    # heuristic: maximum manhattan distance between any two possible robot locations
    # this is admissible because at least one robot must travel this distance to reach the goal
    # this heuristic relaxes the constraint that robots must move around walls
    def sensorless_heuristic(self, state):
        if len(state) <= 1:
            return 0
        
        max_distance = 0 
        state_list = list(state)
        for i in range(len(state_list)):
            for j in range(i + 1, len(state_list)):
                pos1 = state_list[i]
                pos2 = state_list[j]
                distance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
                if distance > max_distance:
                    max_distance = distance
        return max_distance

    def __str__(self):
        string =  "Blind robot problem: "
        return string

    # given a path of belief states, return the sequence of action names
    def get_action_sequence(self, path):
        if len(path) <= 1:
            return []

        actions = []
        action_names = {(0, 1): "north", (1, 0): "east", (0, -1): "south", (-1, 0): "west"}
        possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(len(path) - 1):
            current_state = path[i]
            next_state = path[i + 1]

            # Find which action leads from current state to next state
            for move in possible_moves:
                new_positions = set()
                for (robot_col, robot_row) in current_state:
                    new_col = robot_col + move[0]
                    new_row = robot_row + move[1]

                    if self.maze.is_floor(new_col, new_row):
                        new_positions.add((new_col, new_row))
                    else:
                        new_positions.add((robot_col, robot_row))

                if frozenset(new_positions) == next_state:
                    actions.append(action_names[move])
                    break

        return actions

    # given a sequence of states (including robot turn), modify the maze and print it out.
    #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # Get the action sequence
        actions = self.get_action_sequence(path)

        print("Starting sensorless robot animation")
        print(f"Initial belief state: {len(path[0])} possible positions\n")

        for step, state in enumerate(path):
            print(f"Step {step}: {len(state)} possible position(s)")
            if step > 0 and step - 1 < len(actions):
                print(f"Action taken: {actions[step - 1]}")

            # Flatten the belief state into the format maze expects
            self.maze.robot_locations = []
            for (x, y) in state:
                self.maze.robot_locations.append(x)
                self.maze.robot_locations.append(y)

            print(str(self.maze))

            if len(state) == 1:
                print(f"GOAL REACHED! Robot localized at position {list(state)[0]}")
                break

            sleep(1)

        # Print complete action sequence at the end
        if actions:
            print(f"\nComplete plan: {', '.join(actions)}")
            print(f"Total actions: {len(actions)}")


## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
