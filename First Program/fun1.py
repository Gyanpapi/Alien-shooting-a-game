from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time

W_Width, W_Height = 500, 500

point_visible = True  # Variable to control point visibility
blink_animation = False  # Variable to control blinking animation
blink_duration = 0.5  # Duration of each blink in seconds
blink_start_time = 0  # Time when the blinking animation started

balls = []  # List to store ball positions
cl = []
ball_speed = 0.01
ball_size = 10
speed_increase = 0.001
move_points = True

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

def draw_points(x, y, s):
    glPointSize(s)
    glBegin(GL_POINTS)
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

def keyboardListener(key, x, y):
    global ball_size, move_points
    if key == b'w':
        ball_size += 1
        print("Size Increased")
    if key == b's':
        ball_size -= 1
        print("Size Decreased")
    if key == b' ':
        move_points = not move_points  # Toggle the move_points flag
        if move_points:
            print("Points Unfrozen")
        else:
            print("Points Frozen")
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global ball_speed
    if key == 'w':
        print(1)
    if key == GLUT_KEY_UP:
        ball_speed *= 2
        print("Speed Increased")
    if key == GLUT_KEY_DOWN:
        ball_speed /= 2
        print("Speed Decreased")
    glutPostRedisplay()

a = 0
b = 0
c = 0

def mouseListener(button, state, x, y):
    global balls, ball_speed, a, b, c, blink_animation, blink_start_time

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            c_X, c_y = convert_coordinate(x, y)
            a = random.uniform(0.0, 1.0)
            b = random.uniform(0.0, 1.0)
            c = random.uniform(0.0, 1.0)
            balls.append((c_X, c_y))
            cl.append([a, b, c])
            glutPostRedisplay()

    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            # Start the blinking animation
       
            ball_speed += speed_increase
            blink_animation = True
            blink_start_time = time.time()
            glutPostRedisplay()
            
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)

    for ball, c in zip(balls, cl):
        draw_points(ball[0], ball[1], ball_size)
        glColor3f(c[0], c[1], c[2])

    # Draw the point only when it should be visible


    glutSwapBuffers()

def animate():
    global point_visible, blink_animation, blink_start_time, blink_duration

    current_time = time.time()
    if move_points:
        for i in range(len(balls)):
            balls[i] = (balls[i][0] , (balls[i][1] + ball_speed) % 180)



def random_color():
    return (random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))

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
