from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from math import cos,sin
# Initial position of the stick figure
stick_y = 0.0

# Initial state of the stick figure (0 = left, 1 = right)
stick_state = 0

def draw_stick_figure(state):
    # Draw the head
    glColor3f(1.0, 1.0, 1.0)  # White color
    glBegin(GL_POLYGON)
    for i in range(360):
        glVertex2f(0.0 + 0.1 * cos(i), stick_y + 0.1 * sin(i))
    glEnd()

    # Draw the body
    glColor3f(1.0, 1.0, 1.0)  # White color
    glBegin(GL_LINES)
    glVertex2f(0.0, stick_y - 0.1)
    glVertex2f(0.0, stick_y - 0.3)
    glEnd()

    # Draw the arms
    glColor3f(1.0, 1.0, 1.0)  # White color
    glBegin(GL_LINES)
    if state == 0:
        glVertex2f(-0.1, stick_y - 0.15)
        glVertex2f(0.1, stick_y - 0.15)
    else:
        glVertex2f(-0.1, stick_y - 0.25)
        glVertex2f(0.1, stick_y - 0.25)
    glEnd()

    # Draw the legs
    glColor3f(1.0, 1.0, 1.0)  # White color
    glBegin(GL_LINES)
    if state == 0:
        glVertex2f(0.0, stick_y - 0.3)
        glVertex2f(-0.1, stick_y - 0.4)
        glVertex2f(0.0, stick_y - 0.3)
        glVertex2f(0.1, stick_y - 0.4)
    else:
        glVertex2f(0.0, stick_y - 0.3)
        glVertex2f(-0.1, stick_y - 0.5)
        glVertex2f(0.0, stick_y - 0.3)
        glVertex2f(0.1, stick_y - 0.5)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_stick_figure(stick_state)
    glutSwapBuffers()

def timer(v):
    global stick_state
    stick_state = (stick_state + 1) % 2  # Change the state of the stick figure
    glutPostRedisplay()
    glutTimerFunc(int(1000/60), timer, 0)

def main():
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"Stick Figure Animation")
    glutDisplayFunc(display)
    glutTimerFunc(0, timer, 0)
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set the background color to black
    glutMainLoop()

if __name__ == "__main__":
    main()
