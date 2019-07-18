# sandbox version of Asteroids program
# have the spaceship update handler working more-or-less
# 28 Jul 2015; 1017

import math
import random
import time

import pygame, sys
from pygame.locals import *


# Define some colors as global constants
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time_r = 0
# add comment line
tabulae = pygame.display.set_mode([WIDTH, HEIGHT])

def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    #def __init__(self, pos, vel, angle, image, info):
    def __init__(self, pos, vel, angle):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        #self.image = image
        #self.image_center = info.get_center()
        #self.image_size = info.get_size()
        #self.radius = info.get_radius()
        self.radius = 15
    def draw(self,canvas):
        self.pos[0] = int(self.pos[0])
        self.pos[1] = int(self.pos[1])
        self.radius = int(self.radius)
        #print('self.pos: ', self.pos)
        pygame.draw.circle(canvas, WHITE, self.pos, self.radius, 0)
        #canvas.blit(ship_image, (self.pos[0], self.pos[1], 90, 90), (0, 0, 90, 90))
    def update(self):
        # position update
        self.pos[0] = self.pos[0] + self.vel[0]
        self.pos[1] = self.pos[1] + self.vel[1]
        # friction update
        FRIC = .1
        self.vel[0] = (self.vel[0] * (1 - FRIC))
        self.vel[1] = (self.vel[1] * (1 - FRIC))
        #print('time: ', time_r,'self.vel: ', self.vel)
        
        # thrust update
        forward = [math.cos(self.angle), math.sin(self.angle)]
        if self.thrust:
            self.vel[0] = self.vel[0] + forward[0]
            self.vel[1] = self.vel[1] + forward[1]

def draw(canvas):
    global time_r

    # animiate background
    time_r += 1
    wtime = (time_r / 4) % WIDTH
    #center = debris_info.get_center()
    #size = debris_info.get_size()
    ##print('time: ', time_r, ' wtime: ', wtime, ' center: ', center, ' size: ', size)
    #canvas.blit(nebula_image, (0, 0, WIDTH, HEIGHT))
    ##canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, #HEIGHT])
    ##canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    #dx = int(wtime - WIDTH / 2)
    #dy = int(HEIGHT / 2 - 300)
    #canvas.blit(debris_image, (dx, dy, WIDTH, HEIGHT))
    ##canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    #dx = int(wtime + WIDTH / 2)
    #canvas.blit(debris_image, (dx, dy, WIDTH, HEIGHT))
    ## draw ship and sprites
    ##TODO how do these objects get created ??
    ##  It looks like they get initialized in the 'main' function; need to 
    ##  recheck, but I think it might run this way
    my_ship.draw(canvas)
    #a_rock.draw(canvas)
    #a_missile.draw(canvas)
    
    ## update ship and sprites
    my_ship.update()
    #a_rock.update()
    #a_missile.update()

    
pygame.display.set_caption("Asteroids")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()  

#my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0)

my_ship.vel[0] = 3
my_ship.vel[1] = 4
my_ship.thrust = True
my_ship.angle = .4
my_event = USEREVENT + 0
pygame.time.set_timer(my_event, 750)
my_event_cnt = 0
t = 0.00
# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == my_event:
            t = time.clock()
            print('my event count: ', my_event_cnt, ' time: ', t)
            my_event_cnt = my_event_cnt + 1
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
 
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
   
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

    my_ship.angle = my_ship.angle + .07 +(.07*time_r/100) 

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # TODO (recheck this) I think this needs to come out, as we are 
    #  putting up a background image
    tabulae.fill(GREEN)
    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    draw(tabulae)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()

    # Limit to 20 frames per second
    clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
#sys.exit()
#quit()


