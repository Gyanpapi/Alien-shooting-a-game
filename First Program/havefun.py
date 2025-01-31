from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
random.randint(0, 4)
import sys
bg_color=0
bg_color1=0
bg_color2=1
bg_color3=0

h = 0
#pause_game=False

expFactor = 1.0



i = -245
j = -90

Bombed = 0

h = 0




def reshape(width, height):
    fieldOfView = 90.0
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-662, 662, -350, 350, -450, 450)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()





moon_j=100

byebye_spaceship=0
explode1=1  
def explode():
    
    global expFactor,list1

 
       
    glColor3f(1, 1, 1)
       
    draw_circle2(2+expFactor,list1[0][0],list1[0][1],1)
    

        

    expFactor=expFactor+20
    if(expFactor>100):
        explode1=0
  

list1=[]
    
def mouseListener(button, state, x, y):
   
  #  print(bomb_x-648," ",bomb_x+649)
    global list1
    if button == GLUT_LEFT_BUTTON :
        if state==GLUT_DOWN:
            print(x," ",y)
            y=300-y
            x=x
            print(x," ",y)
            list1.append([x,y])
    if button == GLUT_RIGHT_BUTTON:
        if state==GLUT_DOWN:
            pass

def draw():
    global bg_color,list1
    #glColor3f(color.red, color.green, color.blue)
    bg_color1=0
    bg_color2=0.5
    bg_color3=0.9
    if(bg_color==0):
        
        glClearColor(bg_color1, bg_color2, bg_color3, 1)
        
    else:
        glClearColor(0, 0, 0.3, 1)
        
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    if(len(list1)>0):
        explode()


    glFlush()
    glutSwapBuffers()
        
        
def idle():
    glutPostRedisplay()

def initGL(width, height):
    reshape(width, height)
    glClearColor(1.2, 0.8, 1.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    

############# mid circle 2 ################
def circlePoints2(x, y, x0, y0,d):
    draw_points2(x + x0, y + y0,d)
    draw_points2(y + x0, x + y0,d)
   
    draw_points2(y + x0, -x + y0,d)
    draw_points2(x + x0, -y + y0,d)
    draw_points2(-x + x0, -y + y0,d)
    draw_points2(-y + x0, -x + y0,d)
    draw_points2(-y + x0, x + y0,d)
    draw_points2(-x + x0, y + y0,d)

def midpointcircle2(radius, x0, y0,d):
    d = 1 - radius
    x = 0
    y = radius

    circlePoints2(x, y, x0, y0,d)

    while x < y:
        #print("y")
        if d < 0:
            # Choose East.
            d = d + 2*x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2*x -2*y + 5
            x += 1
            y = y - 1

        circlePoints2(x, y, x0, y0,d)

def draw_circle2(radius, x0, y0,d):
    midpointcircle2(radius, x0, y0,d)        # outer circle


# This function is used to draw pixels.
def draw_points2(x, y,d):
    # The parameter that is passed in the function dictates the size of the pixel.

    glPointSize(2)

    glBegin(GL_POINTS)

    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    
    glVertex2f(x, y)

    glEnd()

######################################
# ... Midpoint line algo code...

    

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"pROOJECT")

    # register glut call backs
glutMouseFunc(mouseListener)
glutReshapeFunc(reshape)
glutDisplayFunc(draw)
  
glutIdleFunc(idle)
glutIgnoreKeyRepeat(1)  # ignore key repeat

initGL(1244, 700)
glutMainLoop()