from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from math import sin,cos
import random
scene = 0
flag2 = 0
flag3 = 0
bg_color=1

h = 0

explodeTx = 1.0
explodeTy = 1.0
expFactor = 1.0
scene = 1
x = 0
y = -195
opt = 0
clouds = 0

wx1 = [-670, -150, 418]
wy1 = -232

cx = [-540, -150, 520, -30, -540, -150, 520, -30]
cy = [210, 130, 250, 250, -210, -130, -250, -250]

i = -245
j = -90

Bombed = 0
flag2 = 0
h = 0
flag3 = 0



import math

pi = math.pi

class RgbColor:
    def __init__(self, red, green, blue, alpha):
        self.red = red / 256
        self.green = green / 256
        self.blue = blue / 256
        self.alpha = alpha

def createColor(red, green, blue, alpha):
    return RgbColor(red, green, blue, alpha)



def reshape(width, height):
    fieldOfView = 90.0
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-662, 662, -350, 350, -450, 450)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Need to write code 


def Bomb():
    global j, Bombed
    if Bombed == 1:
        j=j-1
        print(j)

  

    glBegin(GL_POLYGON)
    color = createColor(0, 139, 34, 0)
    if(Bombed):
        glColor3f(color.red, color.green, color.blue)

        

    glVertex3f(-5, 205+j, 0)
    glVertex3f(0, 200+j, 0)
    glVertex3f(100, 200+j, 0)
    glVertex3f(120, 215+j, 0)
    glVertex3f(100, 230+j, 0)
    glVertex3f(0, 230+j, 0)
    glVertex3f(-5, 225+j, 0)
    glEnd()
  
    glBegin(GL_TRIANGLES)
    color = createColor(34, 139, 34, 0)
    glColor3f(color.red, color.green, color.blue)
    glVertex3f(100, 215+j, 0)
    glVertex3f(140, 205+j, 0)
    glVertex3f(140, 225+j, 0)
    glEnd()

    glLineWidth(12.5)
parachute_y=1.0
def timer(v):
    global parachute_y
    parachute_y -= 0.01  # Move the parachute down
    if parachute_y < -1.0:  # If the parachute is off the screen, move it back to the top
        parachute_y = 1.0
    glutPostRedisplay()
    glutTimerFunc(int(1000/60), timer, 0)

def draw_parachute():
    global parachute_y

    # Draw the parachute
    glColor3f(1.0, 1.0, 1.0)  # White color
    glBegin(GL_POLYGON)
    for i1 in range(360):
        glVertex2f(100.0 + 0.1 * cos(i1), parachute_y + 0.1 * sin(i1))
    glEnd()

    # Draw the strings
    glColor3f(0.0, 0.0, 0.0)  # Black color
    glBegin(GL_LINES)
    glVertex2f(41.0, parachute_y - 0.1)
    glVertex2f(5.0, parachute_y - 0.2)
    glEnd()

    # Draw the person
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glBegin(GL_POLYGON)
    for i1 in range(360):
        glVertex2f(100.0 + 0.05 * cos(i1), (parachute_y - 0.2) + 0.05 * sin(i1))
    glEnd()
def Jet():
    global i, Bombed
    
    if Bombed == 0:
        if scene == 3:
            i += 2
        else:
            i += 2
    else:
        i+=2
        print(i)
        print(Bombed)
        
    if(i>400):
        Bombed=1
        Bomb()
    ############ mahin nnnn
    
    glBegin(GL_POLYGON)  # body
    color = createColor(0, 0, 0, 0)
    glColor3f(color.red, color.green, color.blue)
    glColor3f(0,0.5 ,0)
    glVertex3f(-600+i, 130, 0)
    glVertex3f(-300+i, 130, 0)
    glColor3f(0.9,0 , color.blue)
    glVertex3f(-350+i, 170, 0)
    glColor3f(0.9,0 , color.blue)
    glVertex3f(-550+i, 170, 0)
    glVertex3f(-600+i, 245, 0)
    glEnd()

    glBegin(GL_POLYGON)  # glass
    color = createColor(168, 225, 232, 0)
    glColor3f(color.red, color.green, color.blue)
   
    glVertex3f(-380+i, 150, 0)
    glVertex3f(-340+i, 150, 0)
    glVertex3f(-360+i, 160, 0)
    glVertex3f(-380+i, 160, 0)
    glEnd()

