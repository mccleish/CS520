#Curtis McCleish ccm141
import math
import heapq
#from collections import deque

endNodeCoords = [18,3]
#we need to define function BFS, class problem, class node, FIFO queue for frontier, reached array, is_empty function for FIFO queue, 
# pop function for node, expand(problem, node), child, child.state, adding to reached and frontier
class Problem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        goal.state = 1
    def is_goal(self, state):
        return state == self.goal



class Node:
    def __init__(self, x, y, neighborPassList, name):
        self.x = x
        self.y = y

        self.neighbors = {}
        self.name = name
        self.state = 0
        #self.distance = {}
        #neighbors array will hold distance values 

        if neighborPassList:
            for neighbor in neighborPassList:
                self.addNeighborToNeighbors(neighbor)

        self.path_cost = (math.sqrt((self.x-endNodeCoords[0])**2 + (self.y-endNodeCoords[1])**2))
        #greedy path to I (straight line)
        #heuristic ^
    def addNeighborToNeighbors(self, neighbor):
        distance1 = (math.sqrt((self.x-neighbor.x)**2 + (self.y-neighbor.y)**2))
        self.neighbors[neighbor] = distance1
        neighbor.neighbors[self] = distance1
        #update list of neighbors w/ u and v
        #since in problem 1 the graph is undirected all children = neighbors
    

    def __repr__(self):
        return self.name # printing 

    def __lt__(self, node2):
        return self.name < node2.name




def main():
    # A(0,4) connected to B
#B(3,4) connected to A and C and D
#C(7,9) connected to B, G, F
#D(7,3) connected to B, J, H
#E(10, 0) connected to H
#F(12,12) connected to C and G
#G(14,8) connected to C and F
#H(14,0) connected to E and I
#I (18,3) connected to H, J, G (TERMINAL NODE)
#J (12,3) connected to I and D
#perform BFS for I


    A = Node(0, 4, None, "A")
    B = Node(3, 4, [A], "B")
    C = Node(7,9,[B], "C")
    D = Node(7,3,[B], "D")
    E =Node(10,0,[], "E")
    F= Node(12,12,[C],"F")
    G= Node(14,8,[C,F], "G")
    H= Node(14,0,[D, E],"H")
    I= Node(18,3,[H,G],"I")
    J= Node(12,3,[I,D],"J")
    #we initialized our nodes

    problem = Problem(A, I)
    best_first_search(problem)

def best_first_search(problem):
    node = problem.initial
   #frontier = heapq() # heapq
    frontier = []
    heapq.heappush(frontier, (node.path_cost, node))
    reached = [problem.initial]
    while (len(frontier)):
        print("frontier", frontier)
        print("reached", reached)
        node = heapq.heappop(frontier)[1]
        if problem.is_goal(node):
            return node
        for child in node.neighbors:
            if (child not in reached):
                reached.append(child)
                heapq.heappush(frontier, (child.path_cost, child))
    return 0

#function BEST-FIRST-SEARCH(problem, f) returns a solution node or failure
    #node←NODE(STATE=problem.INITIAL)
    #frontier←a priority queue ordered by f , with node as an element
    #reached←a lookup table, with one entry with key problem.INITIAL and value node
    #while not IS-EMPTY(frontier) do
        #node←POP(frontier)
        #if problem.IS-GOAL(node.STATE) then return node
        #for each child in EXPAND(problem, node) do
            #s←child.STATE
            #if s is not in reached or child.PATH-COST < reached[s].PATH-COST then
                #reached[s]←child
                #add child to frontier
    #return failure

#function EXPAND(problem, node) yields nodes
    #s←node.STATE
    #for each action in problem.ACTIONS(s) do
        #s'←problem.RESULT(s, action)
        #cost←node.PATH-COST + problem.ACTION-COST(s, action,s')

        #yield NODE(STATE=s', PARENT=node, ACTION=action, PATH-COST=cost)

''' from RUssell and Norvig text
Following the PARENT pointers back from a node allows us to recover the states and actions
along the path to that node. Doing this from a goal node gives us the solution.

We need a data structure to store the frontier. The appropriate choice is a queue of some
kind, because the operations on a frontier are:
• IS-EMPTY(frontier) returns true only if there are no nodes in the frontier.
• POP(frontier) removes the top node from the frontier and returns it.
• TOP(frontier) returns (but does not remove) the top node of the frontier.
• ADD(node, frontier) inserts node into its proper place in the queue.

• node.STATE: the state to which the node corresponds;
• node.PARENT: the node in the tree that generated this node;
• node.ACTION: the action that was applied to the parent’s state to generate this node;
• node.PATH-COST: the total cost of the path from the initial state to this node. In mathematical formulas, we use g(node) as a synonym for PATH-COST.'''

if __name__ == "__main__":
    main()





