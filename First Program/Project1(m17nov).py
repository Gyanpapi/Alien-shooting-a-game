from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
random.randint(0, 4)
import sys
bg_color=0
bg_color1=0
bg_color2=1
bg_color3=0

h = 0
#pause_game=False

expFactor = 1.0



i = -245
j = -90

Bombed = 0

h = 0







def reshape(width, height):
    fieldOfView = 90.0
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-662, 662, -350, 350, -450, 450)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


bomb_y=120
bomb_x=0
blust_bomb=False
explode1=0
def Bomb():
    global j, Bombed,bomb_y,bomb_x,explode1,bg_color,bomb_speed,game_paused
    if Bombed == 1:
        if(game_paused==False):
            j=j+bomb_speed-1
       # print(j)

  

   
   # glColor3f(0,139,34)
       # glColor3f(color.red,color.green,color.blue)
 ##   glLineWidth(2.5)
       
       # draw_circle(12,bomb_x,bomb_y+j,2)
        glColor3f(0,0,0)
    #    draw_circle(10,bomb_x,bomb_y+j,1)
     #   draw_circle1(21,bomb_x,bomb_y+j,1)
        
        
        ###########################
        
           # Bomb starting
        a=random.random() # Choose a random color
        b=random.random() # Choose a random color
        c=random.random() # Choose a random color
        if(a<0.5 and b<0.5 and c<0.5):    # to avoid a color that is similar to the background 
            b=1.5
        glColor3f(0,0,0)
        glPointSize(2)
        draw_circle(10,bomb_x,bomb_y+j,1)
        draw_circle1(21,bomb_x,bomb_y+j,1)
        draw_circle1(24,bomb_x,bomb_y+j,1)
        glColor3f(1,1,1)
        glPointSize(4)
        Mid_Point_Line(bomb_x,bomb_y+j+35,bomb_x,bomb_y+26+j) #bomb_ string
        glColor3f(a,b,c)
        Mid_Point_Line(bomb_x,bomb_y+42+j,bomb_x,bomb_y+50+j) # bomb strings
        glColor3f(c,b,a)
        Mid_Point_Line(bomb_x+5,bomb_y+37+j,bomb_x+14,bomb_y+37+j)
        glColor3f(b,a,c)
        Mid_Point_Line(bomb_x-5,bomb_y+37+j,bomb_x-14,bomb_y+37+j)
        glPointSize(2)
        glColor3f(1,1,1)
        Mid_Point_Line(bomb_x+10,bomb_y+j+15,bomb_x-8,bomb_y+j+15) #top
        Mid_Point_Line(bomb_x+18,bomb_y+j+10,bomb_x+10,bomb_y+j+15) #right top
        Mid_Point_Line(bomb_x-16,bomb_y+j+10,bomb_x-8,bomb_y+j+15)  #left top
  #  Mid_Point_Line(110,100,92,100)  
        Mid_Point_Line(bomb_x+10,bomb_y+j-10,bomb_x+18,bomb_y+j+10)
        Mid_Point_Line(bomb_x-8,bomb_y+j-10,bomb_x-16,bomb_y+j+10)
        Mid_Point_Line(bomb_x+10,bomb_y+j-10,bomb_x-8,bomb_y+j-10)
    #110,100
    #92,100
        Mid_Point_Line(bomb_x-8,bomb_y+j-10,bomb_x-8,bomb_y+j-16)
   # Mid_Point_Line(96,90,96,84)
        Mid_Point_Line(bomb_x-2,bomb_y+j-10,bomb_x-2,bomb_y+j-16)
        Mid_Point_Line(bomb_x+4,bomb_y+j-10,bomb_x+4,bomb_y+j-16)
        Mid_Point_Line(bomb_x+10,bomb_y+j-10,bomb_x+10,bomb_y+j-16)
        Mid_Point_Line(bomb_x-10,bomb_y+j-16,bomb_x+10,bomb_y+j-16)
   # Mid_Point_Line(110,100,110,90)
   # Mid_Point_Line(105,100,105,90)
   # Mid_Point_Line(110,100,84,110)
 #   Mid_Point_Line(92,100,84,110)
   # Mid_Point_Line(118,106,84,106)
  #  Mid_Point_Line(122,100,78,100)  # middle point
    
        Mid_Point_Line(bomb_x+4,bomb_y+j-7,bomb_x,bomb_y+j) # Nose
        Mid_Point_Line(bomb_x-4,bomb_y+j-7,bomb_x,bomb_y+j)
        Mid_Point_Line(bomb_x+4,bomb_y+j-7,bomb_x-4,bomb_y+j-7)
    
   # Mid_Point_Line(94,103,94,100)  #left eye
   # Mid_Point_Line(92,103,97,103)
        Mid_Point_Line(bomb_x-5,bomb_y+j+3,bomb_x-10,bomb_y+j+7)
    
 #   Mid_Point_Line()                #right eye
        Mid_Point_Line(bomb_x+5,bomb_y+j+3,bomb_x+10,bomb_y+j+7) 
    
    # Bomb ending
        
        ###########################
      #  if((bomb_y+j)<-100):
            
     #       draw_circle(10,bomb_x-100,bomb_y+100+j,2)
        
      #  if((bomb_y+j)<-150):
    #        draw_circle(10,bomb_x-200,bomb_y+150+j,2)
        
        if((bomb_y+j)<=-250):
          #  blust_bomb=True
            
            Bombed=0
            explode1=1
            bg_color=1

  #  glLineWidth(5.5)
