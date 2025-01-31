from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Constants
PI = 3.1416

# Variables
i, j, k = 0, 0, 0
sun_spin, sun_x, sun_y = 0.0, 0.0, 0.0
ax, bx, cx, dx, str, mn = 0.0, 0.0, 0.0, 0.0, 500.0, 500.0
sr, sg, sb = 0.0, 0.749, 1.0
spin = 0.0

def init():
    glClearColor(.40, .110, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 1000.0, 0.0, 500.0)

def circle(rad):
    points = 50
    delTheta = (2.0 * PI) / points
    theta = 0.0

    glBegin(GL_POLYGON)
    for _ in range(points + 1):
        glVertex2f(rad * math.cos(theta), rad * math.sin(theta))
        theta += delTheta
    glEnd()

def Sun_Model():
    glPushMatrix()
    glTranslatef(500, 0, 0)
    circle(30)
    glPopMatrix()

def Moving_Sun_Model():
    glPushMatrix()
    glRotatef(-sun_spin, 0, 0, -.009)
    Sun_Model()
    glPopMatrix()

def cloud_model_one():
    glColor3f(1.25, 0.924, 0.930)

    # Top_Left
    glPushMatrix()
    glTranslatef(320, 210, 0)
    circle(15)
    glPopMatrix()

    # Top
    glPushMatrix()
    glTranslatef(340, 225, 0)
    circle(16)
    glPopMatrix()

    # Right
    glPushMatrix()
    glTranslatef(360, 210, 0)
    circle(16)
    glPopMatrix()

    # Middle_Fill
    for x in range(305, 365, 5):
        glPushMatrix()
        glTranslatef(x, 210, 0)
        circle(16)
        glPopMatrix()

    for x in range(305, 365, 5):
        glPushMatrix()
        glTranslatef(x, 204, 0)
        circle(10)
        glPopMatrix()

# Continue with the rest of your functions here...
def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        glutIdleFunc(move_right)
    elif button in (GLUT_MIDDLE_BUTTON, GLUT_RIGHT_BUTTON) and state == GLUT_DOWN:
        glutIdleFunc(None)

def Sun():
    glColor3f(1, 1, 0)
    glPushMatrix()
    Moving_Sun_Model()
    glPopMatrix()
def cloud_one():
    glPushMatrix()
    glTranslatef(cx, -40, 0)
    cloud_model_one()
    glPopMatrix()
def sun_move():
    global sun_spin
    sun_spin = sun_spin + 0.0008

def move_right():
    global spin, ax, bx, cx, dx
    sun_move()
    spin = spin + 0.1
    ax = ax + 0.05
    bx = bx + 0.08
    cx = cx + 0.10
    dx = dx + 0.15

    if cx > 1000:
        cx = -300
    if bx > 1000:
        bx = -400
    if cx > 1000:
        cx = -400
    if dx > 1000:
        dx = -500

    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)

    # Call your drawing functions here...
    Sun()

    cloud_one()
 

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(50, 50)  
    glutInitWindowSize(300, 1300)
    glutCreateWindow(b"Smart Village")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMainLoop()

if __name__ == "__main__":
    main()
