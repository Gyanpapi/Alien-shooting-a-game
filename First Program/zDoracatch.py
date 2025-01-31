from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
from random import randint
import ctypes
window = 0                                             # glut window number
width, height = 500, 500                               # window size
dx, dy = 0, 0                                         # diamond position
bx = 0                                                 # basket x position
score = 0                                              # player's score

def draw_text(x, y, text):
    glColor3f(1, 1, 1)                                 # set color to white
    glWindowPos2f(x, y)                                # set position
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ctypes.c_int(ord(ch)))
        
def draw_diamond(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle

def draw_basket(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle
    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point
    glEnd()                                            # done drawing a rectangle

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw():                                            # ondraw is called all the time
    global dx, dy, bx, score
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d

    glColor3f(0.0, 0.0, 1.0)                           # set color to blue
    draw_diamond(dx, dy, 10, 10)                       # draw the diamond
    glColor3f(1.0, 0.0, 0.0)                           # set color to red
    draw_basket(bx, 10, 30, 10)                        # draw the basket

    dy -= 0.01                                        # move diamond slower
    if dy < 0:                                         # if diamond is at the bottom
        if dx < bx or dx > bx + 30:                    # if diamond is not caught by the basket
            print("Game Over")
            sys.exit(0)
        dy = height                                    # reset diamond position
        dx = randint(10, width - 10)
        score += 1                                     # increase score

    draw_text(10, height - 30, "Score: " + str(score)) # draw score

    glutSwapBuffers()                                  # important for double buffering                            # important for double buffering

def keyboard(*args):
    global bx
    if args[0] == b'a':
        bx -= 5                                        # move basket left
    elif args[0] == b'd':
        bx += 5                                        # move basket right

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow(b"Diamond Catching Game")    # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutKeyboardFunc(keyboard)                             # tell opengl that we want to check the keyboard
glutMainLoop()                                         # start everything
