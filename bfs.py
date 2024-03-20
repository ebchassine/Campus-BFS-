#Name: Ethan Wong-Chassine
#Date: 3/8/23
#Purpose: Breadth First Search algorithm for Lab 4

from collections import deque
from load_graph import load_graph
DICT = load_graph("dartmouth_graph.txt")

def breadth_first_search(start, finish):
    #Creating frontier python queue
    frontier = deque()

    frontier.append(start) #Appending start vertex to queue
    #Creating backpointer dictionary
    backpointer = {}
    backpointer[start] = None #Adding start object to dictionary with no value

    while len(frontier) > 0:
        #Taking the current object from the front of the queue (using popleft method)
        current = frontier.popleft()
        for val in current.adj_list:#Since current is an object, it has instance variables
            #If the object is not in backpointer, add it to the queue and current to it
            if val not in backpointer:
                backpointer[val] = current
                frontier.append(val)
        #if the finish is found, break the loop
        if finish in backpointer:
            break
    #defining path python list
    path = []
    vertex = finish
    #while there are items to go backwards from in backpointer
    while vertex != None:
        path.append(vertex)
        vertex = backpointer[vertex]
    #Returinign the path list to map_plot
    return path