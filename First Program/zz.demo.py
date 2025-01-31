from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random

pi = 3.142857

# Global Declaration
c, d, left, right = 0, 0, 0, 0
m, j, flag1, l, flag2, n, score, count = 0, 1, 0, 1, 0, 0, 0, 1
game_over = False  # Flag to indicate game over

W_Width, W_Height = 1100, 600

# Initialize ball position at a random x-coordinate at the top
ball_x, ball_y = random.uniform(-600, 600), W_Height - 20

# Initialize ball motion
ball_speed_x, ball_speed_y = 0, -1.0  # Start with no horizontal motion and downward motion
ball_acceleration_x = 0.01  # Horizontal acceleration (optional)
timer_interval = 10  # Timer interval for animation

# Initialization function
def myInit():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-620.0, 620.0, -340.0, 340.0)

# Keyboard function
def keyboard(key, x, y):
    global c, d, left, right
    left = -200 + 200 * (d - c)
    right = 200 + 200 * (d - c)

    if left == -600:
        if key == b'n':
            d += 1
    elif right == 600:
        if key == b'b':
            c += 1
    else:
        if key == b'b':
            c += 1
        if key == b'n':
            d += 1

    glutPostRedisplay()

# Timer function to control ball animation
def timer(value):
    global ball_x, ball_y, ball_speed_x, ball_speed_y, ball_acceleration_x, game_over

    if not game_over:
        # Update ball position and speed
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Apply optional horizontal acceleration
        ball_speed_x += ball_acceleration_x

        if ball_y < -340:
            # Check if the ball touches the lower stick (adjust the condition as needed)
            left = -200 + 200 * (d - c)
            right = 200 + 200 * (d - c)
            if ball_x < left or ball_x > right:
                game_over = True  # Set game over flag

        glutPostRedisplay()

        # Control the timer interval to control the animation speed
        glutTimerFunc(timer_interval, timer, 0)

# Main display function
def myDisplay():
    global c, d, left, right, m, j, flag1, l, flag2, n, score, game_over

    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_LINE_STRIP)

    x, y, k = ball_x, ball_y, 0
    i = 0

    m = m + 6
    n = n + 4

    while i <= 2 * pi:
        y = 12 + 20 * math.cos(i)
        x = 20 * math.sin(i)
        i = i + 0.1

        if m == 288 and flag1 == 0:
            j = -1
            m = -288
            flag1 = 1
            score += 1

        if m == 288 and flag1 == 1:
            j = 1
            m = -288
            flag1 = 0

        if n == 580 and flag2 == 0:
            l = -1
            n = -580
            flag2 = 1

        if n == 580 and flag2 == 1:
            l = 1
            n = -580
            flag2 = 0

        glVertex2i(int(x - l * n), int(y - j * m))

    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex2i(-600, -320)
    glVertex2i(-600, 320)
    glVertex2i(600, 320)
    glVertex2i(600, -320)
    glEnd()

    left = -200 + 200 * (d - c)
    right = 200 + 200 * (d - c)
    glBegin(GL_LINE_LOOP)

    glVertex2i(left, -315)
    glVertex2i(left, -295)
    glVertex2i(right, -295)
    glVertex2i(right, -315)
    glEnd()

    if (j * m) == 276:
        if ball_y < -340:
            game_over = True  # Set game over flag
        if not game_over:
            if ball_x < left or ball_x > right:
                game_over = True  # Set game over flag

    if game_over:
        # Display "Game Over" in the window
        glColor3f(1.0, 0.0, 0.0)
        glRasterPos2f(-50, 0)
        for char in "Game Over! Your Score is: " + str(score):
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
        glutSwapBuffers()
    else:
        # Display the score
        glColor3f(0.0, 0.0, 0.0)
        glRasterPos2f(-600, 300)
        for ch in "Score: " + str(score):
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))
        glutSwapBuffers()

# Main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(W_Width, W_Height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Game")

    glutKeyboardFunc(keyboard)
    myInit()
    glutDisplayFunc(myDisplay)

    # Start the ball falling animation
    glutTimerFunc(timer_interval, timer, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()
