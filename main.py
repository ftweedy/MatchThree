# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("x_wing.jpeg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1000,1000))
    grid = [(50,200),(260,200),(470,200),(680,200)]

    # images on screen
    x_wing = pygame.image.load("x_wing.jpeg")
    x_wing = pygame.transform.scale(x_wing, (200, 200))
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        for x in grid:
                screen.blit(x_wing, x)
        pygame.display.flip()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()