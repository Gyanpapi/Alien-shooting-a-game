from OpenGL.GL import *
from OpenGL.GLUT import *
import math

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
list1= []
factor= 1.0
paused = False
def circ_point(x, y, cx, cy):
    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)
    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)
    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)
    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)

def mid_circle(cx, cy, radius):
    d = 1 - radius
    x = 0
    y = radius

    circ_point(x, y, cx, cy)

    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * x - 2 * y + 5
            y = y - 1
        x = x + 1
        circ_point(x, y, cx, cy)

def initialize():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_circle_with_midpoint(cx, cy, radius):
    mid_circle(cx, cy, radius)

def draw_circles():
    for i in list1:
        x, y, radius = i
        draw_circle_with_midpoint(x, y, radius)

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(1.0, 1.0, 1.0) 
    glPointSize(1.5)
    glBegin(GL_POINTS)
    draw_circles()
    up_list1()
    glEnd()

    glutSwapBuffers()

def up_list1():
  
    global paused,list1
    if not paused:
        for i in list1:
            x, y, radius = i
            i[2] += factor
            if x - radius < 0 or x + radius > WINDOW_WIDTH or y - radius < 0 or y + radius > WINDOW_HEIGHT:
                list1.remove(i) 
        glutPostRedisplay()

def mouse(button, state, x, y):
    global list1
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
       list1.append([x, WINDOW_HEIGHT - y, 5])  
       
def specialKeyListener(key, x, y):
    global paused, factor
    if key == b' ':
        paused = not paused
    elif key == b'\x1b':  
        glutLeaveMainLoop()
    elif key == GLUT_KEY_LEFT and factor < 10.0:  
        factor += 0.1
    elif key == GLUT_KEY_RIGHT and factor >0.1:  
        factor -= 0.1
        print(factor)
    glutPostRedisplay()
def initialize_display():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"Water")
    glutDisplayFunc(draw_scene)
    glutMouseFunc(mouse)
    glutSpecialFunc(specialKeyListener)
    glEnable(GL_DEPTH_TEST)
    initialize()
    glutMainLoop()

initialize_display()