parachute_y=0.0
parachute_x=0.0

ran=0
bomb_speed=0
def collision():
    global j,catcher_x,bomb_x,ran,bomb_speed,score,rocket_x,rocket_y,clicked
    if(bomb_y<=rocket_y+150 and ((bomb_x-24<=rocket_x+10) and bomb_x+24>=rocket_x-10)):
        print(bomb_y," ",rocket_y)
        
        reset_bomb()
        bomb_speed-=0.5
        score=score+1
       
       
        
def reset_bomb():  #both bomb and spaceship
    global j,m,bomb_x,ran,bomb_y,clicked
    bomb_y=100
    j=10
    ran=random.randint(-150,150)
  #  print("reason collisoin:(bombx,bomx+12,catch_x,catch_x+100)")
  #  print(bomb_x," ",bomb_x+12," ",catcher_x," ",catcher_x+100)
    m=ran
    bomb_x=ran
   # print("bomb")
   # print(bomb_x," ",bomb_x+12)
   # print('bomb')
    Bomb()
    rocket()
   # print("after update:(bombx,bomx+12,catch_x,catch_x+100)")
   # print(bomb_x," ",bomb_x+12," ",catcher_x," ",catcher_x+100)



sun_j=100
moon_flag=1
def draw_parachute():
    global parachute_y,parachute_x,bg_color,sun_j,moon_flag,game_paused

    # Draw the parachute
   # glColor3f(0.0, 0.6, 0.0)  # White color
    # Main body
  #  glPushMatrix()
  #  glTranslated(0,80,0)
  #  glScalef(80, 40, 1)
 #   glutSolidSphere(1, 120, 120) #smoothing
  #  glPopMatrix()
    
  #  glColor3f(0.9, 0.0, 0.0)  # White color
    # Main body
 #   glPushMatrix()
  #  glTranslated(0,90,0)
  #  glScalef(80, 20, 1)
   # glutSolidSphere(1, 12, 120) #smoothing
  #  glPopMatrix()
    
    
   # glColor3f(0.9, 0.0, 0.0)  # White color
    # Main body
  #  glPushMatrix()
    #glTranslated(0,70,0)
  #  glScalef(80, 20, 1)
  #  glutSolidSphere(1, 12, 120) #smoothing
  #  glPopMatrix()
    
    #draw_circle(70, 0, 150)
    if(i>400):
       # parachute_y-=2
    #draw_circle(70, 0, 150+parachute_y)
        if(parachute_y>-250):
           # print(parachute_y)
            if(game_paused==False):
                
                parachute_y-=7
            

        else:
            bg_color=0
            glColor3f(1,0.5,0)
        
            draw_circle(2,200,250+sun_j,1)
          #  draw_circle1(10,200,300,1)
          #  draw_circle(12,200,300,1)
          #  draw_circle1(15,200,300,1)
          #  draw_circle1(18,200,300,1)
          #  draw_circle1(20,200,300,1)
         #   draw_circle1(30,200,300,1)
            draw_circle(25,200,250+sun_j,1)
            draw_circle(10,200,250+sun_j,1)
          #  draw_circle1(35,200,300,1)
            draw_circle(40,200,250+sun_j,1)
         #   draw_circle1(45,200,300,1)r
            draw_circle1(50,200,250+sun_j,1)
            if(sun_j>0 and moon_flag==0 and game_paused==False):
                sun_j=sun_j-5

       
        glPointSize(2)
        glColor3f(0.0, 0.0, 0.8)  # Black color #right one 
        Mid_Point_Line(65.0+parachute_x, 120+parachute_y,0+parachute_x, 0+parachute_y)
    
        glColor3f(0.0, 0.0, 0.8)  # Black color #left one 
        Mid_Point_Line(-65.0+parachute_x, 120+parachute_y,0+parachute_x, 0+parachute_y)
    
        glColor3f(0.0, 0.0,0.8)  # Black color #middle one 
        Mid_Point_Line(0+parachute_x, 80+parachute_y,0+parachute_x, 0+parachute_y)
        glPointSize(10)
      #  glBegin(GL_LINES)
     #   glVertex2f(-50+parachute_x,0+parachute_y)
      #  glVertex2f(50+parachute_x,0+parachute_y)
        Mid_Point_Line(-50+parachute_x,0+parachute_y,50+parachute_x,0+parachute_y)
       # glVertex2f(-50+parachute_x,0+parachute_y)
      #  glVertex2f(-50+parachute_x,-30+parachute_y)
        Mid_Point_Line(-50+parachute_x,0+parachute_y,-50+parachute_x,-30+parachute_y)
     #   glVertex2f(50+parachute_x,0+parachute_y)
     #   glVertex2f(50+parachute_x,-30+parachute_y)
        Mid_Point_Line(50+parachute_x,0+parachute_y,50+parachute_x,-30+parachute_y)
      #  glVertex2f(50+parachute_x,-30+parachute_y)
     #   glVertex2f(-50+parachute_x,-30+parachute_y)
        Mid_Point_Line(50+parachute_x,-30+parachute_y,-50+parachute_x,-30+parachute_y)
       
        glColor3f(1.0, 0.0, 0.0)
            
        glColor3f(0.0, 0.7, 0.0)  
        draw_circle(70, 0+parachute_x, 150+parachute_y,2)
        draw_circle(50, 0+parachute_x, 150+parachute_y,2)
            
        glColor3f(1.0, 0.0, 0.0)
        draw_circle(10, 0+parachute_x, 150+parachute_y,2)
        draw_circle(30, 0+parachute_x, 150+parachute_y,2)
        
        
        
    #print(parachute_y)
    # Draw the strings
    
    


