# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

from util import *

def search(problem, fringe, heuristic):
    node = (problem.getStartState(), None, 0, None)
    traversed = dict()

    # add heuristic to cost if PQ if provided for PQ
    if heuristic:
        hCost = node[2] + heuristic(node[0], problem)
        fringe.push(node, hCost)
    else:
        fringe.push(node)

    while not fringe.isEmpty():
        node = fringe.pop()
        current, action, cost, previous = node

        # no duplicate path expansions
        if traversed.has_key(current):
            continue
        # get path
        elif problem.isGoalState(current):
            break

        # add to traversed
        traversed.update({current: node})

        for s in problem.getSuccessors(current):
            # if new add to fringe
            successor = s + (current,)

            if not traversed.has_key(s[0]):
                if heuristic:

                    sCurrent, sAction, sCost, sPrevious = successor
                    sCost += cost
                    fringe.push((sCurrent, sAction, sCost, sPrevious), sCost + heuristic(sCurrent, problem))
                else:
                    fringe.push(successor)

    path = []
    while node[3] is not None:
        path.insert(0, node[1])
        node = traversed[node[3]]

    return path

def depthFirstSearch(problem):
    return search(problem, Stack(), None)

def breadthFirstSearch(problem):
    return search(problem, Queue(), None)

def uniformCostSearch(problem):
    return search(problem, PriorityQueue(), nullHeuristic)

def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    return search(problem, PriorityQueue(), heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
