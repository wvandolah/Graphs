"""Graph representation using adjacency matrix."""

class Vertex:
    """Vertices just need a label, the matrix will track edges."""
    # Using simple classes for illustrative purposes
    # pylint: disable=too-few-public-methods
    def __init__(self, label):
        self.label = label


class Graph:
    """The graph is a matrix of 0s/1s indicating existence of edges."""
    # pylint: disable=too-few-public-methods
    def __init__(self, num_vertices):
        # * copying is shallow, so need explicit iteration for unique rows
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def connect_vertex(self, row, col):
        """Add an edge between vertices indicated by row/col of matrix."""
        self.matrix[row][col] = 1

"""
Below if from class
"""
"""Live coding of different ways to represent graphs."""


class Vertex:
    """MVV - Minimum Viable Vertex."""
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return str(self.label)


class MatrixGraph:
    """Adjacency matrix representation of a graph."""
    def __init__(self, num_vertices):
        self.matrix = [[0 for _ in range(num_vertices)]
                       for _ in range(num_vertices)]
        self.vertices = [Vertex(str(i)) for i in range(num_vertices)]

    def add_edge(self, start_index, end_index, bidirectional=True):
        """Add an edge from start vertex to end vertex."""
        self.matrix[start_index][end_index] = 1
        if bidirectional:
            self.matrix[end_index][start_index] = 1