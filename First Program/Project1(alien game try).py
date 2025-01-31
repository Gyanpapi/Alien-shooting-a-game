from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

XMAX = 1200
YMAX = 700
SPACESHIP_SPEED = 20
TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3

m_viewport = [0, 0, 0, 0]
mButtonPressed = False
mouseX, mouseY = 0.0, 0.0
viewPage = 1  # Placeholder for view enum, replace with appropriate values
keyStates = [False] * 256
direction = [False] * 4
laser1Dir = [False] * 2
laser2Dir = [False] * 2

alienLife1 = 100
alienLife2 = 100
gameOver = False
xOne, yOne = 500, 0
xTwo, yTwo = 500, 0
laser1=False
laser2=False
CI = 0
a = [[0, -50], [70, -50], [70, 70], [-70, 70]]
LightColor = [[1, 1, 0], [0, 1, 1], [0, 1, 0]]
AlienBody = [[-4, 9], [-6, 0], [0, 0], [0.5, 9], [0.15, 12], [-14, 18], [-19, 10], [-20, 0], [-6, 0]]
AlienCollar = [[-9, 10.5], [-6, 11], [-5, 12], [6, 18], [10, 20], [13, 23], [16, 30], [19, 39], [16, 38],
               [10, 37], [-13, 39], [-18, 41], [-20, 43], [-20.5, 42], [-21, 30], [-19.5, 23], [-19, 20],
               [-14, 16], [-15, 17], [-13, 13], [-9, 10.5]]
ALienFace = [[-6, 11], [-4.5, 18], [0.5, 20], [0., 20.5], [0.1, 19.5], [1.8, 19], [5, 20], [7, 23], [9, 29],
             [6, 29.5], [5, 28], [7, 30], [10, 38], [11, 38], [11, 40], [11.5, 48], [10, 50.5], [8.5, 51], [6, 52],
             [1, 51], [-3, 50], [-1, 51], [-3, 52], [-5, 52.5], [-6, 52], [-9, 51], [-10.5, 50], [-12, 49], [-12.5, 47],
             [-12, 43], [-13, 40], [-12, 38.5], [-13.5, 33], [-15, 38], [-14.5, 32], [-14, 28], [-13.5, 33], [-14, 28],
             [-13.8, 24], [-13, 20], [-11, 19], [-10.5, 12], [-6, 11]]
ALienBeak = [[-6, 21.5], [-6.5, 22], [-9, 21], [-11, 20.5], [-20, 20], [-14, 23], [-9.5, 28], [-7, 27], [-6, 26.5],
             [-4.5, 23], [-4, 21], [-6, 19.5], [-8.5, 19], [-10, 19.5], [-11, 20.5]]


def displayRasterText(x, y, z, stringToDisplay):
    glRasterPos3f(x, y, z)
    for c in stringToDisplay:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))


def init():
    glClearColor(0.0, 0.0, 0.0, 0)
    glColor3f(1.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1200, 1200, -700, 700)
    glMatrixMode(GL_MODELVIEW)


def introScreen():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    displayRasterText(-425, 490, 0.0, "NMAM INSTITUTE OF TECHNOLOGY")
    glColor3f(1.0, 1.0, 1.0)
    displayRasterText(-700, 385, 0.0, "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING")
    glColor3f(0.0, 0.0, 1.0)
    displayRasterText(-225, 300, 0.0, "A MINI PROJECT ON ")
    glColor3f(1.0, 0.0, 1.0)
    displayRasterText(-125, 225, 0.0, "Space Shooter")
    glColor3f(1.0, 0.7, 0.8)
    displayRasterText(-100, 150, 0.0, "created by")
    glColor3f(1.0, 1.0, 1.0)
    displayRasterText(-130, 80, 0.0, "SHOOTERS")
    glColor3f(1.0, 0.0, 0.0)
    displayRasterText(-800, -100, 0.0, " STUDENT NAMES")
    glColor3f(1.0, 1.0, 1.0)
    displayRasterText(-800, -200, 0.0, " Saurav N Shetty")
    displayRasterText(-800, -285, 0.0, " Rajath R Pai")
    glColor3f(1.0, 0.0, 0.0)
    displayRasterText(500, -100, 0.0, "Under the Guidance of")
    glColor3f(1.0, 1.0, 1.0)
    displayRasterText(500, -200, 0.0, "Prof X")
    glColor3f(1.0, 0.0, 0.0)
    displayRasterText(-250, -400, 0.0, "Academic Year 2020-2021")
    glColor3f(1.0, 1.0, 1.0)
    displayRasterText(-300, -550, 0.0, "Press ENTER to start the game")
    glFlush()
    glutSwapBuffers()

