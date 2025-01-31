from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin
import math
# Initialize the variables as per your requirement
obj = gluNewQuadric()
ro = 0.0
speed = 0.0
bladeAngle = 0.0
moving = False
curX = 0.0
curZ = 0.0
heliRot = 0.0
eyeX = 0.0
eyeY = 0.0
eyeZ = 0.0
upX = 0.0
upY = 0.0
upZ = 0.0
r = 0.0
theta = 0.0
phi = 0.0
viewPerson = 0
THIRD = 0
lightingEnabled = False
headlight = False

def drawGround(size, numSegments):
    init = -size / 2.
    d = size / numSegments
    x = init
    for i in range(numSegments + 1):
        z = init
        glBegin(GL_TRIANGLE_STRIP)
        glNormal3f(0, 1, 0)
        glColor3f(0.5, 0.5, 0.5)
        xd = x + d
        for j in range(numSegments + 1):
            glVertex3f(x, 0.0, z)
            glVertex3f(xd, 0.0, z)
            z += d
        glEnd()
        x = xd

def moveHelicopter():
    global ro, bladeAngle, moving, curX, curZ, heliRot
    if moving:
        ro += speed
        bladeAngle += 31.0

    if ro >= 180:
        ro = -180

    prevX = curX
    prevZ = curZ

    curX = 100 * ((math.cos(ro * math.pi / 180) / (1 + math.sin(ro * math.pi / 180) * math.sin(ro * math.pi / 180))))
    curZ = 100 * ((math.cos(ro * math.pi / 180) * (math.sin(ro * math.pi / 180))) / (1 + math.sin(ro * math.pi / 180) * math.sin(ro * math.pi / 180)))

    if moving:
        magnitude = math.sqrt(curX * curX + curZ * curZ)
        heliRot = math.atan2(((curX - prevX) / magnitude) * -1.0, ((curZ - prevZ) / magnitude) * -1.0)

    glTranslatef(curX, 0.0, curZ)

def lemniscate(a, t):
    return a * math.cos(t) / (math.sin(t) * math.sin(t) + 1)

def drawTrack(a, numSegments):
    width = 10.0
    t = 0.0
    dt = 2.0 * math.pi / numSegments

    # init values
    lastX = lemniscate(a, t)
    lastZ = lastX * math.sin(t)

    curX, curZ = None, None

    glBegin(GL_TRIANGLE_STRIP)
    glNormal3f(0, 1, 0)
    glColor3f(0.3, 0.3, 0.3)

    # loop and draw
    for i in range(numSegments + 1):
        # increment state
        t += dt
        curX = lemniscate(a, t)
        curZ = curX * math.sin(t)
        dX = curX - lastX
        dZ = curZ - lastZ
        lastX = curX
        lastZ = curZ

        # normalize dX, dZ
        factor = 1.0 / math.sqrt(dX * dX + dZ * dZ)

        # rotate dX, dZ by 90 deg, and apply track width
        tX = dX * factor
        dX = -(dZ * factor) * width
        dZ = tX * width

        # draw vertices
        glVertex3f(curX - dX, 0.0, curZ - dZ)
        glVertex3f(curX + dX, 0.0, curZ + dZ)

    glEnd()


def moveCamera():
    global eyeX, eyeY, eyeZ, upX, upY, upZ, theta, phi, r
    if viewPerson == THIRD:
        # Restrict the angles within 0~360 deg (optional)
        if theta > 360:
            theta = theta % 360
        if phi > 360:
            phi = phi % 360

        # Spherical to Cartesian conversion.
        # Degrees to radians conversion factor 0.0174532
        eyeX = r * math.sin(theta * 0.0174532) * math.sin(phi * 0.0174532)
        eyeY = r * math.cos(theta * 0.0174532)
        eyeZ = r * math.sin(theta * 0.0174532) * math.cos(phi * 0.0174532)

        # Reduce theta slightly to obtain another point on the same longitude line on the sphere.
        dt = 1.0

        # Connect these two points to obtain the camera's up vector.
        upX = (r * math.sin((theta - dt) * 0.0174532) * math.sin(phi * 0.0174532)) - eyeX
        upY = (r * math.cos((theta - dt) * 0.0174532)) - eyeY
        upZ = (r * math.sin((theta - dt) * 0.0174532) * math.cos(phi * 0.0174532)) - eyeZ

