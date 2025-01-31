from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set the clear color to black
    glClear(GL_COLOR_BUFFER_BIT)     # Clear the color buffer
    glutSwapBuffers()                # Swap buffers to display the dark screen

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutCreateWindow("Dark Screen")
glutDisplayFunc(display)
glutMainLoop()