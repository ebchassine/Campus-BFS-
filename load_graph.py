#Author: Ethan Wong-Chassine
#Date: 3/3/23
#Purpose: load_graph file for Lab 4

#Importing Vertex Class
from vertex import Vertex

def load_graph(file):
    #Open file
    file_read = open(file, 'r')
    vertex_dict = {}

    for line in file_read:
        #splitting the values by ;
        line = line.split(';')
        #Setting the object instance variables
        vertex_name = line[0]
        vertex_x, vertex_y = line[2].split(',')[0].strip(), line[2].split(',')[1].strip()
        #Creating an object using the variables created
        object = Vertex(vertex_name, vertex_x, vertex_y, [])
        #Appending the objects to the vertex dicitonary
        vertex_dict[vertex_name] = object
    #Closing file before second loop
    file_read.close()
    #Opening file before second loop
    file_read = open(file, 'r')
    for line1 in file_read:
        line1 = line1.split(';')
        vertex_name = line1[0]
        vertex_object=vertex_dict[vertex_name.strip()]
        adj_temp_list = list(line1[1].split(','.strip()))
        # print(vertex_name, adj_list) # DEBUG LINE
        if vertex_name in vertex_dict:
            #Finding Object in the dicitonary that matches the desired name
            # vertex_object = (vertex_dict[vertex_name])
            #setting the object adj_list to the adj_list craeted earlier in this loop
            for val in adj_temp_list:
                adj_obj=vertex_dict[val.strip()]
                vertex_object.adj_list.append(adj_obj)
            # vertex_dict[vertex_name.strip()].adj_list = adj_temp_list
    file_read.close()
    return vertex_dict