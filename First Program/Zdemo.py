from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window size
width, height = 400, 600  # 2:3 ratio

# diamond position
diamond_x, diamond_y = 0, 0

# Basket position
basket_x, basket_y = 0, 0

# Basket size
basket_width = 60

# Score
score = 0

# Game state
game_over = False
game_paused = False

# Button states
button_states = [False, False, False]  # Restart, Pause, Quit

# diamond speed
diamond_speed = 10

# Basket speed
basket_speed = 25

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


def Mid_Point_Line(x1, y1, x2, y2):
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
    colors = [(0, 1, 1), (1, 0.75, 0), (1, 0, 0)]  # Teal, Amber, Red 

#    draw_button(10, height - 60,60,height-60, colors[0])  #left one 
    draw_button(20, height - 40,70,height-40, colors[0])  
    draw_button(20, height - 40, 45,height-60,colors[0])
    draw_button(20, height - 40, 45,height-60,colors[0])
    draw_button(45, height - 60, 20,height-40,colors[0])
    draw_button(45, height - 60, 20,height-40,colors[0])
    
    draw_button(20, height - 40, 45,height-20,colors[0])
    draw_button(20, height - 40, 45,height-20,colors[0])
    draw_button(45, height - 20, 20,height-40,colors[0])
    draw_button(45, height - 20, 20,height-40,colors[0])
  
#    draw_button(170, height-60,220,height-60, colors[1])#middle one 
    draw_button(190,height-20,190,height -60,colors[1] )
    draw_button(205,height-20,205,height -60,colors[1] )
    
#    draw_button(340, height - 60, 390,height-60,colors[2]) #right one 
    draw_button(340, height - 20, 380,height-60,colors[2])
    draw_button(380, height - 60, 340,height-20,colors[2])
    draw_button(380, height - 20, 340,height-60,colors[2])
    draw_button(340, height - 60, 380,height-20,colors[2])

def draw_diamond(a,b,c):
    glColor3f(a,b,c)
    Mid_Point_Line(diamond_x, diamond_y, diamond_x+8, diamond_y+12)
    Mid_Point_Line(diamond_x+8, diamond_y+12, diamond_x+16, diamond_y)
    Mid_Point_Line(diamond_x+8, diamond_y-12, diamond_x, diamond_y)
    Mid_Point_Line(diamond_x+16, diamond_y, diamond_x+8, diamond_y-12)

    
def draw_basket():
    glColor3f(1.0, 1.0, 1.0)
    Mid_Point_Line(basket_x, 25, basket_x+10, 10)
    Mid_Point_Line(basket_x+100,25,basket_x+90,10)
    Mid_Point_Line(basket_x,25,basket_x+100,25)
    Mid_Point_Line(basket_x+10,10,basket_x+90,10)
    
    #Mid_Point_Line(basket_x+100,25,basket_x+90,10)
    
  #  Mid_Point_Line(basket_x+50, 10,basket_x+60, 30)

def display():
    global score
    glClear(GL_COLOR_BUFFER_BIT)
    draw_buttons()
    if game_over:
        print("GAME OVER || SCORE :",score)
    else:
        a=random.random()
        b=random.random()
        c=random.random()
        draw_diamond(a,b,c)
        draw_basket()
    
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #.................
def keyboard(key, x, y):
    global basket_x, game_over
    if key == b'a':
        basket_x = max(0, basket_x - basket_speed)  #  left of window
    elif key == b'd':
        basket_x = min(width - 100, basket_x + basket_speed)  #  right of window  
        # width-100 meaning substracting the basket size ,here 100 is the basket size
    elif key == b'r' and game_over:
        reset_game()
    glutPostRedisplay()

def mouse(button, state, x, y):
    global game_over, game_paused,height
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 20<=x <= 70 and y<=(height-540):  # Restart button
            reset_game()
            print("starting over")

        elif 190 <= x <= 205 and y<=(height-540):  # Pause button
            game_paused = not game_paused
        elif 340 <= x <= 380 and y<=(height-540):  # Quit button
            print("Goodbye")
            print("Score: ", score)
            glutLeaveMainLoop()
        else:
            pass
   

def timer(v):
    global diamond_x,diamond_y, score, game_over
    if not game_paused:
        diamond_y -= diamond_speed
        if diamond_y < 0:
            if diamond_x+16 >= basket_x and diamond_x <= basket_x + 100:    # +16 for diamond width and +100 for basket width
                score += 1
                print("Score: ",score)
                reset_diamond()
            else:
                print(diamond_x," ",basket_x)
                game_over = True
    glutPostRedisplay()
    if not game_over:
        glutTimerFunc(100, timer, 0)

def reset_diamond():
    global diamond_x, diamond_y
    diamond_x = random.randint(0, width-10)
    diamond_y = height-65

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
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    reset_game()
    glutMainLoop()

if __name__ == "__main__":
    main()
