import pygame, os
from pygame.locals import *
from pygame.compat import geterror
if not pygame.font: raise SystemExit("Unable to render text, game unplayable!")
if not pygame.mixer: print ("!!!Warning, sound disabled!!!")

#Our stuff
import globals
globals.init()
from globals import *

from filehandling import *
from classes import *
from rendering import *



def main():
    #
    ##  Window Setup
    #
    os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (500, 100) #Set initial window position
    pygame.init()
    context["screen_width"], context["screen_height"] = 900, 900
    screen = pygame.display.set_mode((context["screen_width"], context["screen_height"]))
    pygame.display.set_caption("Caption")


    #
    ##  Image imports
    #
    images["stars.png"] = import_image("stars.png")

    #
    ##  State Setup
    #
    framerate = 60 #60FPS #PCMasterRace #FrameRatePolice
    clock = pygame.time.Clock()
    context["leftdown"], context["rightdown"], context["middown"] = False, False, False
    context["leftwaspressed"], context["rightwaspressed"], context["midwaspressed"] = False, False, False
    context["leftpressed"], context["rightpressed"], context["midpressed"] = False, False, False
    context["scrollup"], context["scrolldown"] = False, False

    #
    ##  Initialise any static images based on screen-size etc.
    #
    basecolour = pygame.Surface((context["screen_width"], context["screen_height"]))
    basecolour = basecolour.convert()
    basecolour.fill((250, 250, 250))
    images["basecolour"] = basecolour




    #
    ##  Pretty screens here
    #
    def solarsystem():
        #print("A pretty picture of the solar system")

        #calculate offset for images
        if context["scrollup"]:
            print("Scrolling up!")
        if context["scrolldown"]:
            print("Scrolling down :(")

        #make your pretty picture




        #output
        #blitque.append(())

    def research():
        print("Some nice research statistics and options")

    menu = {0: solarsystem,
            1: research
    }
    currentmenu = 0



    #
    ##  Setting up the save data -- and testing it for now
    #
    save = Save()
    ingame = False


    #
    ##  Main Loop
    #
    running = True
    while running:
        clock.tick(framerate) #if we want a static framerate

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                break
            elif event.type == MOUSEBUTTONDOWN:
                whichbutton = event.button
                if (whichbutton == 1): #leftclick
                    print("left")
                    context["leftwaspressed"] = context["leftdown"]
                    context["leftdown"] = True
                elif (whichbutton == 2): #rightclick
                    print("left")
                    context["rightwaspressed"] = context["rightdown"]
                    context["rightdown"] = True
                elif (whichbutton == 3): #middleclick
                    print("left")
                    context["midwaspressed"] = context["middown"]
                    context["middown"] = True
                elif (whichbutton == 4): #scrollup
                    print("left")
                    context["scrollup"] = True
                elif (whichbutton == 5): #scrolldown
                    print("left")
                    context["scrolldown"] = True
                else:
                    pass
            elif event.type == MOUSEBUTTONUP:
                whichbutton = event.button
                if (whichbutton == 1): #leftclick
                    context["leftwaspressed"] = context["leftdown"]
                    context["leftdown"] = False
                elif (whichbutton == 2): #rightclick
                    context["rightwaspressed"] = context["rightdown"]
                    context["rightdown"] = False
                elif (whichbutton == 3): #middleclick
                    context["midwaspressed"] = context["middown"]
                    context["middown"] = False
                elif (whichbutton == 4): #scrollup
                    context["scrollup"] = False
                elif (whichbutton == 5): #scrolldown
                    context["scrolldown"] = False
                else:
                    pass
        if not running:
            continue

        #mouse https://www.pygame.org/docs/ref/mouse.html
        context["leftdown"], context["rightdown"], context["middown"] = pygame.mouse.get_pressed()
        context["mousepos"] = pygame.mouse.get_pos() # -> (x, y)
        if context["leftdown"] and not context["leftwaspressed"]:
            context["leftpressed"] = True
        else:
            context["leftpressed"] = False

        if context["rightdown"] and not context["rightwaspressed"]:
            context["rightpressed"] = True
        else:
            context["rightpressed"] = False

        if context["middown"] and not context["midwaspressed"]:
            context["midpressed"] = True
        else:
            context["midpressed"] = False


        #for now not "zeroing" the screen, relying on background being sufficiently large, otherwise will need to use coloured fill to start frame
        currentbackground = "stars.png"
        blitque = [(images[currentbackground], (0, 0))] #refresh blitque with the background



        if ingame:
            menu[currentmenu]() #say, 0 or 1 or 2 etc.

        else:
            #Some text rendering
            title, titlerect = text_box("ExTerra", fontsize = 36, fontcolour = (150, 150, 150))
            subtitle = text_image("A William Webb & Alex Blandin 4X Space Game", 28, (120, 120, 120))

            #Set text positions
            titlerect = title.get_rect(centerx = context["screen_width"] / 2, y = 5)
            subtitlerect = subtitle.get_rect(centerx = context["screen_width"] / 2, centery = 50)

            #Showing it can blit to the background
            blitque.append((title, titlerect))
            blitque.append((subtitle, subtitlerect))

            pressed, newgame = button(text = "New Game", centerx = context["screen_width"] / 2, centery = 100, width = 108, height = 50, colour = (200, 200, 200), fontsize = 28, fontcolour = (10, 10, 10))
            if pressed:
                save.clear()
                print("New game")
                ingame = True
                currentmenu = 0
                #move to game state.
                #Redraw the frame with the maps and buttons.
                #open tutorial? We'll need to make some class to give the first instructions on how to interact with the interface.
            blitque.append(newgame)

            pressed, loadgame = button(text = "Load Game", centerx = context["screen_width"] / 2, centery = 175, width = 108, height = 50, colour = (200, 200, 200), fontsize = 28, fontcolour = (10, 10, 10))
            if pressed:
                save.load()
                print("Load game")
                ingame = True
                currentmenu = 0
                #give up the launch codes
                #Load the previous game state. Menus should be closed.
            blitque.append(loadgame)

            pressed, quitgame = button(text = "Fuck this Gay Earth", centerx = context["screen_width"] / 2, centery = 250, width = 108, height = 50, colour = (200, 200, 200), fontsize = 28, fontcolour = (10, 10, 10))
            if pressed:
                print("Quit Game")
                running = False
            blitque.append(quitgame)


        for image, rect in blitque: #blit straight to screen -- can do by layer IF NEEDED, would start with background & move forward
            screen.blit(image, rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__': main()
