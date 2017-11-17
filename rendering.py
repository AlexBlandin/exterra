import pygame, matplotlib
matplotlib.use("agg") # https://matplotlib.org/api/matplotlib_configuration_api.html?highlight=use#matplotlib.use

from matplotlib.backends.backend_agg import FigureCanvasAgg as GraphCanvas #can't import before setting backend, because matplot
from matplotlib.figure import Figure as Graph
from globals import *


#
##  Rect & Image functions
#
def within(pos, rect):
    px, py = pos
    ax, ay, aw, ah = rect

    if px >= ax and py >= ay and px <= ax + aw and py <= ay + ah:
        return True
    else:
        return False



#
##  Text rendering
#
def text_image(string, fontsize = 28, fontcolour = (10, 10, 10), font = None, aa = 1):
    font = pygame.font.Font(font, fontsize)
    text = font.render(string, aa, fontcolour)

    return text

def text(string, x = 0, centerx = None, y = 0, centery = None, fontsize = 28, fontcolour = (10, 10, 10), font = None, aa = 1):
    image = text_image(string, fontsize, fontcolour, font, aa)
    imagerect = image.get_rect().move(x, y)
    if centerx != None:
        imagerect = image.get_rect(centerx = centerx, centery = centery)

    return image, imagerect



#
##  Menu options
#
def box(x = 0, centerx = None, y = 0, centery = None, width = 0, height = 0, colour = (0, 0, 0), image = None):
    box = pygame.Surface((width, height))

    box.fill(colour)

    if image != None:
        box.blit(images[image])

    boxrect = box.get_rect().move(x, y)

    if centerx != None:
        boxrect = box.get_rect(centerx = centerx, centery = centery)

    return box, boxrect


def text_box(string, x = 0, centerx = None, y = 0, centery = None, padding = 5, fontsize = 28, fontcolour = (10, 10, 10), colour = (0, 0, 0), image = None, font = None, aa = 1):
    textimage, textrect = text(string, fontsize = fontsize, fontcolour = fontcolour, font = font, aa = aa)
    scratch, pad, width, height = textrect

    textbox, boxrect = box(x = x - padding, centerx = centerx, y = y - padding, centery = centery, width = width + (2*padding), height = height + (2*padding) - 3, colour = colour, image = image)

    textbox.blit(textimage, (padding, padding))

    return textbox, boxrect


def button(hold = False, x = 0, centerx = None, y = 0, centery = None, width = 0, height = 0, colour = (200, 200, 200), image = None, text = None, padding = 5, fontsize = 28, fontcolour = (10, 10, 10), font = None, aa = 1):
    if text != None:
        button, buttonrect = text_box(text, x = x, y = y, padding = padding, fontsize = fontsize, fontcolour = fontcolour, colour = colour, image = image, font = font, aa = aa)
        x, y, width, height = buttonrect
    else:
        button, buttonrect = box(x = x, y = y, width = height, height = height, colour = colour, image = image)

    pair = (button, buttonrect)

    if hold:
        mouse = context["leftdown"]
    else:
        mouse = context["leftpressed"]
    if mouse and within(context["mousepos"], (x, y, width, height)):
        return True, pair
    else:
        return False, pair



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
