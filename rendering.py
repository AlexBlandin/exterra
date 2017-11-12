import pygame, matplotlib
matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg as GraphCanvas
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


#
##  Plotting data
#
def linear_plot(points = [], title = "", xlabel = "", ylabel = "", axes_in_inches = [5, 5], dpi = 100, grid = True):
    graph = Graph(figsize = axes_in_inches, dpi = dpi) # https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html
    axes = graph.gca() # https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.gca
    axes.plot(points)
    axes.grid(grid)

    axes.set_title(title)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
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
