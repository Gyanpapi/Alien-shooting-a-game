from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin

# Initial position of the parachute
parachute_y = 1.0

# Initial state of the people (0 = sad, 1 = happy)
people_state = 0

def draw_people(state):
    # Draw the people
    glColor3f(state, 1 - state, 0)  # Red when sad, green when happy
    for i in range(-5, 6):
        glRectf(i * 0.2 - 0.1, -1.0, i * 0.2, -0.9)

def draw_parachute():
    global parachute_y, people_state

    # Draw the parachute
    glColor3f(1.0, 1.0, 1.0)  # White color
    glBegin(GL_POLYGON)
    for i in range(360):
        glVertex2f(0.0 + 0.1 * cos(i), parachute_y + 0.1 * sin(i))
    glEnd()

    # Draw the strings
    glColor3f(0.0, 0.0, 0.0)  # Black color
    glBegin(GL_LINES)
    glVertex2f(0.0, parachute_y - 0.1)
    glVertex2f(0.0, parachute_y - 0.2)
    glEnd()

    # Draw the person
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glBegin(GL_POLYGON)
    for i in range(360):
        glVertex2f(0.0 + 0.05 * cos(i), (parachute_y - 0.2) + 0.05 * sin(i))
    glEnd()

    # If the parachute has reached the bottom, change the state of the people
    if parachute_y <= -0.8:
        people_state = 1

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_people(people_state)
    draw_parachute()
    glutSwapBuffers()

def timer(v):
    global parachute_y
    parachute_y -= 0.01  # Move the parachute down
    if parachute_y < -1.0:  # If the parachute is off the screen, move it back to the top
        parachute_y = 1.0
    glutPostRedisplay()
    glutTimerFunc(int(1000/60), timer, 0)

def main():
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"Parachute Animation")
    glutDisplayFunc(display)
    glutTimerFunc(0, timer, 0)
    glClearColor(0.0, 0.0, 1.0, 1.0)  # Set the background color to blue
    glutMainLoop()

if __name__ == "__main__":
    main()