def startScreenDisplay():
    glLineWidth(10)
    glColor3f(1,0,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-750 ,-500)
    glVertex2f(-750 ,550)
    glVertex2f(750 ,550)
    glVertex2f(750 ,-500)
    glEnd()

    glLineWidth(1)

    glColor3f(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2f(-200 ,300)
    glVertex2f(-200 ,400)
    glVertex2f(200 ,400)
    glVertex2f(200 ,300)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-200, 50)
    glVertex2f(-200 ,150)
    glVertex2f(200 ,150)
    glVertex2f(200 ,50)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-200 ,-200)
    glVertex2f(-200 ,-100)
    glVertex2f(200, -100)
    glVertex2f(200, -200)
    glEnd()

    if mouseX>=-100 and mouseX<=100 and mouseY>=150 and mouseY<=200:
        glColor3f(0 ,0 ,1)
        if mButtonPressed:
            alienLife1 = alienLife2 = 100
            viewPage = 3
            mButtonPressed = False
    else:
        glColor3f(0 , 0, 0)

    displayRasterText(-100 ,340 ,0.4 ,"Start Game")

    if mouseX>=-100 and mouseX<=100 and mouseY>=30 and mouseY<=80:
        glColor3f(0 ,0 ,1)
        if mButtonPressed:
            viewPage = 2
            mButtonPressed = False
    else:
        glColor3f(0 , 0, 0)
    displayRasterText(-120 ,80 ,0.4 ,"Instructions")

    if mouseX>=-100 and mouseX<=100 and mouseY>=-90 and mouseY<=-40:
        glColor3f(0 ,0 ,1)
        if mButtonPressed:
            mButtonPressed = False
            exit(0)
    else:
        glColor3f(0 , 0, 0)
    displayRasterText(-100 ,-170 ,0.4 ,"    Quit")
    glutPostRedisplay()

def backButton():
    if mouseX <= -450 and mouseX >= -500 and mouseY >= -275 and mouseY <= -250:
        glColor3f(0, 0, 1)
        if mButtonPressed:
            viewPage = 1
            mButtonPressed = False
            glutPostRedisplay()
    else:
        glColor3f(1, 0, 0)
    displayRasterText(-1000 ,-550 ,0, "Back")
    
def instructionsScreenDisplay():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1, 0, 0)
    displayRasterText(-900 ,550 ,0.4 ,"INSTRUCTIONS")
    glColor3f(1, 0, 0)
    displayRasterText(-1000 ,400 ,0.4 ,"PLAYER 1")
    displayRasterText(200 ,400 ,0.4 ,"PLAYER 2")
    glColor3f(1, 1, 1)
    displayRasterText(-1100 ,300 ,0.4 ,"Key 'w' to move up.")
    displayRasterText(-1100 ,200 ,0.4 ,"Key 's' to move down.")
    displayRasterText(-1100 ,100 ,0.4 ,"Key 'd' to move right.")
    displayRasterText(-1100 ,0 ,0.4 ,"Key 'a' to move left.")
    displayRasterText(100 ,300 ,0.4 ,"Key 'i' to move up.")
    displayRasterText(100 ,200 ,0.4 ,"Key 'k' to move down.")
    displayRasterText(100 ,100 ,0.4 ,"Key 'j' to move right.")
    displayRasterText(100 ,0 ,0.4 ,"Key 'l' to move left.")
    displayRasterText(-1100 ,-100 ,0.4 ,"Key 'c' to shoot, Use 'w' and 's' to change direction.")
    displayRasterText(100 ,-100 ,0.4 ,"Key 'm' to shoot, Use 'i' and 'k' to change direction.")
    displayRasterText(-1100, -300,0.4,"The Objective is to kill your opponent.")
    displayRasterText(-1100 ,-370 ,0.4 ,"Each time a player gets shot, LIFE decreases by 5 points.")
    backButton()

def DrawAlienBody(isPlayer1):
    if isPlayer1:
        glColor3f(0,1,0)
    else:
        glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    for i in range(9):
        glVertex2fv(AlienBody[i])
    glEnd()

    glColor3f(0,0,0)
    glLineWidth(1)
    glBegin(GL_LINE_STRIP)
    for i in range(9):
        glVertex2fv(AlienBody[i])
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-13,11)
    glVertex2f(-15,9)
    glEnd()

def DrawAlienCollar():
    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    for i in range(21):
        glVertex2fv(AlienCollar[i])
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_LINE_STRIP)
    for i in range(21):
        glVertex2fv(AlienCollar[i])
    glEnd()

def DrawAlienFace(isPlayer1):
    glColor3f(0,0,1)
    glBegin(GL_POLYGON)
    for i in range(43):
        glVertex2fv(ALienFace[i])
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_LINE_STRIP)
    for i in range(43):
        glVertex2fv(ALienFace[i])
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex2f(3.3,22)
    glVertex2f(4.4,23.5)
    glVertex2f(6.3,26)
    glEnd()

