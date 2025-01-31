from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

pi = 3.142857

# Global Declaration
c, d, left, right = 0, 0, 0, 0
m, j, flag1, l, flag2, n, score, count = 0, 1, 0, 1, 0, 0, 0, 1

W_Width, W_Height = 1100, 600

# Initialize ball position at the top
ball_x, ball_y = random.uniform(-620, 620), W_Height // 2

# Initialize ball motion
ball_speed_x, ball_speed_y = 0, -1.0

# Initialize the position and size of the moveable stick
stick_x = 0
stick_width = 200

# Timer interval in milliseconds (adjust this to control ball speed)
timer_interval = 10

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
    global stick_x

    if key == b'b':
        stick_x -= 20
    elif key == b'n':
        stick_x += 20

    glutPostRedisplay()

# Timer function to control ball movement
def timer(value):
    global ball_x, ball_y, ball_speed_x, ball_speed_y, score, stick_x, stick_width

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check if the ball touches the stick
    if ball_y < -300 and stick_x <= ball_x <= stick_x + stick_width:
        ball_speed_y = 1.0
        score += 1
        stick_x = 0  # Reset the stick position

    if ball_y < -340:
        # Check if the ball touches the border line
        if ball_x < -620 or ball_x > 620:
            print("Game Over! Your Score is:", score)
            exit(0)

    if ball_x >= 620:
        ball_speed_x = -ball_speed_x

    if ball_x <= -620:
        ball_speed_x = -ball_speed_x

    glutPostRedisplay()
    glutTimerFunc(timer_interval, timer, 0)

# Main display function
def myDisplay():
    global c, d, left, right, m, j, flag1, l, flag2, n, score, stick_x, stick_width

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

    # Display the stick
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(stick_x - stick_width / 2, -320)
    glVertex2f(stick_x + stick_width / 2, -320)
    glVertex2f(stick_x + stick_width / 2, -310)
    glVertex2f(stick_x - stick_width / 2, -310)
    glEnd()

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

    # Set up the timer
    glutTimerFunc(timer_interval, timer, 0)

    glutMainLoop()

if __name__ == "__main__":
    main()
