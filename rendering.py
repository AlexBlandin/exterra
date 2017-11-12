import pygame

#
##  Returns an image of the input string
#
def make_text(string, size = 28, colourTuple = (10, 10, 10), font = None, aa = 1):
    font = pygame.font.Font(font, size)
    text = font.render(string, aa, colourTuple)
    return text
