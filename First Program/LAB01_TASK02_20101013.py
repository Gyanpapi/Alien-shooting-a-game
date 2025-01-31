from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time

W_Width, W_Height = 500, 500

ballx = bally = 0
speed = 0.01
ball_size = 2
create_new = False
points = []  # List to store points
freeze = False  # Boolean to freeze/unfreeze points

blink_timer = 0  # Timer for blinking effect
blink_interval = 1  # Blinking interval in seconds
blinking = False  # Boolean to control blinking effect

def generate_random_point(x, y):
    new_point = point()
    new_point.x, new_point.y = convert_coordinate(x, y)
    new_point.color = (random.random(), random.random(), random.random())
    new_point.direction = (random.choice([-1, 1]), random.choice([-1, 1]))
    return new_point

class point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

def crossProduct(a, b):
    result = point()
    result.x = a.y * b.z - a.z * b.y
    result.y = a.z * b.x - a.x * b.z
    result.z = a.x * b.y - a.y * b.x
    return result

def convert_coordinate(x, y):
    global W_Width, W_Height
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y
    return a, b

def draw_points(x, y, s, color):
    glPointSize(s)
    glBegin(GL_POINTS)
    glColor3f(color[0], color[1], color[2])
    glVertex2f(x, y)
    glEnd()

def drawAxes():
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(250, 0)
    glVertex2f(-250, 0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0, 250)
    glVertex2f(0, -250)
    glEnd()
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(0, 1.0, 0.0)
    glVertex2f(0, 0)
    glEnd()

def drawShapes():
    glBegin(GL_TRIANGLES)
    glVertex2d(-170, 170)
    glColor3f(0, 1.0, 0.0)
    glVertex2d(-180, 150)
    glColor3f(1, 0, 0.0)
    glVertex2d(-160, 150)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2d(-170, 120)
    glColor3f(1, 0, 1)
    glVertex2d(-150, 120)
    glColor3f(0, 0, 1)
    glVertex2d(-150, 140)
    glColor3f(0, 1, 0)
    glVertex2d(-170, 140)
    glEnd()
is_frozen = False

def keyboardListener(key, x, y):
    global ball_size, is_frozen
    if key == b'w':
        ball_size += 1
        print("Size Increased")
    elif key == b's':
        ball_size -= 1
        print("Size Decreased")
    elif key == b' ':
        is_frozen = not is_frozen
        if is_frozen:
            print("Points Frozen")
        else:
            print("Points Unfrozen")

    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global speed
    if key == 'w':
        print(1)
    if key == GLUT_KEY_UP:
        speed *= 2
        print("Speed Increased")
    if key == GLUT_KEY_DOWN:
        speed /= 2
        print("Speed Decreased")
    if key == GLUT_KEY_RIGHT:
        pass
    if key == GLUT_KEY_LEFT:
        pass
    if key == GLUT_KEY_PAGE_UP:
        pass
    if key == GLUT_KEY_PAGE_DOWN:
        pass
    if key == GLUT_KEY_INSERT:
        pass
    if key == GLUT_KEY_HOME:
        pass
    if key == GLUT_KEY_END:
        pass
    glutPostRedisplay()

def timerCallback(value):
    global create_new
    create_new = None  # Clear the newly created point
    glutPostRedisplay()
    glutTimerFunc(1000, timerCallback, 0)  # Call the timer again after 1 second

def mouseListener(button, state, x, y):
    global ballx, bally, create_new, blinking
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            print(x, y)
            c_X, c_Y = convert_coordinate(x, y)
            ballx, bally = c_X, c_Y
            create_new = None  # Clear the newly created point
            toggle_blinking()  # Start or stop the blinking effect

    elif button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            create_new = generate_random_point(x, y)  # Generate a random point
            speed = 0.01  # Reset the speed when creating new points

    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    drawAxes()
    drawShapes()
    glBegin(GL_LINES)
    glVertex2d(180, 0)
    glVertex2d(180, 180)
    glVertex2d(180, 180)
    glVertex2d(0, 180)
    glEnd()
    global ballx, bally, ball_size
    draw_points(ballx, bally, ball_size, (1, 1, 1))
    draw_points(0, 0, ball_size, (1, 1, 1))
    for pt in points:
        draw_points(pt.x, pt.y, ball_size, pt.color)
    if create_new:
        m, n = create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(m, n)
        glEnd()
    glutSwapBuffers()

def animate():
    if not is_frozen:
        glutPostRedisplay()
        global ballx, bally, speed
        ballx = (ballx + speed) % 180
        bally = (bally + speed) % 180



def toggle_blinking():
    global blinking, blink_timer
    blinking = not blinking
    blink_timer = time.time()

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()
glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()
