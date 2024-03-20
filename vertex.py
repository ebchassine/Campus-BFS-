#Author: Ethan Wong-Chassine
#Date: 3/3/23
#Purpose: Vertex Class for Lab 4

from cs1lib import *

class Vertex:
    def __init__(self, name, x, y, adj_list):
        #intializing variables
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adj_list = adj_list

    def __str__(self):
        # I had to reformat the list using the join method to avoid [] in the self.adj_list when printed - this does make it a str rather than a list but only when it is printed (does not change the data type of the instance variable)
        # I used stack overflow and w3 as my source for researching join method
        # I know this is not syntax from class however I remembered it from past python problems
        return self.name + '; Location: ' + str(self.x) + ', ' + str(self.y) + '; Adjacent vertices:' + str.join(',', self.adj_list)
    #Method to draw the vertex connections (under the drawing the vertices)
    def draw_edge(self, vertex2, r, g, b):
        enable_stroke()
        set_stroke_width(5)

        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, vertex2.x, vertex2.y)
    #method to draw all the vertices

    def draw_all_edge(self, r, g, b):
        set_stroke_color(r, g, b)
        for key in self.adj_list:
            draw_line(int(self.x), int(self.y), int(key.x), int(key.y))

    def draw_vertex(self, r, g, b):
        enable_stroke()
        set_stroke_width(0)
        set_fill_color(r, g, b)
        draw_circle(int(self.x), int(self.y), 10)
        disable_stroke()
    #method to change object fill color
    def highlight_vertex(self):
        disable_stroke()
        set_fill_color(1, 0 ,0)
        draw_circle(int(self.x), int(self.y), 10)
        enable_stroke()

    def draw_name(self):
        draw_text(self.name, int(self.x + 10) , self.y)