k=315
m=0
def DrawSpaceshipBody(isPlayer1):
    global k,m
    a=random.random() # Choose a random color
    b=random.random() # Choose a random color
    c=random.random() # Choose a random color
    if(a<0.5 and b<0.5 and c<0.5):    # to avoid a color that is similar to the background 
        b=1.5       
        
    glColor3f(0.5,0,0.5)
    
    if k>-230:
        k=k-4
    else:
        m=m-1
    # Main body
    glPushMatrix()
    glTranslated(m,70+k,0)
    glScalef(100, 25, 1)
    glutSolidSphere(1, 70, 70)
    glPopMatrix()

    # Side lights
    glColor3f(a,b,c)
    glPushMatrix()
    glTranslated(m,70+k-5,0)
    glScalef(10, 10, 1)
    glutSolidSphere(1, 70, 70)
    glPopMatrix()
    
    glColor3f(b,a,c)
    glPushMatrix()
    glTranslated(m-20,70+k-5,0)
    glScalef(10, 10, 1)
    glutSolidSphere(1, 70, 70)
    glPopMatrix()
    
    glColor3f(c,b,a)
    glPushMatrix()
    glTranslated(m+20,70+k-5,0)
    glScalef(10, 10, 1)
    glutSolidSphere(1, 70, 70)
    glPopMatrix()
    
    glColor3f(a,b,a)
    glPushMatrix()
    glTranslated(m+40,70+k-5,0)
    glScalef(10, 10, 1)
    glutSolidSphere(1, 70, 70)
    glPopMatrix()
    
    glColor3f(c,a,b)
    glPushMatrix()
    glTranslated(m-40,70+k-5,0)
    glScalef(10, 10, 1)
    glutSolidSphere(1, 70, 70)
    glPopMatrix()



def DrawSpaceshipDoom():
    global k,m
    print(k)
    glColor4f(0.7,1,1,0.0011)
    glPushMatrix()
    glTranslated(m,100+k,0)
    glScalef(45,50,1)
    glutSolidSphere(1,80,80)
    glPopMatrix()


   
   
def explode():
    global expFactor
    color = createColor(237, 105, 74, 0)
    glColor3f(color.red, color.green, color.blue)
    Circle(-10, -130, 0, 10.0*expFactor , 200)

    color = createColor(216, 85, 58, 0)
    glColor3f(color.red, color.green, color.blue)
    Circle(0, -135, 0, 10.0* expFactor , 200)

def Circle(cx, cy, cz, r, num_segments):
    ii = 0
    theta = 0
    x = 0
    y = 0
    j = num_segments if clouds == 0 else num_segments // 2

    glBegin(GL_POLYGON)
    for ii in range(j):
        i = ii / num_segments
        theta = 2.0 * pi * i
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex3f(x + cx, y + cy, cz)
    glEnd()
    
def Clouds(r):
    global clouds, cx, cy, scene, Bombed
    c = 0
    clouds = 1
    for c in range(3):
        color = createColor(255, 255, 255, 0)
        glColor3f(color.red, color.green, color.blue)

        # clouds half circle
        Circle(cx[c], cy[c], 0, r, 200)
        Circle(cx[c]+40, cy[c]+20, 0, r, 200)
        Circle(cx[c]+70, cy[c], 0, r, 200)
        Circle(cx[c]+100, cy[c], 0, r, 200)
        Circle(cx[c], cy[c], 0, r, 200)
        Circle(cx[c]+40, cy[c]+20, 0, r, 200)
        Circle(cx[c]+70, cy[c], 0, r, 200)
        Circle(cx[c]+100, cy[c], 0, r, 200)
        

def createColor1(r, g, b, a):
    return {'red': r/255.0, 'green': g/255.0, 'blue': b/255.0, 'alpha': a/255.0}



def Background():
    glPushMatrix()
    # gradient BG
    glBegin(GL_POLYGON)
    color = createColor(109, 209, 241, 0)
    glColor3f(color.red, color.green, color.blue)
    glVertex3f(-670, -350, -2)
    glVertex3f(670, -350, -2)
    glVertex3f(670, 350, -2)
    glVertex3f(-670, 350, -2)
    glEnd()
    # drawing clouds
    Clouds(25)
    Clouds(25)
    Clouds(25)
    Clouds(25)
    glPopMatrix()



def City():
    glBegin(GL_QUADS)  # b1
    color = createColor1(163, 163, 194, 0)
    glColor3f(color['red'], color['green'], color['blue'])
    glVertex3f(-670, -210, 0)
    glVertex3f(-500, -210, 0)
    glVertex3f(-500, 100, 0)
    glVertex3f(-670, 100, 0)
    glEnd()

    # Repeat the following block for each glass in the building
    glBegin(GL_QUADS)  # b1 glass1
    color = createColor1(193, 215, 215, 0)
    glColor3f(color['red'], color['green'], color['blue'])
    glVertex3f(-670, -200, 0)
    glVertex3f(-500, -200, 0)
    glVertex3f(-500, -190, 0)
    glVertex3f(-670, -190, 0)
    glEnd()

    # ... repeat for each glass ...

    glBegin(GL_QUADS)  # b1 glass15
    color = createColor1(193, 215, 215, 0)
    glColor3f(color['red'], color['green'], color['blue'])
    glVertex3f(-670, 60, 0)
    glVertex3f(-500, 60, 0)
    glVertex3f(-500, 70, 0)
    glVertex3f(-670, 70, 0)
    glEnd()


