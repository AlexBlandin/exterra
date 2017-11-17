#Import images
images["earth.png"] = import_image("earth.png", -1)
images["mountain.jpg"] = import_image("mountain.jpg")
images["player.png"] = import_image("player.png")


#Generate graphs
some_data_plot = linear_plot([3, 1, 2, 7], size_in_inches = [3, 3]) #plot the points, optional arguments after
images["linegraph"] = graph_image(some_data_plot) #generate an image pygame understands
images["piechart"] = graph_image(pie_chart([3.14159, 6.28318], labels = ["pi", "tau"], shadow = True, size_in_inches = [3.14, 3.14]))


#checking save works
print(save.__dict__) #print all of its members
save.playername = "Alex"
save.playertime += 1
save.save()
if save.playertime >= 4:
    save.clear()

#checking Singletons work
maze = Save()
endoftheuniverse = Save()
context["offset"] = 0

print("It is %s that Save() is a Singleton" % (save is maze is endoftheuniverse))


#Draw a white rect
rectangle, rectrect = box(x = (context["screen_width"]/2) - 300, y = 0, width = 600, height = 70, colour = (90, 90, 90))
blitque.append((rectangle, rectrect))

#Some text rendering
title, titlerect = text_box("ExTerra", fontsize = 36, fontcolour = (70, 70, 70))
subtitle = text_image("A William Webb & Alex Blandin 4X Space Game", 28, (10, 10, 10))

#Set text positions
titlerect = title.get_rect(centerx = context["screen_width"] / 2, y = 5)
subtitlerect = subtitle.get_rect(centerx = context["screen_width"] / 2, centery = 50)

#Showing it can blit to the background
blitque.append((title, titlerect))
blitque.append((subtitle, subtitlerect))


#Some graph rendering
blitque.append((images["linegraph"], (533, 300))) #and now we can blit a graph
blitque.append((images["piechart"], (100, 300)))


#Generate a more managable Earth. Might be impossible
earth = pygame.transform.scale(images["earth.png"], (256, 256))
earthrect = earth.get_rect(centerx = context["screen_width"] / 2, centery = (context["screen_height"] / 2 ) + context["offset"])

blitque.append((earth, earthrect))

clicked = within(context["mousepos"], earthrect)
if clicked and context["leftdown"]:
    context["offset"] -= 1
else:
    context["offset"] += 0.3

clicked, buttonpair = button(x = 700, y = 700, width = 100, height = 100, colour = (200, 200, 200))
if clicked:
    image, rect = buttonpair
    image.fill((170, 170, 170))
    buttonpair = image, rect
    print("TOUCH DAT BUTTON")
blitque.append(buttonpair)
