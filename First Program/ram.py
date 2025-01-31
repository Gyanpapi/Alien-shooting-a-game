from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

W_Width, W_Height = 500,500


ballx = bally = 0
speed = 0.01
ball_size = 2
create_new = False

def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b

def draw_points(x, y, s):
    glPointSize(s) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def keyboardListener(key, x, y):

    global ball_size
    if key==b'w':
        ball_size+=1
        print("Size Increased")
    if key==b's':
        ball_size-=1
        print("Size Decreased")
    # if key==b's':
    #    print(3)
    # if key==b'd':
    #     print(4)

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed
    if key=='w':
        print(1)
    if key==GLUT_KEY_UP:
        speed *= 2
        print("Speed Increased")
    if key== GLUT_KEY_DOWN:		#// up arrow key
        speed /= 2
        print("Speed Decreased")
    glutPostRedisplay()

def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    global ballx, bally, create_new
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):    # 		// 2 times?? in ONE click? -- solution is checking DOWN or UP
            print(x,y)
            c_X, c_y = convert_coordinate(x,y)
            ballx, bally = c_X, c_y
        
    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN: 	
            create_new = convert_coordinate(x,y)
    # case GLUT_MIDDLE_BUTTON:
    #     //........

    glutPostRedisplay()


def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

  
    global ballx, bally, ball_size
    draw_points(ballx, bally, ball_size)
 

  

    if(create_new):
        m,n = create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(m,n)
        glEnd()


    glutSwapBuffers()


def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global ballx, bally,speed
    ballx=(ballx+speed)%250
    bally=(bally+speed)%250

def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL
