#Date: 3/9/23
#Purpose: Creating the graph and image for Lab 4 with BFS

#Importing methods from other files
from cs1lib import *
from load_graph import load_graph
from bfs import breadth_first_search

#loading the dictionary from the load_graph function
DICT = load_graph("dartmouth_graph.txt")

#window height and width variables
WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811
#vertex radius constant for drawing methods in vertex class
VERTEX_RADIUS = 10
#mouse location global variables
mouse_x = None
mouse_y = None
mouse_press = False
#Search variables for BFS function
vertex_start = None
vertex_finish = None

def main():
    #Clearing backround
    set_clear_color(1, 1, 1)
    clear()
    #Draws map image first as base layer
    img = load_image("img.png")
    draw_image(img, 0, 0)
    #Calls draw_edges function passing dictionary of objects as parameter
    edges(DICT)
    #Edges must be drawn first in order for the vertices to be displayed over them
    # Calls draw_vertex function passing dicitonary of objects as parameter
    vertex(DICT)

    v1, v2 = user_input(DICT)
    highlight(v1, v2, DICT)

def vertex(dict):
    for val in dict:
        dict[val].draw_vertex(0, 0, 1)

def edges(dict):
    for item in dict:
        dict[item].draw_all_edge(0, 0, 1)
    #For each value in the object dictionary
    for key in dict:
        #for each object in val's adj_list
        for location in dict[key].adj_list:
            #call draw_edge on val, passing the objects from the adj_list into the Vertex class method
            dict[key].draw_edge(location, 0, 0, 1)

#Condition for user input function to detect if the mouse is pressed - only if it is will the user_input function take it into account
def user_mouse_press(px, py):
    global mouse_press
    mouse_press = True
def user_mouse_release(rx, ry):
    global mouse_press
    mouse_press = False
#Updates global mouse location variables
def user_mouse_location(x, y):
    global mouse_x, mouse_y
    mouse_x = x
    mouse_y = y

def user_input(dict):
    global pass_1, vertex_start, vertex_finish
    #setting values for the start and finish of BFS function
    for val in dict:
        if mouse_press == True and mouse_x in range((dict[val].x - VERTEX_RADIUS), (dict[val].x + VERTEX_RADIUS)) and mouse_y in range((dict[val].y - VERTEX_RADIUS), (dict[val].y + VERTEX_RADIUS)):
            if vertex_start == None:
                vertex_start = val
            val == None
    for val in dict:
        if mouse_press == False and mouse_x in range((dict[val].x - VERTEX_RADIUS),(dict[val].x + VERTEX_RADIUS)) and mouse_y in range((dict[val].y - VERTEX_RADIUS), (dict[val].y + VERTEX_RADIUS)):
            if vertex_start != None:
                vertex_finish = val
    return vertex_start, vertex_finish

def highlight(v1, v2, dict):
    #if both start and finish vertices have values
    if v1 != None and v2 != None:
        #Call highlight_vertex method from vertex Class
        dict[v1].highlight_vertex()
        dict[v2].highlight_vertex()
    if v1 != None and v2 != None and v1 != v2:
        #Getting list of path from BFS function
        bfs_list = breadth_first_search(dict[v1], dict[v2])
        #highlighting the vertices and the edges of each value in the path list
        for val in range(len(bfs_list)):
            #Calling highlight_vertex method from Vertex class
            bfs_list[val].highlight_vertex()
            #Calling highlight_edge method from Vertex class (until the final value is approached where there is no more path to highlight)
            if not val + 1 >= len(bfs_list):
                bfs_list[val].draw_edge(bfs_list[val + 1], 1, 0, 0)
        dict[v1].draw_name()
        dict[v2].draw_name()

start_graphics(main, mouse_move=user_mouse_location, mouse_press=user_mouse_press, mouse_release=user_mouse_release, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
