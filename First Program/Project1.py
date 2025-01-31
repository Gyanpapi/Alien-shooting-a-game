from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
from math import sin,cos
import sys
from math import sin,cos
scene = 0
flag2 = 0
flag3 = 0
bg_color=0
i = 0
j = 0
h = 0
Bombed = 0
explodeTx = 0
explodeTy = 0
expFactor = 1
scene = 0
x = 0
y = -195
opt = 0
clouds = 0

wx1 = [-670, -150, 418]
wy1 = -232

cx = [-540, -150, 520, -30, -540, -150, 520, -30]
cy = [210, 130, 250, 250, -210, -130, -250, -250]

i = -245
j = 400

Bombed = 0
flag2 = 0
h = 0
flag3 = 0

expFactor = 0.0
explodeTx = 1.0
explodeTy = 1.0

import math

pi = math.pi
# Window size
width, height = 400, 600  # 2:3 ratio

# diamond position
diamond_x, diamond_y = 0, 0

# catcher position
catcher_x, catcher_y = 0, 0

# catcher size
catcher_width = 60

# Score
score = 0

# Game state
game_over = False
game_paused = False

# Button states
button_states = [False, False, False]  # Restart, Pause, Quit

# diamond speed
diamond_speed = 10

# catcher speed
catcher_speed = 25


colors = (1.0, 1.0, 1.0)  # initial color

def stars():
    glPointSize( 10 );
    glVertex2f(100,100)
    glPointSize( 2.5 );
    glBegin(GL_POINTS);
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(0.8, 0.95);
    glVertex2f(0.9, 0.9);
    glVertex2f(0.95, 0.7);
    glVertex2f(0.8, 0.8);
    glVertex2f(0.7, 0.9);
    glVertex2f(0.6, 0.8);
    glVertex2f(0.5, 0.75);
    glVertex2f(0.4, 0.9);
    glVertex2f(0.3, 0.7);
    glVertex2f(0.25, 0.9);
    glVertex2f(0.25, 0.7);
    glVertex2f(0.1, 0.9);
    glVertex2f(0.15, 0.75);
    glVertex2f(0.0, 0.8);
    glVertex2f(-0.7, 0.9);
    glVertex2f(1, 0.95);
    glVertex2f(2, 0.8);
    glVertex2f(3, 0.95);
    glVertex2f(4, 0.9);
    glVertex2f(5, 0.7);
    glVertex2f(-0.8, 0.8);
    glVertex2f(-0.7, 0.9);
    glVertex2f(-0.6, 0.8);
    glVertex2f(-0.5, 0.75);
    glVertex2f(-0.4, 0.9);
    glVertex2f(-0.3, 0.7);
    glVertex2f(-0.25, 0.9);
    glVertex2f(-0.25, 0.7);
    glVertex2f(-0.15, 0.75);
    glVertex2f(-0.1, 0.9);
    glEnd();


# ... Midpoint line algo code...

