import pygame

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
