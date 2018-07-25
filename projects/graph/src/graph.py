#!/usr/bin/python
 
"""
Simple graph implementation compatible with BokehGraph class.
"""
from random import choice, random

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
        start.edges.add(end)
        if bi:
            end.edges.add(start)

    def bfs(self, start):
        random_color = '#' + \
            ''.join([choice('0123456789ABCDEF') for j in range(6)])
        queue = []
        found = []
        queue.append(start)
        found.append(start)

        start.color = random_color
        
        while (len(queue) > 0):
            v = queue[0]
            # print(v.edges)
            for edge in v.edges:
                # print(edge)
                if edge not in found:
                    found.append(edge)
                    queue.append(edge)
                    edge.color = random_color

            queue.pop(0)  
        # print(found)
        return found
    
    def con_components(self):
        """use bfs to find components connected"""

        searched = []
        
        for index, vertex in self.vertices.items():
            # print('whats being passed to bfs',vertex.color)
            if vertex not in searched:
                searched.append(self.bfs(vertex))
        # print(searched)
        








