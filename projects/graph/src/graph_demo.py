#!/usr/local/opt/pyenv/versions/3.7.0/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from random import choice
from draw import BokehGraph
from graph import Graph, Vertex


def main(number_verts=15, number_edges=10, bfs_search=0):

    graph = Graph()
    v = set()

    for n in range(number_verts):
        n = Vertex(n)
        graph.add_vertex(n)
        v.add(n)

    for _ in range(number_edges):
        first = choice(tuple(v))
        second = choice(tuple(v))
        graph.add_edge(first, second)
        v.remove(first)

    if bfs_search:
        graph.bfs(graph.vertices[bfs_search])
    else:
        graph.con_components()
    bg = BokehGraph(graph)
    bg.show()


if __name__ == '__main__':
    if len(argv) > 1:
        NUMBER_VERTS = int(argv[1])
        NUMBER_EDGES = int(argv[2])
        BFS = int(argv[3])
        main(NUMBER_VERTS, NUMBER_EDGES, BFS)
    else:
        main()
