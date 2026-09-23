
import math

from collections import deque

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
        # ex. neighbors["B"] = 15.23
        if neighborPassList:
            for neighbor in neighborPassList:
                self.addNeighborToNeighbors(neighbor)

    def addNeighborToNeighbors(self, neighbor):
        distance1 = (math.sqrt((self.x-neighbor.x)**2 + (self.y-neighbor.y)**2))
        self.neighbors[neighbor] = distance1
        neighbor.neighbors[self] = distance1
        #update list of neighbors w/ u and v
        #since in problem 1 the graph is undirected all children = neighbors

    def __repr__(self):
        return self.name # printing 




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
    C = Node(7,9,[B], "C" )
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



if __name__ == "__main__":
    main()





'''
def breadth_first_search(problem):
    node = problem.initial
    print("Starting from node", node)
    if (problem.is_goal(node)):
        print("Goal found ")
        return node
    frontier = deque([node]) # FIFO queue: .append() and .popleft()
    reached = [problem.initial]
    while len(frontier) > 0: # while not IS-EMPTY(frontier) do
        print("Frontier array", frontier)
        print("reached array", reached)
        node = frontier.popleft()
        for child in node.neighbors:

            if (problem.is_goal(child)):
                print("Found target node", child)
                return child
            if (not (child in reached)):
                print(child, "child")
                reached.append(child)
                frontier.append(child)
    return 0 # failure
''''''
function BREADTH-FIRST-SEARCH(problem) returns a solution node or failure
    node←NODE(problem.INITIAL)
    if problem.IS-GOAL(node.STATE) then return node
    frontier←a FIFO queue, with node as an element
    reached← {problem.INITIAL}
    while not IS-EMPTY(frontier) do
        node←POP(frontier)
        for each child in EXPAND(problem, node) do
            s←child.STATE
            if problem.IS-GOAL(s) then return child
            if s is not in reached then
                add s to reached
                add child to frontier
    return failure

function UNIFORM-COST-SEARCH(problem) returns a solution node, or failure
    return BEST-FIRST-SEARCH(problem, PATH-COST)
'''