def scene8():
    glPushMatrix()
    global i, j, flag2, Bombed, explodeTx, explodeTy, expFactor
    if flag2 == 0:
        i = -690
        j = 400
        flag2 = 1
    Background()
    City()
    Bomb()
    Bombed=1
    if explodeTx <= 1.3:
            explodeTy += 0.001
            explodeTx = explodeTy
    expFactor = expFactor if expFactor >= 1000 else expFactor + 1
    if int(j) == -420:
        Bombed = 1
    
    if Bombed:
        glPushMatrix()
        glLoadIdentity()
        glScalef(explodeTx, explodeTy, 0)
        glTranslatef(0.05, 0, 0)
        explode()
        glPopMatrix()

        glPushMatrix()
        glLoadIdentity()
        glScalef(explodeTx, explodeTy, 0)
        glTranslatef(0.1, 0, 0)
        explode()
        glPopMatrix()

        if explodeTx <= 1.3:
            explodeTy += 0.0001
            explodeTx = explodeTy
        expFactor = expFactor if expFactor >= 1000 else expFactor + 0.000000001
    glPopMatrix()
    
def Text(text, x, y, z):
    # The color
    glColor3f(1, 1, 1)
    # Position of the text to be printed
    glRasterPos3f(x, y, z)
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))

def printLines(s, offsetY, n, x, y):
    i = 0
    for i in range(n):
        Text(s[i], x, y + offsetY, 0)
        offsetY -= 35
        
def scene1():
    glPushMatrix()
 
    glPopMatrix()

# ... (similarly for other scene functions)


def parasuit():
    global j1, parasuited
    if parasuit == 0:
        if scene == 8:
            j1 -= 4
        else:
            j1 -= 4

    glBegin(GL_POLYGON)
    color = createColor(0, 139, 34, 0)
    glColor3f(color.red, color.green, color.blue)
    glVertex3f(-5, 205+j, 0)
    glVertex3f(0, 200+j, 0)

    glEnd()

    glBegin(GL_TRIANGLES)
    color = createColor(34, 139, 34, 0)
    glColor3f(color.red, color.green, color.blue)
    glVertex3f(100, 215+j, 0)
    glVertex3f(140, 205+j, 0)
    glVertex3f(140, 225+j, 0)
    glEnd()

    glLineWidth(12.5)
def draw():
    global bg_color
    glClearColor(bg_color, bg_color, bg_color, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    Background()
    DrawSpaceshipDoom()
    DrawSpaceshipBody(True)
    explode()
    #draw_parachute()
    #Flames(4,5)
    #Candles()
  #  draw_parachute()
    blust()
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(250,0)
    glVertex2f(-250,0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0,250)
    glVertex2f(0,-250)

    glEnd()
    Jet()
   # Bomb()
 
    
    # render the scene here
    if scene == 0:
        scene1()
      
    elif scene==1:
        scene1()
    elif scene == 2:
   
        pass
    elif scene == 8:
        scene8()
    # ... (similarly for other scenes)

    glFlush()
    glutSwapBuffers()

def blust():
    glPushMatrix()
    global i, j, flag2, Bombed, explodeTx, explodeTy, expFactor

 
    #Bombed=1
    if explodeTx <= 1.3:
            explodeTy += 0.001
            explodeTx = explodeTy
    expFactor = 0 if expFactor >= 1000 else expFactor + 1
    if expFactor>200:
        expFactor=0
        print(expFactor)
    glPopMatrix()
        
def idle():
    glutPostRedisplay()

def initGL(width, height):
    reshape(width, height)
    glClearColor(1.2, 0.8, 1.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    
def specialKeyListener(key, x, y):
    global bg_color
    if key == GLUT_KEY_LEFT :  # left arrow key
        bg_color= 1 
    elif key == GLUT_KEY_RIGHT :  # right arrow key
        bg_color=0
    else:
        pass
    glutPostRedisplay()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1300, 700)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"HIROSHIMA BOMBING")

    # register glut call backs
  
    glutSpecialFunc(specialKeyListener)
    glutReshapeFunc(reshape)
    glutDisplayFunc(draw)
    glutTimerFunc(0, timer, 0)
    glutIdleFunc(idle)
    glutIgnoreKeyRepeat(1)  # ignore key repeat

    initGL(1244, 700)
    glutMainLoop()

if __name__ == "__main__":
    main()
