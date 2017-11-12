import pygame, matplotlib
matplotlib.use("Agg")
import pylab
from matplotlib.backends.backend_agg import FigureCanvasAgg

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

def graph_image(graph):
    canvas = FigureCanvasAgg(graph)
    canvas.draw()
    rgb_string = canvas.get_renderer().tostring_rgb()
    return pygame.image.fromstring(rgb_string, canvas.get_width_height(), "RGB")

def linear_plot(graph_size = [5, 5], dpi = 100, points = []):
    graph = matplotlib.figure.Figure(figsize = graph_size, dpi = dpi) # https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html
    axes = graph.gca() # https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.gca
    axes.plot(points)
    return graph
