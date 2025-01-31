from OpenGL.GL import *
from OpenGL.GLUT import *
import math
import random

Width = 500
Height = 500
seasons = ['summer','winter','monsoon','spring']
current_season=0
speed=1
raindrops=[]
mouse_x = -1

#Mid Point Line Algorithm

def mpla(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = current_zone(dx, dy)

    x1, y1, x2, y2 =convert_to_zone_zero(x1, y1, x2, y2, zone)
    x_new = []
    y_new = []
    d = []

    dx = x2 - x1
    dy = y2 - y1
    D = 2 * dy - dx

    d += [D]
    dNE = 2 * (dy - dx)
    dE = 2 * dy

    x = x1
    y = y1
    while x <= x2:
        a = x
        b = y
        x_new += [x]
        y_new += [y]

        a, b = back_to_original(a, b, zone)
        draw(a, b)
        if D <= 0:
            D = D + dE
            d += [D]
            x = x + 1
        else:
            x = x + 1
            y = y + 1
            D = D + dNE

def current_zone(dx, dy):

    if dx>=0 and dy>=0:
        if abs(dx)>=abs(dy):
            return 0
        else:
            return 1
    if dx<=0 and dy>=0:
        if abs(dx)>=abs(dy):
            return 3
        else:
            return 2
    if dx<=0 and dy<=0:
        if abs(dx)>=abs(dy):
            return 4
        else:
            return 5
    if dx>=0 and dy<=0:
        if abs(dx)>=abs(dy):
            return 7
        else:
            return 6

def convert_to_zone_zero(x1, y1, x2, y2, zone):
    if zone == 0:
        return x1, y1, x2, y2
    elif zone == 1:
        return y1, x1, y2, x2
    elif zone == 2:
        return y1, -x1, y2, -x2
    elif zone == 3:
        return -x1, y1, -x2, y2
    elif zone == 4:
        return -x1, -y1, -x2, -y2
    elif zone == 5:
        return -y1, -x1, -y2, -x2
    elif zone == 6:
        return -y1, x1, -y2, x2
    elif zone == 7:
        return x1, -y1, x2, -y2
    return x1,y1,x2,y2


def back_to_original(x, y, zone):
    if zone == 0:       
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y
    
def draw(x, y):
    glVertex2f(x, y)

#Mid Point Circle Algorthm

def mpca(xn, yn, r):
    d = 1 - r
    x = 0
    y = r
    circle_points(x, y, xn, yn)
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * x - 2 * y + 5
            y = y - 1
        x = x + 1
        circle_points(x, y, xn, yn)

def circle_points(x, y, xn, yn):
    glVertex2f(x + xn, y + yn)
    glVertex2f(-x + xn, -y + yn)
    glVertex2f(y + xn, x + yn)
    glVertex2f(-y + xn, -x + yn)
    glVertex2f(x + xn, -y + yn)
    glVertex2f(-x + xn, y + yn)
    glVertex2f(-y + xn, x + yn)
    glVertex2f(y + xn, -x + yn)

#Drawing Objects

def draw_flowers():
    if seasons[current_season]=='spring':
        x=10
        while x<210:
            glColor3f(.72, .45, 0.2)
            mpla(x,100,x,110)
            glColor3f(1, 0, 1)
            mpca(x,116,1)
            glColor3f(1, 1, 0)
            mpca(x-2,114,1)
            glColor3f(1, 0, 0)
            mpca(x+2,114,2)
            x=x+13
        x=250
        while x<290:
            glColor3f(.72, .45, 0.2)
            mpla(x,100,x,110)
            glColor3f(1, 0, 1)
            mpca(x,116,1)
            glColor3f(1, 1, 0)
            mpca(x-2,114,1)
            glColor3f(1, 0, 0)
            mpca(x+2,114,2)
            x=x+13
        x=430
        while x<490:
            glColor3f(.72, .45, 0.2)
            mpla(x,100,x,110)
            glColor3f(1, 0, 1)
            mpca(x,116,1)
            glColor3f(1, 1, 0)
            mpca(x-2,114,1)
            glColor3f(1, 0, 0)
            mpca(x+2,114,2)
            x=x+13

def draw_lines():
    glColor3f(.63, .16, 0.16)
    y=100
    for i in range(y):
      mpla(0,y-i,500,y-i)    

def draw_house():
    glColor3f(1.0, 1.0, 0.0)
    mpla(300,101,420,101)
    mpla(300,100,300,140)
    mpla(350,100,350,140)
    mpla(350,100,350,140)
    mpla(295,140,355,140)
    mpla(295,140,325,165)
    mpla(325,165,355,140)
    mpla(355,140,425,140)
    mpla(325,165,390,165)
    mpla(390,165,425,140)
    mpla(420,140,420,100)
    mpla(315,122,315,100)
    mpla(335,122,335,100)
    mpla(315,122,335,122)
    mpla(325,122,325,100)
    mpla(370,127,400,127)
    mpla(370,110,400,110)
    mpla(370,127,370,110)
    mpla(400,127,400,110)
    mpla(385,127,385,110)
    mpla(370,118,400,118)

def draw_tree():
    glColor3f(.72, .45, 0.2)
    x=220
    for i in range(20):
      mpla(x+i,100,x+i,150)
    glColor3f(.1, .9, 0.1)
    mpca(213,140,7)
    mpca(213,140+14,7)
    mpca(213,140+28,7)
    mpca(213,140+28+14,7)
    mpca(247,140,7)
    mpca(247,140+14,7)
    mpca(247,140+28,7)
    mpca(247,140+28+14,7)
    mpca(230,160,8)
    mpca(230,160+14,8)
    mpca(230,160+28,8)
    mpca(260,147,7)
    mpca(260,147+14,7)
    mpca(260,147+28,7)
    mpca(200,147,7)
    mpca(200,147+14,7)
    mpca(200,147+28,7)
    mpca(268,154,7)
    mpca(268,154+14,7)
    mpca(193,154,7)
    mpca(193,154+14,7)

def draw_sun():
    global mouse_x, seasons
    if mouse_x != -1 and mouse_x < 455 and mouse_x > 45 and seasons[current_season]=='summer' or seasons[current_season]=='spring':
        glColor3f(1.0, 0.0, 0.0)  # Red color
        mpca(mouse_x, 420, 30)
        mpla(mouse_x+35,420,mouse_x+60,420)
        mpla(mouse_x-35,420,mouse_x-60,420)
        mpla(mouse_x,420+35,mouse_x,420+60)
        mpla(mouse_x,420-35,mouse_x,420-60)
        mpla(mouse_x + 25, 420 + 25, mouse_x + 45, 420 + 45)
        mpla(mouse_x - 25, 420 - 25, mouse_x - 45, 420 - 45)
        mpla(mouse_x + 25, 420 - 25, mouse_x + 45, 420 - 45)
        mpla(mouse_x - 25, 420 + 25, mouse_x - 45, 420 + 45)

#Animation

def animation():
    global speed,seasons,current_season
    if seasons[current_season]=='monsoon':
        glColor3f(0.2, 0.6, 0.8)
        for _ in range(50): #snowfall
            x1 = random.randint(0, Width)
            y1 = random.randint(0, Height)
            x2 = x1 + 5
            y2 = y1 + 10
            mpla(x1, y1, x2, y2)
    elif seasons[current_season]=='winter':
        glColor3f(1, 1, 1)
        for _ in range(50): #snowfall
            x = random.randint(0, Width)
            y = random.randint(0, Height) + speed
            glVertex2f(x, y)
    else:
        pass
    glutPostRedisplay()
    
#Key assigning

def change_season(direction):
    global current_season
    if direction == GLUT_KEY_RIGHT:
        current_season = (current_season + 1) % len(seasons)
    elif direction == GLUT_KEY_LEFT:
        current_season = (current_season - 1) % len(seasons)
    glutPostRedisplay()

def change_speed(direction):
    global speed
    if direction == GLUT_KEY_UP:
        speed -= 2
    elif direction == GLUT_KEY_DOWN:
        speed += 2

def special_key_func(key, x, y):
    if key in [GLUT_KEY_LEFT, GLUT_KEY_RIGHT]:
        change_season(key)
    elif key in [GLUT_KEY_UP, GLUT_KEY_DOWN]:
        change_speed(key)

def mouse_click(button, state, x, y):
    global mouse_x
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        mouse_x = x
        glutPostRedisplay()

#Displaying and Animation

def iterate():
    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, Width, 0.0, Height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    normalized_mouse_x = mouse_x / Width  # Normalize mouse_x to range [0, 1]
    inverted_normalized_x = 1.0 - normalized_mouse_x  # Invert the value for brightness
    background_color = inverted_normalized_x * 0.5
    glClearColor(background_color, background_color, background_color, 1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    draw_lines()
    draw_flowers()
    draw_house()
    draw_tree()
    draw_sun()
    animation()
    glEnd()
    glutSwapBuffers()

def display():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(Width, Height)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"Mid Point Circle Algorithm")
    glutDisplayFunc(showscreen)
    glutSpecialFunc(special_key_func)
    
    glutMouseFunc(mouse_click)
    glEnable(GL_DEPTH_TEST)
    iterate()
    glutMainLoop()

display()