def Jet():
    global i, Bombed
    
   # if Bombed == 0:
  #      if scene == 3:
  #          i += 2
 #       else:
 #           i += 2
#    else:
 #       i+=2
     #   print(i)
     #   print(Bombed)
    glPointSize(5.0)

    # Begin drawing points
   # glBegin(GL_POINTS)

    # Specify the coordinates of the points
   # glVertex2f(0.0, 0.0)
    

    # End drawing points
  #  glEnd()
    if not game_paused:
        i+=14
        
    if(i>400):
        pass
     #   Bombed=1
       # Bomb()
    ############ mahin nnnn
    

  
    glColor3f(0.0, 0.5, 0.0)  # Black color
  
    glPointSize(23)
    Mid_Point_Line(-600+i,130,-300+i,130) #lower part
    Mid_Point_Line(-558+i,132,-298+i,132)
    Mid_Point_Line(-559+i,131,-299+i,131)
   # glVertex2f(-600.0+i, 130)
   # glVertex2f(-350+i,180)
   # Mid_Point_Line(-600+i,130,-350+i,180)  #upper part
   
    Mid_Point_Line(-350+i,170,-550+i,170)
    
    Mid_Point_Line(-300+i,130,-350+i,170)
    glColor3f(1.0, 0.0, 0.0)  # Black color
    Mid_Point_Line(-600.0+i, 130,-550+i,170)
   
    Mid_Point_Line(-600.0+i, 130,-600+i,245)
     
    Mid_Point_Line(-600+i,245,-550+i,170)
    
  
     
 
    glColor3f(0, 0, 0.9)

    glPointSize(10)
    Mid_Point_Line(-380+i, 150,-340+i, 150)
    Mid_Point_Line(-360+i, 160,-380+i, 160)
    Mid_Point_Line(-360+i,160,-340+i,150)
    Mid_Point_Line(-380+i,150,-380+i,160)
  

k=315
m=0
def DrawSpaceshipBody(isPlayer1):
    global k,m,Bombed,game_paused
    a=random.random() # Choose a random color
    b=random.random() # Choose a random color
    c=random.random() # Choose a random color
    if(a<0.5 and b<0.5 and c<0.5):    # to avoid a color that is similar to the background 
        b=1.5       
        
    glColor3f(0.5,0,0.5)
    
    if k>-30 and game_paused==False:
        k=k-12
    if k<=-30:
        #m=m-4
        draw_catcher()
        
    if((bomb_y+j)>-250 and k<=-30):
        Bombed=1
        Bomb()
    
   # if(Bombed):
    #    Bomb()
        
    # Main body
   # glLineWidth(2)
  #  glPushMatrix()
  #  glTranslated(m,70+k,0)
  #  glScalef(100, 25, 1)
  #  glutSolidSphere(1, 70, 70)
   # glPopMatrix()
    glColor3f(0.5,0,0.5)   
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(-50+m,50+k)
    glVertex2f(50+m,50+k)
    
    glVertex2f(-50+m,90+k)
    glVertex2f(50+m,90+k)
    
    glVertex2f(m,70+k)
    glVertex2f(m,90+k)
    
    glVertex2f(m,70+k)
    glVertex2f(m,90+k)
    
    glVertex2f(m,70+k)
    glVertex2f(m,90+k)
    
    glEnd()
   # print(m)
    draw_circle(11,-50+m,70+k,2)
    draw_circle(11,-30+m,70+k,2)
    draw_circle(11,-10+m,70+k,2)
    draw_circle(11,10+m,70+k,2)
    draw_circle(11,30+m,70+k,2)
    draw_circle(11,50+m,70+k,2)
    glColor3f(0,0,0)
    glPointSize(2)
    Mid_Point_Line(-70+11+m,80+11+k,50+11+m,80+11+k)
    Mid_Point_Line(-70+11+m,79+11+k,50+11+m,79+11+k)
    
    #Mid_Point_Line(-70+11+m,44+11+k,50+11+m,44+11+k)
    Mid_Point_Line(-70+11+m,41+11+k,50+11+m,41+11+k)



    # Side lights
    glLineWidth(1)

    
    glColor3f(a,b,c)
    glPointSize(10)
    glBegin(GL_POINTS)
    # co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(m, 70+k)
    glEnd()
    glColor3f(b,a,c)
    glPointSize(10)
    glBegin(GL_POINTS)
    # co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(m-20, 70+k)
    glEnd()
    
    glColor3f(c,b,a)
    glPointSize(10)
    glBegin(GL_POINTS)
    # co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(m+20, 70+k)
    glEnd()
    
    glColor3f(a,b,a)
    glPointSize(10)
    glBegin(GL_POINTS)
    # co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(m+40, 65+k)
    glEnd()
    
    glColor3f(c,a,b)
    glPointSize(10)
    glBegin(GL_POINTS)
    # co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(m-40, 65+k)
    glEnd()



