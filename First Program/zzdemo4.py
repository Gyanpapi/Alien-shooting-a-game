import sys
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
import math
# Window dimensions
window_width = 800
window_height = 600
stick_x=1

# Ball attributes
ball_radius = 20
ball_x = random.randint(0, window_width - 2 * ball_radius)
ball_y = window_height - ball_radius
ball_speed = 2

# Stick attributes
stick_width = 100
stick_height = 10
stick_x = (window_width - stick_width) // 2
stick_y = 10
stick_speed = 10

# Score
score = 0

# Initialize OpenGL
def init():
    glClearColor(0, 0, 0, 0)
    glOrtho(0, window_width, 0, window_height, -1, 1)

# Display function
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Move the stick using the keyboard
    if glutSpecialFunc:
        keys = glutGetModifiers()
        if keys == GLUT_ACTIVE_SHIFT and stick_x > 0:
            stick_x -= stick_speed
        if keys == GLUT_ACTIVE_CTRL and stick_x < window_width - stick_width:
            stick_x += stick_speed
    
    # Move the ball
    global ball_y,ball_x,stick_x
    ball_y -= ball_speed
    
    # Check if the ball hits the stick
    if (ball_y - ball_radius <= stick_y + stick_height) and \
       (ball_x >= stick_x) and (ball_x <= stick_x + stick_width):
        global score
        score += 1
        ball_x = random.randint(0, window_width - 2 * ball_radius)
        ball_y = window_height - ball_radius
    
    # Check if the ball hits the bottom
    if ball_y - ball_radius <= 0:
        game_over()
    
    # Draw the ball
    glColor3f(1, 1, 1)
    glBegin(GL_TRIANGLE_FAN)
    for angle in range(0, 360, 10):
        x = ball_x + ball_radius
        y = ball_y + ball_radius 
        glVertex2f(x, y)
    glEnd()
    
    # Draw the stick
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(stick_x, stick_y)
    glVertex2f(stick_x + stick_width, stick_y)
    glVertex2f(stick_x + stick_width, stick_y + stick_height)
    glVertex2f(stick_x, stick_y + stick_height)
    glEnd()
    
    # Display the score
    glColor3f(1, 1, 1)
    glRasterPos2f(10, window_height - 20)
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('S'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('c'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('o'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('r'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('e'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(':'))
    score_str = str(score)
    for char in score_str:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    
    glFlush()

# Game over function
def game_over():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glColor3f(1, 1, 1)
    glRasterPos2f(window_width // 2 - 100, window_height // 2)
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('G'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('a'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('m'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('e'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(' '))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('O'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('v'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('e'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('r'))
    
    glColor3f(1, 1, 1)
    glRasterPos2f(window_width // 2 - 50, window_height // 2 - 20)
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('S'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('c'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('o'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('r'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord('e'))
    glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(':'))
    score_str = str(score)
    for char in score_str:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    
    glFlush()
    
    # Wait for a few seconds before exiting
    glutTimerFunc(2000, sys.exit, 0)

# Keyboard function
def special_keys(key, x, y):
    glutPostRedisplay()

# Main function
def main():
    glutInit()
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Ball Game")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(special_keys)
    glutMainLoop()

if __name__ == "__main__":
    main()
