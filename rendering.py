import pygame, matplotlib
from pygame.locals import *
from pygame.compat import geterror
matplotlib.use("agg") # https://matplotlib.org/api/matplotlib_configuration_api.html?highlight=use#matplotlib.use
from matplotlib.backends.backend_agg import FigureCanvasAgg as GraphCanvas #can't import before setting backend, because matplot
from matplotlib.figure import Figure as Graph

#
##  Returns an image of the input string
#
def text_image(string, size = 28, colourTuple = (10, 10, 10), font = None, aa = 1):
    font = pygame.font.Font(font, size)
    text = font.render(string, aa, colourTuple)
    return text

def text(string, x = 0, y = 0, size = 28, colourTuple = (10, 10, 10), font = None, aa = 1):
    image = text_image(string, size, colourTuple, font, aa)
    return image, image.get_rect().move(x, y)

def box(x = 0, y = 0, width = 0, height = 0, colour = (255, 255, 255)):
    box = pygame.Surface((width, height))
    box.fill(colour)
    return box, box.get_rect().move(x, y)

#
##  Plotting data
#
def linear_plot(points = [], title = "", xlabel = "", ylabel = "", size_in_inches = [5, 5], dpi = 100, grid = True):
    graph = Graph(figsize = size_in_inches, dpi = dpi) # https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html
    axes = graph.gca() # https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.gca
    axes.plot(points)
    axes.grid(grid)

    axes.set_title(title)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    return graph

def pie_chart(values = [], labels = [], labeldistance = 1.1, explode = None, shadow = False, size_in_inches = [5, 5], dpi = 100):
    #explode is an [] of fractions of the radius with which to offset each wedge
    # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie
    graph = Graph(figsize = size_in_inches, dpi = dpi)
    axes = graph.gca()
    axes.pie(values, labels = labels, labeldistance = labeldistance, explode = explode, shadow = shadow)

    return graph



#
## Graphing plots
#
def graph_image(graph):
    canvas = GraphCanvas(graph) # https://matplotlib.org/gallery/api/agg_oo_sgskip.html
    canvas.draw()
    rgb_string = canvas.get_renderer().tostring_rgb()
    return pygame.image.fromstring(rgb_string, canvas.get_width_height(), "RGB")

def save_graph(graph):
    import datetime
    GraphCanvas(graph)
    graph.savefig(datetime.datetime.now().strftime("%Y-%m-%d (%H'%M'%S)"))
