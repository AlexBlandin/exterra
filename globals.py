def init():
    global context
    context = {} #things that aren't mutable and so need to be wrapped in a mutable for global access

    global images
    images = {} #named images -- returns image data for blitting

    global blitque
    blitque = [] #ordered tuples (images, rects) to blit, for now just go to background -- can be done by layer IF NEEDED

    global entities
    entities = [] #should we ever use them
