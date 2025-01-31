from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *





def init():
    glClearColor(0.0, 0.0, 0.0, 0)
    glColor3f(1.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1200, 1200, -700, 700)
    glMatrixMode(GL_MODELVIEW)




def DrawSpaceshipBody(isPlayer1):
    if isPlayer1:
        glColor3f(1, 0, 0)
    else:
        glColor3f(0.5, 0, 0.5)

    # Main body
    glPushMatrix()
    glScalef(70, 20, 1)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

    # Side lights
    glPushMatrix()
    glScalef(3, 3, 1)

    for _ in range(3):
        glTranslated(5, 0, 0)
        glColor3fv((1, 0, 1))  # You can replace this with LightColor[(CI+i)%3]
        glutSolidSphere(1, 1000, 1000)

    glPopMatrix()


def DrawSpaceshipDoom():
    glColor4f(0.7,1,1,0.0011)
    glPushMatrix()
    glTranslated(0,30,0)
    glScalef(35,50,1)
    glutSolidSphere(1,50,50)
    glPopMatrix()

   # glVertex2f(xend, yend)
    glEnd()









def display():
    #keyOperations()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    DrawSpaceshipBody(True)
    DrawSpaceshipDoom()
 
    glFlush()
    glLoadIdentity()
    glutSwapBuffers()








def mouse(button, state, x, y):
    global mButtonPressed, mouseX, mouseY
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        mButtonPressed = True
        mouseX = x
        mouseY = y
    elif button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        mButtonPressed = False





XMAX = 1200
YMAX = 700


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(XMAX, YMAX)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Space Invaders")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
 
    glutMouseFunc(mouse)

    glutMainLoop()


if __name__ == "__main__":
    main()
