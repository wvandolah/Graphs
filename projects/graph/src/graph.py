#!/usr/bin/python
 
"""
Simple graph implementation compatible with BokehGraph class.
"""
# class Vertex:
#     def __init__

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
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bi=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Error - vertices not in graph!")
        self.vertices[start].add(end)
        if bi:
            self.vertices[end].add(start)

graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3', False)