def DrawSpaceshipDoom():
    global k,m
   # print(k)
    glColor3f(0,0,0)
    draw_circle(32,m,100+k,2)
  #  Mid_Point_Line(m-27,100+k,m,100+17+k)
  #  Mid_Point_Line(m+27,100+k,m,100+17+k)
  #  Mid_Point_Line(m+27,104+k,m,100-17+k)
  #  Mid_Point_Line(m-32,100-32+k,m+32,100-3+k)
    glColor4f(0.7,1,1,0.0011)

    draw_circle(30,m,100+k,2)



moon_j=100

byebye_spaceship=0
    
def explode():
    
    global expFactor,explode1,bg_color1,bg_color2,bg_color3,moon_j,moon_flag,byebye_spaceship,bomb_x,game_paused
    byebye_spaceship=1
    if(explode1==1):
        bg_color1=0
        bg_color2=0
        bg_color3=0
       
        glColor3f(0.7, 0, 0)
       
        draw_circle(12*expFactor,bomb_x,-250,1)
    
        glColor3f(0.3, 0, 0)
    
        draw_circle(8*expFactor,bomb_x,-250,1)
        
        if(game_paused==False):
            expFactor=expFactor+3
        if(expFactor>100):
            explode1=0
  

    

        
def Clouds1(r):
    
    
    glColor3f(0,0,0)
    draw_circle(35,-400,220,1)   #BlackMOON
   
    draw_circle(35,-350,220,1)   #MOON

    draw_circle(35,-350,220,1)   #MOON

    draw_circle(35,-450,220,1)   #MOON

    draw_circle(35,-425,270,1)   #MOON
  #
    draw_circle(35,-375,270,1)   #MOON

    glColor3f(1,1,1)
    draw_circle(30,-400,220,1)   #WhiteMOON
   # draw_circle1(25,-400,250,1)
  #  draw_circle1(23,-400,250,1)
  #  draw_circle1(28,-400,250,1)
    draw_circle(20,-400,220,1)
  #  draw_circle1(17,-400,250,1)
  #  draw_circle1(13,-400,250,1)
  #  draw_circle1(8,-400,250,1)
   # draw_circle1(15,-400,250,1)
  #  draw_circle1(10,-400,250,1)
    draw_circle(5,-400,220,1)
  #  draw_circle1(2,-400,250,1)
    draw_circle(30,-350,220,1)   #MOON
   # draw_circle1(25,-350,250,1)
  #  draw_circle1(23,-350,250,1)
  #  draw_circle1(28,-350,250,1)
    draw_circle(20,-350,220,1)
 #   draw_circle1(17,-350,250,1)
  #  draw_circle1(13,-350,250,1)
  #  draw_circle1(8,-350,250,1)
  #  draw_circle1(15,-350,250,1)
 #   draw_circle1(10,-350,250,1)
    draw_circle(5,-350,220,1)
 #   draw_circle1(2,-350,250,1)
    draw_circle(30,-350,220,1)   #MOON
   # draw_circle1(25,-350,250,1)
   # draw_circle1(23,-350,250,1)
   # draw_circle1(28,-350,250,1)
    draw_circle(20,-350,220,1)
   # draw_circle1(17,-350,250,1)
   # draw_circle1(13,-350,250,1)
   # draw_circle1(8,-350,250,1)
  #  draw_circle1(15,-350,250,1)
   # draw_circle1(10,-350,250,1)
    draw_circle(5,-350,220,1)
 #   draw_circle1(2,-350,250,1)
    draw_circle(30,-450,220,1)   #MOON
   # draw_circle1(25,-450,250,1)
  #  draw_circle1(23,-450,250,1)
  #  draw_circle1(28,-450,250,1)
    draw_circle(20,-450,220,1)
   # draw_circle1(17,-450,250,1)
   # draw_circle1(13,-450,250,1)
  #  draw_circle1(8,-450,250,1)
  #  draw_circle1(15,-450,250,1)
   # draw_circle1(10,-450,250,1)
    draw_circle(5,-450,220,1)
  #  draw_circle1(2,-450,250,1)
    draw_circle(30,-425,270,1)   #MOON
 #   draw_circle1(25,-425,300,1)
 #   draw_circle1(23,-425,300,1)
