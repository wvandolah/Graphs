#!/usr/bin/python
 
"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """We could check if a key is already in the dictionary, and send an error
        if one is found. This would prevent being able to overwrite keys.
        https://docs.python.org/3.7/tutorial/datastructures.html#dictionaries
        """
        self.vertices[vertex] = set()


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
print(graph.vertices)

