#!/usr/bin/python
 
"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    def __init__(self, label, color='white'):
        self.label = label
        self.edges = set()
        self.color = color
    
    # def __repr__(self):
    #     return str(self.label)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges=()):
        """We could check if a key is already in the dictionary, and send an error
        if one is found. This would prevent being able to overwrite keys.
        https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries
        """
        if vertex in self.vertices:
            raise Exception("Error - vertex {} is already a thing".format(vertex))            
        if not set(edges).issubset(self.vertices):
            raise Exception('error: connot have edge to nonexistent vertices')
               
        self.vertices[vertex.label] = vertex

    def add_edge(self, start, end, bi=True):
        # if start not in self.vertices or end not in self.vertices:
        #     raise Exception("Error - vertices not in graph!")
        start.edges.add(end.label)
        if bi:
            end.edges.add(start.label)

# graph = Graph()  # Instantiate your graph
# a = Vertex(0)
# b = Vertex(1)
# c = Vertex(2)
# d = Vertex(3)

# graph.add_vertex(a)
# graph.add_vertex(b)
# graph.add_vertex(c)
# graph.add_vertex(d)

# graph.add_edge(a, b)
# graph.add_edge(a, d)