def DrawAlienBeak():
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    for i in range(15):
        glVertex2fv(ALienBeak[i])
    glEnd()

    glColor3f(0,0,0)
    glBegin(GL_LINE_STRIP)
    for i in range(15):
        glVertex2fv(ALienBeak[i])
    glEnd()

def DrawAlienEyes(isPlayer1):
    glColor3f(0,1,1)
    glPushMatrix()
    glRotated(-10,0,0,1)
    glTranslated(-6,32.5,0)
    glScalef(2.5,4,0)
    glutSolidSphere(1,20,30)
    glPopMatrix()

    glPushMatrix()
    glRotated(-1,0,0,1)
    glTranslated(-8,36,0)
    glScalef(2.5,4,0)
    glutSolidSphere(1,100,100)
    glPopMatrix()

def DrawAlien(isPlayer1):
    DrawAlienBody(isPlayer1)
    DrawAlienCollar()
    DrawAlienFace(isPlayer1)
    DrawAlienBeak()
    DrawAlienEyes(isPlayer1)




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

def DrawSteeringWheel():
    glPushMatrix()
    glLineWidth(3)
    glColor3f(0.20,0.,0.20)
    glScalef(7,4,1)
    glTranslated(-1.9,5.5,0)
    glutWireSphere(1,8,8)
    glPopMatrix()

def DrawSpaceshipDoom():
    glColor4f(0.7,1,1,0.0011)
    glPushMatrix()
    glTranslated(0,30,0)
    glScalef(35,50,1)
    glutSolidSphere(1,50,50)
    glPopMatrix()

def DrawLaser(x, y, dir):
    xend = -XMAX
    yend = y
    if dir[0]:
        yend = YMAX
    elif dir[1]:
        yend = -YMAX
    glLineWidth(5)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(xend, yend)
    glEnd()

def SpaceshipCreate(x, y, isPlayer1):
    glPushMatrix()
    glTranslated(x,y,0)
    DrawSpaceshipDoom()
    glPushMatrix()
    glTranslated(4,19,0)
    DrawAlien(isPlayer1)
    glPopMatrix()
    DrawSteeringWheel()
    DrawSpaceshipBody(isPlayer1)
    glEnd()
    glPopMatrix()

def DisplayHealthBar1():
    temp1 = "  LIFE = %d" % alienLife1
    glColor3f(1 ,1 ,1)
    displayRasterText(-1100 ,600 ,0.4 ,temp1)
    glColor3f(1 ,0 ,0)

def DisplayHealthBar2():
    temp2 = "  LIFE = %d" % alienLife2
    glColor3f(1 ,1 ,1)
    displayRasterText(800 ,600 ,0.4 ,temp2)
    glColor3f(1 ,0 ,0)

def checkLaserContact(x, y, dir, xp, yp, player1):
    xend = -XMAX
    yend = y
    xp += 8
    yp += 8
    if dir[0]:
        yend = YMAX
    elif dir[1]:
        yend = -YMAX
    m = (float)(yend - y) / (float)(xend - x)
    k = y - m * x
    r = 50
    b = 2 * xp - 2 * m * (k - yp)
    a = 1 + m * m
    c = xp * xp + (k - yp) * (k - yp) - r * r
    d = (b * b - 4 * a * c)
    print("\nDisc: %f x: %d, y: %d, xp: %d, yp: %d" % (d, x, y, xp, yp))
    if d >= 0:
        if player1:
            alienLife1 -= 5
        else:
            alienLife2 -= 5
        print("%d %d\n" % (alienLife1, alienLife2))

def gameScreenDisplay():
   # DisplayHealthBar1()
  #  DisplayHealthBar2()
    glScalef(2, 2, 0)

    if alienLife1 > 0:
        SpaceshipCreate(xOne, yOne, True)

    if alienLife2 > 0:
        SpaceshipCreate(xTwo, yTwo, False)

    if laser1:
        DrawLaser(xOne, yOne, True)

    if laser2:
        DrawLaser(xTwo, yTwo, False)

def displayGameOverMessage():
    glColor3f(1, 1, 0)
    if alienLife1 > 0:
        message = "Game Over! Player 1 won the game"
    else:
        message = "Game Over! Player 2 won the game"
    displayRasterText(-350 ,600 ,0.4 , message)

