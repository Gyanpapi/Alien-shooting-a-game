from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

x_position = -1.0
x1_position = 1.0
y_position = -0.9
y1_position = 0.9
state = 1
rFlag = 0

def cloud(b, c):
    glColor3f(1.0, 0.8, 0)
    glBegin(GL_POLYGON)
    for i in range(361):
        x = i * 3.142 / 180
        glVertex2f(0.100 + 0.060 * math.cos(x), 0.350 + 0.070 * math.sin(x))
    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    for i in range(361):
        x = i * 3.142 / 180
        y = i * 3.142 / 180
        glVertex2f(b + 0.050 * math.cos(x), c + 0.050 * math.sin(y))
    glEnd()

    t = b + 0.050 * math.cos(0)
    z = c + 0.050 * math.sin(0)
    glBegin(GL_POLYGON)
    for j in range(361):
        x = j * 3.142 / 180
        y = j * 3.142 / 180
        glVertex2f(t + 0.080 * math.cos(x), z + 0.080 * math.sin(y))
    glEnd()

    t = t + 0.070 * math.cos(0)
    z = z + 0.070 * math.sin(0)
    glBegin(GL_POLYGON)
    for k in range(361):
        x = k * 3.142 / 180
        y = k * 3.142 / 180
        glVertex2f(t + 0.050 * math.cos(x), z + 0.050 * math.sin(y))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    cloud(0.100, 0.250)
    cloud(0.600, 0.750)
    glutSwapBuffers()

def timer(v):
    global state, rFlag, x_position, y_position, x1_position, y1_position
    glutPostRedisplay()
    glutTimerFunc(int(1000/60), timer, 0)

    if rFlag == 1:
        if state == 1:
            if x_position < 0.9 or y_position < 0.2 or x1_position > -0.9 or y1_position > -0.9:
                x_position += 0.002
                y_position += 0.002
                x1_position -= 0.002
                y1_position -= 0.002
            else:
                state = 2
        elif state == 2:
            if x_position > -1 or y_position > -0.3 or x1_position < 0.9 or y1_position < 0.2:
                x_position -= 0.002
                y_position -= 0.002
                x1_position += 0.002
                y1_position += 0.002
            else:
                state = 1

    # Add similar if conditions for rFlag == 2, rFlag == 3, etc.

def reshape(w, h):
 #   glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-0, 0, -0, 0)
 #   glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"Parachute Animation")
    glutDisplayFunc(display)
 #   glutReshapeFunc(reshape)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
