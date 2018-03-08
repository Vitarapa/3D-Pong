from visual import *
from visual.controls import *
from random import randint
import numpy as np

# objects

left_paddle = box( pos = (-6, 0, 0), size = (0.2, 2, 3), color = color.white)
right_paddle = box( pos = (6, 0, 0), size = (0.2, 2, 3), color = color.white)

ball = sphere(pos = (0, 0, 0), radius = 0.35, color = color.white)

wall_L = box( pos = (-7, 0, 0), size = (0.2, 10, 10), color = color.blue)

wall_R = box( pos = (7, 0, 0), size = (0.2, 10, 10), color = color.blue)

wall_T = box( pos = (0, 5, 0), size = (14, 0.2, 10), color = color.blue)

wall_B = box( pos = (0, -5, 0), size = (14, 0.2, 10), color = color.blue)

wall_back = box( pos = (0, 0, -5), size = (14, 10, 0.2), color = color.blue)


# velocity

velocity = vector(randint(-1,1)*0.5, np.random.rand()*0.5, 0)
paddle_v = vector(0, 1, 0)

# score

left_score = text(text='0', pos = (-3,1.5,0), depth=-0.3, color=color.green)


right_score = text(text='0', pos = (3,1.5,0), align='center', depth=-0.3, color=color.green)



#Function returns true if ball hit either paddle, false otherwise

def hitPaddle():
    if ball.pos.x - ball.radius <= left_paddle.pos.x and \
                    ball.pos.y <= left_paddle.pos.y + (left_paddle.size.y / 2) and \
                    ball.pos.y >= left_paddle.pos.y - (left_paddle.size.y / 2):
        return True

    elif  ball.pos.x + ball.radius >= right_paddle.pos.x and \
                    ball.pos.y <= right_paddle.pos.y + (right_paddle.size.y / 2) and \
                    ball.pos.y >= right_paddle.pos.y - (right_paddle.size.y / 2):
        return True

    else:
        return False


def hitWall():
    if ball.pos.y + ball.radius >= wall_T.pos.y:
        velocity.y = velocity.y*(-1)
    elif ball.pos.y - ball.radius <= wall_B.pos.y:
        velocity.y = velocity.y*(-1)
    else:
        return True


#Function returns adds score accordingly if either paddle is passed

def passedPaddle(velocity):

    if velocity.x < 0 and \
       ball.pos.x - ball.radius <= left_paddle.pos.x and \
       hitPaddle() == False:
        
        temp_score2 = int(right_score.text) + 1
        right_score.text = str(temp_score2)
        return True

    elif velocity.x > 0 and \
       ball.pos.x + ball.radius >= right_paddle.pos.x and \
       hitPaddle() == False:

        temp_score = int(left_score.text) + 1
        left_score.text = str(temp_score)
        return True

    else:
        return False

# controls
#
def controls_r(key):

##    key = scene.kb.getkey()
    #   ev = scene.waitfor('click')
    #   ev = scene.waitfor('click')

    if key == 'up' and right_paddle.pos.y + (right_paddle.size.y/2) != wall_T.pos.y:
        
        right_paddle.pos = right_paddle.pos + paddle_v*0.4
    elif key == 'down' and right_paddle.pos.y - (right_paddle.size.y/2) != wall_B.pos.y:
        right_paddle.pos = right_paddle.pos - paddle_v*0.4
    else:
        pass

#def controls_r_d():

#    right_paddle.pos = right_paddle.pos - paddle_v*0.1


def controls_l(key):

 #   ev = scene.waitfor('click')
    if key == 'w' and left_paddle.pos.y + (left_paddle.size.y/2) != wall_T.pos.y:
        left_paddle.pos = left_paddle.pos + paddle_v*0.4
    elif key == 's' and left_paddle.pos.y - (left_paddle.size.y/2) != wall_B.pos.y:
        left_paddle.pos = left_paddle.pos - paddle_v*0.4
    else:
        pass


#def controls_l_u():
#    left_paddle.pos = left_paddle.pos + paddle_v*0.1
#def controls_l_d():
#    left_paddle.pos = left_paddle.pos - paddle_v*0.1


print passedPaddle(velocity)

while passedPaddle(velocity) == False:
   # print "started"
    if velocity.x != 0: #and int(right_score.text) < 10 and int(left_score.text) < 10:

        rate(100)
        ball.pos = ball.pos + velocity*0.1
#        controls_r()
        if scene.kb.keys:  # check if there are any keys pressed in the queue
            
            key = scene.kb.getkey()

            #print "key start"
            controls_l(key)
            controls_r(key)
            #print "key det"

        if hitPaddle() == True:

            velocity.x = velocity.x*(-1)


        elif passedPaddle(velocity) == True:

            ball.pos.x = 0
            ball.pos.y = 0
            velocity = vector(randint(-1,1)*0.5, np.random.rand()*0.5, 0)

        else:
            hitWall()

      
            
    elif velocity.x == 0:

        velocity.x = randint(-1,1)

 #   elif int(left_score.text) == 9:
#        temp_score = int(left_score.text) + 1
#        left_score.text = str(temp_score)
#        passedPaddle(velocity) == True
#        
#    elif int(right_score.text) == 9:
#        temp_score2 = int(right_score.text) + 1
#        right_score.text = str(temp_score2)
#        passedPaddle(velocity) == True

    else:
        passedPaddle(velocity) == True

    


                       
