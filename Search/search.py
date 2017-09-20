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

def depthFirstSearch(problem):
    from util import Stack
    # initialize variables
    fringe = Stack()
    discovered = dict()
    node = (problem.getStartState(), None, 0, None)
    fringe.push(node)

    # while fringe still has nodes
    while not fringe.isEmpty():
        node = fringe.pop()

        # map discovered by predecesor
        discovered.update({node[0]: node})

        # return if goal
        if problem.isGoalState(node[0]):
            break

        # else add to discovered and put onto stack
        successors = problem.getSuccessors(node[0])
        for s in successors:
            if not discovered.has_key(s[0]):
                fringe.push(s + (node[0],))

    # get path
    path = []

    while node[3] is not None:
        path.insert(0, node[1])
        node = discovered[node[3]]

    return path

def breadthFirstSearch(problem):
    from util import Queue
    # initialize variables
    fringe = Queue()
    node = problem.getStartState()
    discovered = dict({node: None})
    fringe.push(node)

    # while fringe still has nodes
    while not fringe.isEmpty():
        node = fringe.pop()

        # return if goal
        if problem.isGoalState(node):
            break

        # else add to discovered and put onto stack
        successors = problem.getSuccessors(node)
        for s in successors:
            if not discovered.has_key(s[0]):
                discovered.update({s[0]: s + (node,)})  # create new tuple with reference to prev node
                fringe.push(s[0])

    # get path
    path = []
    while discovered[node] is not None:
        details = discovered.get(node)
        path.insert(0, details[1])  # insert path to front since it's backwards
        node = details[3]

    return path

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue

    # initialize variables
    fringe = PriorityQueue()
    start = problem.getStartState()

    fringe.push(start, 0)
    traveled = dict()
    traveled.update({(start, None): (None, None)})

    # while fringe still has nodes
    while not fringe.isEmpty():
        node = fringe.pop()

        # return if goal
        if problem.isGoalState(node):
            break

        # else add to discovered and put onto stack
        successors = problem.getSuccessors(node)
        for s in successors:
            directedNode = (s[0:1] + node)
           # print directedNode
            fringe.push([s], s[1])
            traveled.append({(directedNode): node})

    # need to change discovered to hold the whole tuple as the key

    # get path
    path = []
    print node
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