#    draw_circle1(28,-425,300,1)
    draw_circle(20,-425,270,1)
 #   draw_circle1(17,-425,300,1)
  #  draw_circle1(13,-425,300,1)
  #  draw_circle1(8,-425,300,1)
 #   draw_circle1(15,-425,300,1)
#    draw_circle1(10,-425,300,1)
    draw_circle(5,-425,270,1)
 #   draw_circle1(2,-425,300,1)
    draw_circle(30,-375,270,1)   #MOON
 #   draw_circle1(25,-375,300,1)
 #   draw_circle1(23,-375,300,1)
 #   draw_circle1(28,-375,300,1)
    draw_circle(20,-375,270,1)
 ##   draw_circle1(17,-375,300,1)
#    draw_circle1(13,-375,300,1)
 #   draw_circle1(8,-375,300,1)
  #  draw_circle1(15,-375,300,1)
 #   draw_circle1(10,-375,300,1)
    draw_circle(5,-375,270,1)
 #   draw_circle1(2,-375,300,1)
    
   # glColor3f(0,0,0)
  #  draw_circle1(1,-400,250,1)  # Moon black hole's
  #  draw_circle1(1,-400,250,1)
  #  draw_circle1(1,-400,260,1)
   # draw_circle1(1,-420,250,1)
  #  draw_circle1(1,-400,250,1)
  #  draw_circle1(1,-415,250,1)
  #  draw_circle1(1,-400,245,1)
    glColor3f(0,0,0)
    draw_circle(35,400,250,1)   #BlackMOON
   
    draw_circle(35,350,250,1)   #MOON

    draw_circle(35,350,250,1)   #MOON

    draw_circle(35,450,250,1)   #MOON

    draw_circle(35,425,300,1)   #MOON
  
    draw_circle(35,375,300,1)   #MOON

    glColor3f(1,1,1)
    draw_circle(30,400,250,1)   #WhiteMOON
    draw_circle(20,400,250,1)

    draw_circle(5,400,250,1)

    draw_circle(30,350,250,1)   #MOON
    draw_circle(20,350,250,1)
    draw_circle(5,350,250,1)
 
    draw_circle(30,350,250,1)   #MOON
 
    draw_circle(20,350,250,1)
   
    draw_circle(5,350,250,1)

    draw_circle(30,450,250,1)   #MOON
 
    draw_circle(20,450,250,1)

    draw_circle(5,450,250,1)

    draw_circle(30,425,300,1)   #MOON

    draw_circle(20,425,300,1)

    draw_circle(5,425,300,1)

    draw_circle(30,375,300,1)   #MOON

    draw_circle(20,375,300,1)
    draw_circle(5,375,300,1)

def createColor1(r, g, b, a):
    return {'red': r/255.0, 'green': g/255.0, 'blue': b/255.0, 'alpha': a/255.0}



score=0
def scored():
    
    if(score==1):
        Mid_Point_Line(420, 180, 420, 80)    # 400 300-> 200 ,100
    if(score==3):
        Mid_Point_Line(440, 180, 490, 180)
        Mid_Point_Line(440, 130, 490, 130)
        Mid_Point_Line(440, 80, 490, 80)
        Mid_Point_Line(490, 180, 490, 180)
        Mid_Point_Line(490, 180, 490, 80)