def draw(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    
    glVertex2f(x, y)
    glEnd()


def find_current_zone(dx, dy):

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


def original_zone(x, y, zone):
    
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


def Mid_Point_Line(x1, y1, x2, y2):       # Mid Point Line algorithm
    dx = x2 - x1
    dy = y2 - y1
    zone = find_current_zone(dx, dy)

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

        a, b = original_zone(a, b, zone)
        draw(a, b)
        if D <= 0:
            D = D + dE
            d += [D]
            x = x + 1
        else:
            x = x + 1
            y = y + 1
            D = D + dNE

# end of midpoint line algo code


def draw_button(x1, y1,x2,y2, color):
    glColor3f(*color)
    Mid_Point_Line(x1 ,y1, x2, y2)

  
 
def draw_buttons():
    global game_paused
    colors = [(0, 1, 1), (1, 0.75, 0), (1, 0, 0)]  # Teal, Amber, Red 

#    draw_button(10, height - 60,60,height-60, colors[0])  #left one button
    draw_button(20, height - 40,70,height-40, colors[0])  
    draw_button(20, height - 40, 45,height-60,colors[0])
    draw_button(20, height - 40, 45,height-60,colors[0])
    draw_button(45, height - 60, 20,height-40,colors[0])
    draw_button(45, height - 60, 20,height-40,colors[0])
    
    draw_button(20, height - 40, 45,height-20,colors[0])
    draw_button(20, height - 40, 45,height-20,colors[0])
    draw_button(45, height - 20, 20,height-40,colors[0])
    draw_button(45, height - 20, 20,height-40,colors[0])
    
    
    if(game_paused==False):                                      # middle one button
        draw_button(185,height-20,185,height -60,colors[1] )
        draw_button(210,height-20,210,height -60,colors[1] )
    else:
        draw_button(190,height-20,190,height -60,colors[1] )
        draw_button(190,height-20,210,height -40,colors[1] )
        draw_button(190,height-60,210,height -40,colors[1] )
        
    
#    draw_button(340, height - 60, 390,height-60,colors[2])    #right one button
    draw_button(340, height - 20, 380,height-60,colors[2])
    draw_button(380, height - 60, 340,height-20,colors[2])
    draw_button(380, height - 20, 340,height-60,colors[2])
    draw_button(340, height - 60, 380,height-20,colors[2])

def draw_diamond():
    global colors
    glColor3f(*colors)
    Mid_Point_Line(diamond_x, diamond_y, diamond_x+8, diamond_y+12)
    Mid_Point_Line(diamond_x+8, diamond_y+12, diamond_x+16, diamond_y)
    Mid_Point_Line(diamond_x+8, diamond_y-12, diamond_x, diamond_y)
    Mid_Point_Line(diamond_x+16, diamond_y, diamond_x+8, diamond_y-12)

    
def draw_catcher():
    if(game_over==False):
        
        glColor3f(1.0, 1.0, 1.0)
        Mid_Point_Line(catcher_x, 25, catcher_x+10, 10)
        Mid_Point_Line(catcher_x+100,25,catcher_x+90,10)
        Mid_Point_Line(catcher_x,25,catcher_x+100,25)
        Mid_Point_Line(catcher_x+10,10,catcher_x+90,10)
    else:
        glColor3f(1.0, 0.0, 0.0)
        Mid_Point_Line(catcher_x, 25, catcher_x+10, 10)
        Mid_Point_Line(catcher_x+100,25,catcher_x+90,10)
        Mid_Point_Line(catcher_x,25,catcher_x+100,25)
        Mid_Point_Line(catcher_x+10,10,catcher_x+90,10)
    
 
def drawAxes():
    glLineWidth(1)
   
   
    glVertex2f(100, 0.95)
    glVertex2f(500,300)


    glEnd()
    
def display():
    global score
    glClearColor(bg_color, bg_color, bg_color, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    drawAxes()
    #stars()
  #  draw_buttons()
    explode()
    if game_over:
        print("GAME OVER !! SCORE :",score)
    if game_over==True:
        draw_catcher()
    else:
        draw_diamond()
        draw_catcher()
    glutSwapBuffers()


def specialKeyListener(key, x, y):
    global catcher_x, game_over, game_paused
    if key == GLUT_KEY_LEFT and game_over==False and game_paused==False:  # left arrow key
        catcher_x = max(0, catcher_x - catcher_speed)
    elif key == GLUT_KEY_RIGHT and game_over==False and game_paused==False:  # right arrow key
        catcher_x = min(width - 100, catcher_x + catcher_speed)
    else:
        pass
    glutPostRedisplay()

def mouse(button, state, x, y):
    global game_over, game_paused,height,catcher_speed,diamond_speed
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 20<=x <= 70 and y<=(height-540):  # Restart button
            catcher_speed=25
            diamond_speed=10
            reset_game()
            print("Starting over")

        elif 170 <= x <= 225 and y<=(height-540) and game_over==False:  # Pause button
            game_paused = not game_paused
        elif 340 <= x <= 380 and y<=(height-540):  # Quit button
            print("Goodbye")
            print("Score: ", score)
            glutLeaveMainLoop()
        else:
            pass


expFactor = 0
class RgbColor:
    def __init__(self, red, green, blue, alpha):
        self.red = red / 256
        self.green = green / 256
        self.blue = blue / 256
        self.alpha = alpha

def createColor(red, green, blue, alpha):
    return RgbColor(red, green, blue, alpha)
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
    for c in range(8):
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
def explode():
    color = createColor(237, 105, 74, 0)
    glColor3f(color.red, color.green, color.blue)
    Circle(-25, -130, 0, 1.0 * expFactor, 200)

    color = createColor(216, 85, 58, 0)
    glColor3f(color.red, color.green, color.blue)
    Circle(-5, -135, 0, 1.0 * expFactor, 200)
    
def timer(v):
    global diamond_x,diamond_y, score, game_over,diamond_speed,catcher_speed,catcher_x,catcher_y
    if not game_paused:
        diamond_y -= diamond_speed
        if diamond_y < 0:
            if diamond_x+16 >= catcher_x and diamond_x <= catcher_x + 100:    # +16 for diamond width and +100 for catcher width
                score += 1
                diamond_speed=min(diamond_speed+1,60)  # increasing diamond speed #min function to avoid too much speed
                catcher_speed=min(catcher_speed+2,100) #increasing catcher speed  # min func to avoid too much speed
               # print("diamond speed: ",diamond_speed," ","catcher speed: ",catcher_speed) # printing the speed to see if incre or not
                print("Score: ",score)
                reset_diamond()
            else:
                game_over = True
    glutPostRedisplay()
    if not game_over:
        glutTimerFunc(100, timer, 0)
        

def reset_diamond():
    global diamond_x, diamond_y,colors
    diamond_x = random.randint(0, width-16)
    diamond_y = height-65
    a=random.random() # Choose a random color
    b=random.random() # Choose a random color
    c=random.random() # Choose a random color
    if(a<0.5 and b<0.5 and c<0.5):    # to avoid a color that is similar to the background 
        b=1.5       
    colors = (a,b,c) 

def reset_game():
    global score, game_over, game_paused
    score = 0
    game_over = False
    game_paused = False
    reset_diamond()
    glutTimerFunc(100, timer, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Diamond Game")
    glutDisplayFunc(display)
    gluOrtho2D(0, 400, 0, 600)
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouse)
    reset_game()
    glutMainLoop()

if __name__ == "__main__":
    main()
