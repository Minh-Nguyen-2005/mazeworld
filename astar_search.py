# Author: Minh Nguyen, Date: 10/15/2025

from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        return self.heuristic + self.transition_cost

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


# A* algorithm
def astar_search(search_problem, heuristic_fn):
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {}
    visited_cost[start_node.state] = 0

    while len(pqueue) > 0:
        current_node = heappop(pqueue)
        current_state = current_node.state
        current_cost = current_node.transition_cost

        solution.nodes_visited += 1

        # check for goal
        if search_problem.is_goal(current_state):
            solution.path = backchain(current_node)
            solution.cost = current_cost
            return solution
        
        for (successor, step_cost) in search_problem.get_successors(current_state):
            # compute new cost to reach successor
            new_cost = current_cost + step_cost

            if successor not in visited_cost or new_cost < visited_cost[successor]:
                visited_cost[successor] = new_cost
                heuristic = heuristic_fn(successor)
                new_node = AstarNode(successor, heuristic, current_node, new_cost)
                heappush(pqueue, new_node)

    return None 