def setThirdPersonLight():
    # Turn light 3 on
    glEnable(GL_LIGHT3)

    # Aspects of light 3
    glEnable(GL_NORMALIZE)  # normalize lighting
    glEnable(GL_COLOR_MATERIAL)  # keeps some of original colors

    diffuse = [1, 0, 0, 0.0]
    glLightfv(GL_LIGHT3, GL_DIFFUSE, diffuse)  # color of the direct illumination
    glMaterialfv(GL_FRONT, GL_DIFFUSE, diffuse)

    specular1 = [1, 0, 0, 0.0]
    glLightfv(GL_LIGHT3, GL_SPECULAR, specular1)  # color of the highlight
    glMaterialfv(GL_FRONT, GL_SPECULAR, specular1)

    ambient = [0.5, 0, 0, 0.0]
    glLightfv(GL_LIGHT3, GL_AMBIENT, ambient)  # color of the reflected light
    glMaterialfv(GL_FRONT, GL_AMBIENT, ambient)

    ltPosition = [eyeX + curX, eyeY, eyeZ + curZ, 1.0]
    glLightfv(GL_LIGHT3, GL_POSITION, ltPosition)

    glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, 40.0)  # width of the beam
    glLightf(GL_LIGHT3, GL_SPOT_EXPONENT, 15)

    specReflection = [0.2, 0.2, 0.2, 1.0]  # How bright the white spots are
    glMaterialfv(GL_FRONT, GL_SPECULAR, specReflection)  # How much the object reflects light

def drawBody():
    glColor3f(0.33, 0.42, 0.18)
    glPushMatrix()
    glScalef(1.0, 1.0, 2.0)
  #  glutSolidCube(6.0)
    glPopMatrix()

def drawCockpit():
    # Cockpit Windshield
    glColor3f(0.0, 0.0, 1.0)
    glPushMatrix()
    glScalef(1.33, 1.0, 1.0)
    glTranslatef(0.0, 0.0, 6.0)
   # glutSolidSphere(3, 100, 100)
    glPopMatrix()

    # Cockpit Base
    glColor3f(0.33, 0.42, 0.18)
    glPushMatrix()
    glTranslatef(0.0, -1.5, 6.0)
    glScalef(1.33, 0.65, 1.33)
  #  glutSolidSphere(3, 100, 100)
    glPopMatrix()

    glDisable(GL_TEXTURE_GEN_S)  # disable texture coordinate generation
    glDisable(GL_TEXTURE_GEN_T)
    glDisable(GL_TEXTURE_2D)

def drawBlade():
    glPushMatrix()
    glRotatef(10., 0.0, 0.0, 1.0)
    glScalef(0.75, 0.2, 10.0)
  #  gluCylinder(obj, 0.5, 0.5, 1, 16, 1)
    glPushMatrix()
    glTranslatef(0.0, 0.0, 1.0)
  #  gluDisk(obj, 0.0, 0.5, 16, 1)
    glPopMatrix()
    glPopMatrix()

def drawBladeCap():
    glPushMatrix()
    glRotatef(-90.0, 1.0, 0.0, 0.0)
    glScalef(1.0, 1.0, 1.0)
    gluCylinder(obj, 0.5, 0.5, 1, 16, 1)
    glPushMatrix()
    glTranslatef(0.0, 0.0, 1.0)
    gluDisk(obj, 0.0, 0.5, 16, 1)
    glPopMatrix()
    glPopMatrix()

def drawHelicopter():
    glPushMatrix()
    drawBody()
    drawBlade()
    drawBlade()
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
    drawBladeCap()
    
    glLoadIdentity()
    gluLookAt(eyeX, eyeY, eyeZ, curX, 0.0, curZ, upX, upY, upZ)
     
    glutSwapBuffers()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, w/h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def keyboard(key, x, y):
    global moving
    if key == b' ':
        moving = not moving

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b'Helicopter')
    init()
    glutDisplayFunc(display)
  #  glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
