"""
General drawing methods for graphs using Bokeh.
"""
from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph import *

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=10, height=10,
                show_axis=False, show_grid=False, circle_size=35):
        if not graph.vertices:
            raise Exception('Graph should contain vertices!')
        self.graph = graph

        #setup plot
        self.width = width
        self.height = height
        self.pos = {}
        self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)

    def _setup_graph_renderer(self, circle_size):
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), 'index')
        graph_renderer.node_renderer.data_source.add(
            self._get_random_colors(), 'color')
        graph_renderer.node_renderer.glyph = Circle(size=circle_size, fill_color='color')
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        self.making_labels()
        self.plot.renderers.append(graph_renderer)
        
    
    def _get_random_colors(self):
        colors = []
        for _ in range(len(self.graph.vertices)):
            color = "#"+''.join([choice('0123456789ABCDEF') for j in range(6)])
            colors.append(color)
        return colors

    def _get_edge_indexes(self):
        start_indices = []
        end_indices = []
        checked = set()

        for vertex, edges in self.graph.vertices.items():
            if vertex not in checked:
                for destination in edges:
                    start_indices.append(vertex)
                    end_indices.append(destination)
                checked.add(vertex)
        return dict(start=start_indices, end= end_indices)

    def show(self, output_path='./graph.html'):
        output_file(output_path)
        show(self.plot)

    def randomize(self):
        """Randomize vertex positions."""
        for vertex in self.graph.vertices:
            # TODO make bounds and random draws less hacky
            self.pos[vertex] = (1 + random() * (self.width - 2),
                                1 + random() * (self.height - 2))

    def making_labels(self):
        x = []
        y = []
        names = []
        for name, cords in self.pos.items():
            x.append(cords[0])
            y.append(cords[1])
            names.append(name)
        source = ColumnDataSource(data=dict(x=x, y=y, names=names))
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                        x_offset=10, y_offset=10, source=source, render_mode='canvas')
        self.plot.add_layout(labels)

"""
this is used to randomly create new vertex and add edges
"""
i = set()
for _ in range(25):
    rand = int(100 * random())
    i.add(rand)
for n in i:
    graph.add_vertex(n)
for _ in range(25):
    graph.add_edge(choice(tuple(i)), choice(tuple(i)))


bg = BokehGraph(graph)
bg.show()