explode_flag_for_moon=0
def draw():
    global bg_color,clicked,game_paused,m,catcher_x,bomb_x,bomb_y,j,explode_flag_for_moon,parachute_y,moon_j,moon_flag,m,k # space ship x axis variable m and y for k
 
    #glColor3f(color.red, color.green, color.blue)
    bg_color1=0
    bg_color2=0.5
    bg_color3=0.9
    if(bg_color==0):
        
        glClearColor(bg_color1, bg_color2, bg_color3, 1)
        
    else:
        glClearColor(0, 0, 0.3, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #iterate()
   # Background()
   
    scored()                # for showing score on screen
    glPointSize(175)
    glColor3f(0,0.6,0)             # Lawn art
  #  Mid_Point_Line(-1200,-256,1200,-256)
   # Mid_Point_Line(-1200,-250,1200,-250)
    
   # Mid_Point_Line(-1200,-270,1200,-270)
   # Mid_Point_Line(-1200,-280,1200,-280)
    
   # Mid_Point_Line(-1200,-290,1200,-290)
    Mid_Point_Line(-1200,-315,1200,-315)
    glColor3f(0,0,0)
    DrawSpaceshipDoom()
    DrawSpaceshipBody(True)
    collision()
    if(clicked):
        rocket()
   # print(moon_flag)
   
    
   # Mid_Point_Line(-1200,-700,0,0)
  
   #bomb painting
    
   #bomb done
    if(byebye_spaceship and game_paused==False):
        m=m-16   # space ship x axis variable m
        catcher_x=900
    if(explode1):
        explode()
        explode_flag_for_moon=1
    if(explode_flag_for_moon):
        
        glColor3f(1,1,1)
    
        draw_circle(2,200,250+moon_j,1)
          #  draw_circle1(10,200,300,1)
          #  draw_circle(12,200,300,1)
          #  draw_circle1(15,200,300,1)
          #  draw_circle1(18,200,300,1)
          #  draw_circle1(20,200,300,1)
         #   draw_circle1(30,200,300,1)
        draw_circle(10,200,250+moon_j,1)
        draw_circle(25,200,250+moon_j,1)
           #  draw_circle1(35,200,300,1)
        draw_circle(40,200,250+moon_j,1)
         #   draw_circle1(45,200,300,1)
        draw_circle1(50,200,250+moon_j,1)
        if(moon_j>=0 and moon_flag==1 and game_paused==False):
            moon_j=moon_j-10
        if(moon_j<0):
            moon_flag=0
        
        if(parachute_y<-50 and game_paused==False):
            moon_j=moon_j+3;
            
        
    #explode()
    
    #draw stickma
    
    #draw_parachute()
    #Flames(4,5)
    #Candles()
    Clouds1(1)
    draw_parachute()
   # print(game_paused)
    #blust()
  #  glLineWidth(1)
  #  glBegin(GL_LINES)
   # glColor3f(1.0, 0.0, 0.0)
   # glVertex2f(250,0)
   # glVertex2f(-250,0)
    #glColor3f(0.0, 0.0, 1.0) 
    #glVertex2f(0,250)
   # glVertex2f(0,-250)
   
   # Bomb starting
 
    #stickman 1
    
    if(Bombed!=1 and k>-30):
        glColor3f(0,0,0)
        glPointSize(2)
        Mid_Point_Line(300,-220,325,-180) # first stickman
        Mid_Point_Line(350,-220,325,-180)
        Mid_Point_Line(355,-120,325,-180)  # stickman body
        draw_circle2(22,370,-100,1) # face
        draw_circle2(8,360,-111,1)  # mouth
        #draw_circle2(8,366,-102,1)
        draw_circle2(2,360,-95,1)  # eyes
        draw_circle2(2,375,-100,1)
        Mid_Point_Line(355,-90,365,-85) # eye brow
        Mid_Point_Line(375,-88,380,-98)
        Mid_Point_Line(375,-65,390,-45) #shocking
        Mid_Point_Line(395,-75,410,-55)
        Mid_Point_Line(405,-95,420,-80)
    
        Mid_Point_Line(349,-135, 380,-150) #hands
        Mid_Point_Line(380,-150,380,-115)
        draw_circle2(2,380,-115,1)
    
        Mid_Point_Line(349,-135,300,-90)
        draw_circle2(2,300,-90,1)
    
        #Mid_Point_Line(-300,-220,-325,-180) # second stickman
        Mid_Point_Line(-370,-220,-370,-180)
        Mid_Point_Line(-370,-180,-400,-220)
        Mid_Point_Line(-370,-125,-370,-180)  # stickman body
        draw_circle2(22,-370,-100,1) # face
        draw_circle2(4,-352,-106,1)  # mouth   
        draw_circle2(2,-370,-95,1)  # eyes    
        Mid_Point_Line(-375,-90,-380,-100) # eye brow     
        Mid_Point_Line(-340,-144, -370,-144) #hands
        Mid_Point_Line(-370,-144,-345,-120)
        draw_circle2(2,-340,-115,1)  
        draw_circle2(2,-346,-122,1)  
        Mid_Point_Line(-340,-144,-340,-115)           
   # print(catcher_x-50," ",bomb_x+10)           
        ###
    # Bomb ending
  ##  glEnd()
   # print(bomb_y+j)
    if m<-750 and ((bomb_y+j)<=-250) and expFactor>100:
      
        Jet()
   # Bomb()



    glFlush()
    glutSwapBuffers()

game_paused = False
def mouseListener(button, state, x, y):
    global game_paused,bomb_y,bomb_x,j
   
  #  print(bomb_x-648," ",bomb_x+649)

    if button == GLUT_LEFT_BUTTON :
        if state==GLUT_DOWN:
            
            if 20<=x <= 70 :  # Restart button

                print("Starting over")

            elif 0 <= x <= 225 :  # Pause button
                game_paused = not game_paused
            
            elif bomb_y-16-349+j<=y<=bomb_y-j+16+349+j and bomb_x-16-648<=x<=bomb_x+648+16 and Bombed==1:
               # print('mm')
                bomb_y=bomb_y+10
            #j=j+100
         
            
     #   elif 340 <= x <= 380 :  # Quit button
      
      #      glutLeaveMainLoop()
            else:
                pass
    if button == GLUT_RIGHT_BUTTON:
        if state==GLUT_DOWN:
            
           game_paused = not game_paused
    
   # Mid_Point_Line(1200,0,1200,0)

        
def idle():
    glutPostRedisplay()

def initGL(width, height):
    reshape(width, height)
    glClearColor(1.2, 0.8, 1.0, 1.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    
def specialKeyListener(key, x, y):
    global bg_color,parachute_x,i,game_paused
    if key == GLUT_KEY_LEFT and i>400 and game_paused==False:  # left arrow key
        parachute_x=parachute_x-50
    elif key == GLUT_KEY_RIGHT and game_paused==False :  # right arrow key
        parachute_x=parachute_x+50
    else:
        pass
    glutPostRedisplay()

rocket_y=-150
rocket_x=0
clicked=0
def rocket():
    global rocket_y,rocket_x,clicked
    glColor3f(1,0,1)
    draw_circle2(20,rocket_x,rocket_y,1)
    rocket_y+=5
  #  print(rocket_y," ",bomb_y)
    if(rocket_y==100):
        clicked=0
        rocket_y=-150

    
def keyboardListener(key, x, y):

    global catcher_x,game_paused,Bombed,clicked,rocket_x
    if key==b'd' and game_paused==False:
        catcher_x+=20
      #  print("Size Increased")
    if key==b'a' and game_paused==False:
        catcher_x-=20
       # print("Size Decreased")
    if key==b's' and game_paused==False and Bombed==1 and clicked==0 and rocket_y==-150:
        rocket_x=catcher_x
        clicked=1
        
  
        #print()
       # print("Size Decreased")
    #print('catch')
    #print(catcher_x," ",catcher_x+100)

   # print('catch')

    glutPostRedisplay()
    
def circlePoints(x, y, x0, y0,d):
    draw_points(x + x0, y + y0,d)
    draw_points(y + x0, x + y0,d)
   
    draw_points(y + x0, -x + y0,d)
    draw_points(x + x0, -y + y0,d)
    draw_points(-x + x0, -y + y0,d)
    draw_points(-y + x0, -x + y0,d)
    draw_points(-y + x0, x + y0,d)
    draw_points(-x + x0, y + y0,d)

def midpointcircle(radius, x0, y0,d):
    d = 1 - radius
    x = 0
    y = radius

    circlePoints(x, y, x0, y0,d)

    while x < y:
        #print("y")
        if d < 0:
            # Choose East.
            d = d + 2*x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2*x -2*y + 5
            x += 1
            y = y - 1

        circlePoints(x, y, x0, y0,d)

def draw_circle(radius, x0, y0,d):
    midpointcircle(radius, x0, y0,d)        # outer circle

  
  

# This function is used to draw pixels.
def draw_points(x, y,d):
    # The parameter that is passed in the function dictates the size of the pixel.

    glPointSize(20)

    glBegin(GL_POINTS)

    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    
    glVertex2f(x, y)

    glEnd()


#######################################################

def circlePoints1(x, y, x0, y0,d):
    draw_points1(x + x0, y + y0,d)
    draw_points1(y + x0, x + y0,d)
   
    draw_points1(y + x0, -x + y0,d)
    draw_points1(x + x0, -y + y0,d)
    draw_points1(-x + x0, -y + y0,d)
    draw_points1(-y + x0, -x + y0,d)
    draw_points1(-y + x0, x + y0,d)
    draw_points1(-x + x0, y + y0,d)

def midpointcircle1(radius, x0, y0,d):
    d = 1 - radius
    x = 0
    y = radius

    circlePoints1(x, y, x0, y0,d)

    while x < y:
        #print("y")
        if d < 0:
            # Choose East.
            d = d + 2*x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2*x -2*y + 5
            x += 1
            y = y - 1

        circlePoints1(x, y, x0, y0,d)

def draw_circle1(radius, x0, y0,d):
    midpointcircle1(radius, x0, y0,d)        # outer circle

  
  

# This function is used to draw pixels.
def draw_points1(x, y,d):
    # The parameter that is passed in the function dictates the size of the pixel.

    glPointSize(4)

    glBegin(GL_POINTS)

    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    
    glVertex2f(x, y)

    glEnd()
    
############# mid circle 2 ################
def circlePoints2(x, y, x0, y0,d):
    draw_points2(x + x0, y + y0,d)
    draw_points2(y + x0, x + y0,d)
   
    draw_points2(y + x0, -x + y0,d)
    draw_points2(x + x0, -y + y0,d)
    draw_points2(-x + x0, -y + y0,d)
    draw_points2(-y + x0, -x + y0,d)
    draw_points2(-y + x0, x + y0,d)
    draw_points2(-x + x0, y + y0,d)

def midpointcircle2(radius, x0, y0,d):
    d = 1 - radius
    x = 0
    y = radius

    circlePoints2(x, y, x0, y0,d)

    while x < y:
        #print("y")
        if d < 0:
            # Choose East.
            d = d + 2*x + 3
            x += 1
        else:
            # Choose South East.
            d = d + 2*x -2*y + 5
            x += 1
            y = y - 1

        circlePoints2(x, y, x0, y0,d)

def draw_circle2(radius, x0, y0,d):
    midpointcircle2(radius, x0, y0,d)        # outer circle

  
  

# This function is used to draw pixels.
def draw_points2(x, y,d):
    # The parameter that is passed in the function dictates the size of the pixel.

    glPointSize(2)

    glBegin(GL_POINTS)

    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    
    glVertex2f(x, y)

    glEnd()

######################################
# ... Midpoint line algo code...

def draw1(x, y):
   # glPointSize(2)
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
        draw1(a, b)
        if D <= 0:
            D = D + dE
            d += [D]
            x = x + 1
        else:
            x = x + 1
            y = y + 1
            D = D + dNE

# end of midpoint line algo code

catcher_x=0

def draw_catcher():
    global k,catcher_x
    if(k<=-30):
        
        glColor3f(0.0, 0.0, 0.0)
        glPointSize(2)
       # Mid_Point_Line(catcher_x, -230, catcher_x+10, -180)
      #  Mid_Point_Line(catcher_x+100,-230,catcher_x+90,-180)
       # Mid_Point_Line(catcher_x,-230,catcher_x+100,-230)
        Mid_Point_Line(catcher_x-40,-177,catcher_x+40,-177)  #upper part 
        Mid_Point_Line(catcher_x-40,-172,catcher_x+40,-172)
        
        glPointSize(3)
        Mid_Point_Line(catcher_x-40,-175,catcher_x-30,-202)   # black left rightpart basket
        Mid_Point_Line(catcher_x+40,-175,catcher_x+30,-202)
        
        Mid_Point_Line(catcher_x-28,-205,catcher_x+28,-205)  #lower part 
        Mid_Point_Line(catcher_x-28,-200,catcher_x+28,-200)
        
        Mid_Point_Line(catcher_x-28,-205,catcher_x+28,-205)  #lower part 
        Mid_Point_Line(catcher_x-20,-200,catcher_x-20,-210)
        Mid_Point_Line(catcher_x+20,-200,catcher_x+20,-210)
 
 
        
        draw_circle2(2,catcher_x-20,-218,1)
        draw_circle2(8,catcher_x-20,-218,1)
        draw_circle2(2,catcher_x+20,-218,1)
        draw_circle2(8,catcher_x+20,-218,1)
        glPointSize(2)
        glColor3f(1.0, 0.0, 0.0)                               # red basket
        Mid_Point_Line(catcher_x-38,-174.5,catcher_x+38,-174.5)
        Mid_Point_Line(catcher_x-28,-202.5,catcher_x+28,-202.5)
        glPointSize(2)
            # draw stickman
        glColor3f(0,0,0)
        draw_circle2(15,-70+catcher_x,-150,1)  # drawing stickman
        draw_circle2(15,70+catcher_x,-150,1)
        Mid_Point_Line(70+catcher_x,-165,70+catcher_x,-200) # body
        Mid_Point_Line(-70+catcher_x,-165,-70+catcher_x,-200)
        Mid_Point_Line(-68+catcher_x,-220,-70+catcher_x,-200) # legs
        Mid_Point_Line(-60+catcher_x,-215,-70+catcher_x,-200)
        Mid_Point_Line(78+catcher_x,-220,70+catcher_x,-200) # legs
        Mid_Point_Line(50+catcher_x,-215,70+catcher_x,-200)
        Mid_Point_Line(70+catcher_x,-165,40+catcher_x,-180)  #hands
        Mid_Point_Line(-70+catcher_x,-165,-40+catcher_x,-180)
        Mid_Point_Line(40+catcher_x,-177,40+catcher_x,-183)  # basket stick to hold
        Mid_Point_Line(-40+catcher_x,-177,-40+catcher_x,-183)
        Mid_Point_Line(-55+catcher_x,-150,-60+catcher_x,-160) # mouth
        Mid_Point_Line(55+catcher_x,-150,60+catcher_x,-160)
        Mid_Point_Line(65+catcher_x,-155,60+catcher_x,-155)
        Mid_Point_Line(-65+catcher_x,-155,-60+catcher_x,-155)
    
        Mid_Point_Line(63+catcher_x,-147,63+catcher_x,-147) # eye
        Mid_Point_Line(-63+catcher_x,-147,-63+catcher_x,-147)
    
        Mid_Point_Line(60+catcher_x,-144,66+catcher_x,-140) # eyebrow
        Mid_Point_Line(-60+catcher_x,-144,-66+catcher_x,-140)
   
    
        ################
    
    

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(1244, 700)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"pROOJECT")

    # register glut call backs
  
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutReshapeFunc(reshape)
glutDisplayFunc(draw)
  
glutIdleFunc(idle)
glutIgnoreKeyRepeat(1)  # ignore key repeat

initGL(1244, 700)
glutMainLoop()