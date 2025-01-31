from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin
import random

# Window size
width, height = 600, 650

# Egg position
egg_x, egg_y = 0, 0

# Basket position
basket_x, basket_y = 0, 0

# Score
score = 0

# Game state
game_over = False

def draw_text(x, y, text):
    glColor3f(1, 1, 1)  # White color
    glWindowPos2f(x, y)  # Position
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(ch))

def draw_egg():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    for i in range(100):
        glVertex2f(egg_x + 10 * cos(i/50.0 * 3.1415), egg_y + 20 * sin(i/50.0 * 3.1415))
    glEnd()

def draw_basket():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(basket_x, 30)
    glVertex2f(basket_x + 10, 10)
    glVertex2f(basket_x + 50, 10)
    glVertex2f(basket_x + 60, 30)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    if game_over:
        draw_text(width / 2, height / 2, "GAME OVER")
    else:
        draw_egg()
        draw_basket()
        draw_text(10, height - 20, "Score: " + str(score))
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, 0, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def keyboard(key, x, y):
    global basket_x, game_over
    if key == b'a':
        basket_x -= 10
    elif key == b'd':
        basket_x += 10
    elif key == b'r' and game_over:
        reset_game()
    glutPostRedisplay()

def timer(v):
    global egg_y, score, game_over
    egg_y -= 10
    if egg_y < 0:
        if egg_x >= basket_x and egg_x <= basket_x + 60:
            score += 1
            reset_egg()
        else:
            game_over = True
    glutPostRedisplay()
    if not game_over:
        glutTimerFunc(100, timer, 0)

def reset_egg():
    global egg_x, egg_y
    egg_x = random.randint(0, width)
    egg_y = height

def reset_game():
    global score, game_over
    score = 0
    game_over = False
    reset_egg()
    glutTimerFunc(100, timer, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Egg Game")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    reset_game()
    glutMainLoop()

if __name__ == "__main__":
    main()
