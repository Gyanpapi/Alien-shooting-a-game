from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def circlePoints(x, y, x0, y0):
    draw_points(x + x0, y + y0)
    draw_points(y + x0, x + y0)
    draw_points(y + x0, -x + y0)
    draw_points(x + x0, -y + y0)
    draw_points(-x + x0, -y + y0)
    draw_points(-y + x0, -x + y0)
    draw_points(-y + x0, x + y0)
    draw_points(-x + x0, y + y0)

def midpointcircle(radius, x0, y0):
    d = 1 - radius
    x = 0
    y = radius

    circlePoints(x, y, x0, y0)

    while x < y:
        #print("y")
        if d < 0:
            # Choose East.
            d = d + 2*x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2*x -2*y + 5
            x += 1
            y = y - 1

        circlePoints(x, y, x0, y0)

def draw_circle(radius, x0, y0):
    midpointcircle(radius, x0, y0)        # outer circle

  
  

# This function is used to draw pixels.
def draw_points(x, y):
    # The parameter that is passed in the function dictates the size of the pixel.
    glPointSize(2)

    glBegin(GL_POINTS)

    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(x, y)

    glEnd()



def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # (Red, Green, Blue)
    glColor3f(1.0, 1.0, 1.0)

    ###============================###
    ### call_the_draw_methods_here ###
    ###============================###
    draw_circle(300, 500, 500)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)

# Size of the window.
# Manipulating this value will let us change the size of the output widow where the pixel is shown.
glutInitWindowSize(1000, 1000)

glutInitWindowPosition(0, 0)

# window name
wind = glutCreateWindow(b"LAB03_MidpointCircle")

glutDisplayFunc(showScreen)
glutMainLoop()