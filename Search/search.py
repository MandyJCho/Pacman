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

def search(problem, fringe):
    traversed = dict()
    node = (problem.getStartState(), None, 0, None)
    fringe.push(node)

    # while fringe still has nodes
    while not fringe.isEmpty():
        node = fringe.pop()

        # already visited
        if traversed.get(node[0]) is not None:
            continue
        # or goal
        elif problem.isGoalState(node[0]):
            break

        # otherwise add the node to traversed
        traversed.update({node[0]: node})

        # else add to discovered and put onto stack
        for s in problem.getSuccessors(node[0]):
            if not traversed.has_key(s[0]):
                fringe.push(s + (node[0],))

    # get path
    path = []

    # backtrack until root
    while node[3] is not None:
        path.insert(0, node[1])
        node = traversed[node[3]]

    return path

def depthFirstSearch(problem):
    from util import Stack
    return search(problem, Stack())

def breadthFirstSearch(problem):
    from util import Queue
    return search(problem, Queue())

def uniformCostSearch(problem):
    from util import PriorityQueue

    # initialize variables
    fringe = PriorityQueue()
    node = (problem.getStartState(), None, 0, None)
    fringe.push(node, node[2])
    traversed = dict()

    # while fringe still has nodes
    while not fringe.isEmpty():
        node = fringe.pop()
        print node

        # already visited
        if traversed.get(node[0]) is not None:
            continue
        # return if goal
        elif problem.isGoalState(node):
            break

        traversed.update({node[0]: node})

        # else add to discovered and put onto stack
        for successor, action, stepCost in problem.getSuccessors(node[0]):
            # if not traversed
            if not traversed.has_key(successor):
                print "add ", (successor, action, stepCost + node[2], node[0])
                fringe.push((successor, action, stepCost + node[2], node[0]), stepCost + node[2])


    # get path
    path = []

    # backtrack until root
    while node[3] is not None:
        path.insert(0, node[1])
        node = traversed[node[3]]

    return path

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