def keyOperations():
    global viewPage, laser1Dir, laser2Dir, laser2, xTwo, yTwo, laser1, xOne, yOne
    if keyStates[13] == True and viewPage == 0:
        viewPage = 1
        print("view value changed to %d" % viewPage)
        print("enter key pressed\n")
    if viewPage == 3:
        laser1Dir[0] = laser1Dir[1] = False
        laser2Dir[0] = laser2Dir[1] = False
        if keyStates['c'] == True:
            laser2 = True
            if keyStates['w'] == True:
                laser2Dir[0] = True
            if keyStates['s'] == True:
                laser2Dir[1] = True
        else:
            laser2 = False
            if keyStates['d'] == True:
                xTwo -= SPACESHIP_SPEED
            if keyStates['a'] == True:
                xTwo += SPACESHIP_SPEED
            if keyStates['w'] == True:
                yTwo += SPACESHIP_SPEED
            if keyStates['s'] == True:
                yTwo -= SPACESHIP_SPEED

        if keyStates['m'] == True:
            laser1 = True
            if keyStates['i'] == True:
                laser1Dir[0] = True
            if keyStates['k'] == True:
                laser1Dir[1] = True
        else:
            laser1 = False
            if keyStates['l'] == True:
                xOne += SPACESHIP_SPEED
            if keyStates['j'] == True:
                xOne -= SPACESHIP_SPEED
            if keyStates['i'] == True:
                yOne += SPACESHIP_SPEED
            if keyStates['k'] == True:
                yOne -= SPACESHIP_SPEED
def display():
    #keyOperations()
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    if viewPage == 0:
        introScreen()
        
    elif viewPage == 1:
        DrawAlien(True)
        DrawSpaceshipDoom()
   #     SpaceshipCreate(1,2,True)
        DrawAlien(True)
        DrawSpaceshipBody(True)
        DrawSteeringWheel()
      
        
        
     #   startScreenDisplay()
    elif viewPage == 2:
        instructionsScreenDisplay()
    elif viewPage == 3:
        gameScreenDisplay()
    elif viewPage == 4:
        displayGameOverMessage()
        startScreenDisplay()
    glFlush()
    glLoadIdentity()
    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1200, 1200, -700, 700)
    glMatrixMode(GL_MODELVIEW)
    m_viewport[2] = w
    m_viewport[3] = h


def keyboard(key, x, y):
    if key == b'\033':
        sys.exit()


def keyup(key, x, y):
    keyStates[ord(key)] = False


def keyPressed(key, x, y):
    keyStates[ord(key)] = True
    if keyStates[ord('q')]:
        sys.exit()
    if keyStates[ord('1')]:
        viewPage = 1
    if keyStates[ord('2')]:
        viewPage = 2
    if keyStates[ord('3')]:
        viewPage = 3


def mouse(button, state, x, y):
    global mButtonPressed, mouseX, mouseY
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        mButtonPressed = True
        mouseX = x
        mouseY = y
    elif button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        mButtonPressed = False


def motion(x, y):
    global mouseX, mouseY
    if mButtonPressed:
        deltaX = x - mouseX
        deltaY = y - mouseY
        mouseX = x
        mouseY = y

        if viewPage == 1:
            # ... (rest of the code remains unchanged)
            pass
        elif viewPage == 3:
            if direction[TOP]:
                yOne += deltaY
            if direction[BOTTOM]:
                yOne += deltaY
            if direction[RIGHT]:
                xOne += deltaX
            if direction[LEFT]:
                xOne += deltaX

            if direction[TOP]:
                yTwo += deltaY
            if direction[BOTTOM]:
                yTwo += deltaY
            if direction[RIGHT]:
                xTwo += deltaX
            if direction[LEFT]:
                xTwo += deltaX

    glutPostRedisplay()


def idle():
    global laser1,laser2
    if not gameOver:
        if laser1:
            if laser1Dir[TOP]:
                yOne += SPACESHIP_SPEED
            if laser1Dir[BOTTOM]:
                yOne -= SPACESHIP_SPEED
            if laser1Dir[RIGHT]:
                xOne += SPACESHIP_SPEED
            if laser1Dir[LEFT]:
                xOne -= SPACESHIP_SPEED

            if xOne > XMAX or xOne < -XMAX or yOne > YMAX or yOne < -YMAX:
                laser1 = False

        if laser2:
            if laser2Dir[TOP]:
                yTwo += SPACESHIP_SPEED
            if laser2Dir[BOTTOM]:
                yTwo -= SPACESHIP_SPEED
            if laser2Dir[RIGHT]:
                xTwo += SPACESHIP_SPEED
            if laser2Dir[LEFT]:
                xTwo -= SPACESHIP_SPEED

            if xTwo > XMAX or xTwo < -XMAX or yTwo > YMAX or yTwo < -YMAX:
                laser2 = False

    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(XMAX, YMAX)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Space Invaders")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyup)
    glutSpecialFunc(keyPressed)
    glutSpecialUpFunc(keyup)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutIdleFunc(idle)
    glutMainLoop()


if __name__ == "__main__":
    main()
