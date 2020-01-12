import turtle
import os


wn = turtle.Screen()
wn.title('PONG')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)    #restricts automatic updating


#Scores

score_a = 0
score_b = 0

#Adding Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)   #Speed of Animation - HIGH speed
paddle_a.shape('square')    #20px X20px
paddle_a.color('yellow')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Adding Paddle B


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('red')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)



#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1


#Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color('lightblue')
pen.penup()
pen.hideturtle()    #we don't want to see the pen
pen.goto(0,260)

# Test Variable

game = True





#Functions

def paddle_a_up():
    y = paddle_a.ycor() # Returns y-coordinate
    y +=20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)


#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,'w')  #Call paddle_a_up() if 'w' is pressed
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')


#Main Game Loop
while game:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #Border Checking
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        os.system('aplay bounce.wav&')
    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        os.system('aplay bounce.wav&')

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a,score_b),align='center',font=('Courier',24,'normal'))
        os.system('aplay point.wav&')
        if score_a == 10:
            pen.write('Player A Wins!')
            game = False
    
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a,score_b),align='center',font=('Courier',24,'normal'))
        os.system('aplay point.wav&')
        if score_b == 10:
            pen.write('Player B Wins!')
            game = False
    
    #Paddle and ball Collisions

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
        os.system('aplay bounce.wav&')

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *=-1
        os.system('aplay bounce.wav&')
