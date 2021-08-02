#PONG HOCKEY EDITION
#By: Carson Milne, Pablo Rizzi-Benavides and Cameron Cockrall

from pylsl import StreamInlet, resolve_stream
import turtle

#Set up the game screen
game = turtle.Screen()

game.bgcolor("white")
game.title("PONG: Hockey Edition")

game.setup(width=900, height=500)
game.tracer(0)

#Establish score variables
redscore = 0
bluescore = 0


# GAME OBJECTS --------------------------------------------------------------------------------
#pongtext
pong = turtle.Turtle()

pong.color("black")
pong.shape("square")
pong.hideturtle()

pong.speed(0)
pong.penup()

pong.goto(0,200)

pong.write("HOCKEY", align="center", font=("Times", 30 ,"bold"))

#scoreboard
score = turtle.Turtle()

score.color("black")
score.shape("square")
score.hideturtle()

score.speed(0)
score.penup()

score.goto(0,150)
score.write("Red: 0  Blue: 0", align="center", font=("Times", 30, "bold"))

#Center Ice
Center = turtle.Turtle()

Center.color("red")
Center.shape("circle")
Center.shapesize(stretch_wid=7, stretch_len=7)


Center.speed(0)
Center.penup()

Center.goto(0,0)

#Center2 Ice

Center = turtle.Turtle()

Center.color("white")
Center.shape("circle")

Center.speed(0)
Center.penup()

Center.goto(0,0)

#Mark1 Ice
mark1 = turtle.Turtle()

mark1.color("blue")
mark1.shape("circle")
mark1.shapesize(stretch_wid=3, stretch_len=3)


mark1.speed(0)
mark1.penup()

mark1.goto(300,150)

#Mark2 Ice
mark2 = turtle.Turtle()

mark2.color("blue")
mark2.shape("circle")
mark2.shapesize(stretch_wid=3, stretch_len=3)


mark2.speed(0)
mark2.penup()

mark2.goto(300,-150)

#Mark3 Ice
mark3 = turtle.Turtle()

mark3.color("blue")
mark3.shape("circle")
mark3.shapesize(stretch_wid=3, stretch_len=3)


mark3.speed(0)
mark3.penup()

mark3.goto(-300,-150)

#Mark4 Ice
mark4 = turtle.Turtle()

mark4.color("blue")
mark4.shape("circle")
mark4.shapesize(stretch_wid=3 , stretch_len=3)


mark4.speed(0)
mark4.penup()

mark4.goto(-300,150)



#ball properties
ball = turtle.Turtle()
ball.color("black")
ball.shape("circle")

ball.speed(0)
ball.penup()

ball.goto(0, 0)

#"Speed" of ball moving

ball.dx = -10
ball.dy = -10


#red racket (left)
LR = turtle.Turtle()

LR.color("red")
LR.shape("square")
LR.shapesize(stretch_wid=5.5, stretch_len=0.5)

LR.speed(0)
LR.penup()

LR.goto(-430,0)

#blue racket (right)
RR = turtle.Turtle()

RR.shape("square")
RR.color("blue")
RR.shapesize(stretch_wid=5.5, stretch_len=0.5)

RR.speed(0)
RR.penup()

RR.goto(430, 0)



# Functions --------------------------------------------------------------------------------
def LR_up():
    vertcont = LR.ycor()
    if vertcont > 200:
         vertcont = 200
    elif vertcont < 200:
         vertcont += 40
    LR.sety(vertcont)



def LR_down():
    vertcont = LR.ycor()
    if vertcont < -200:
        vertcont = -200
    elif vertcont > -200:
        vertcont -= 40
    LR.sety(vertcont)

#controls TO BE CHANGED VIA MIND CONTROL --------------------------------------------------------------------------------

#Keyboard input
game.listen()

#Controls for red racket
game.onkeypress(LR_up, "w")
game.onkeypress(LR_down, "s")
game.onkeypress(LR_up, "W")
game.onkeypress(LR_down, "S")

#Connect to stream
print("Looking for an EEG stream...")
streams = resolve_stream('type','EEG')


#Define function to move right racket (with focus/unfocus)
def main():
    vertcont = RR.ycor()

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])
    sample= inlet.pull_sample()

    print(sample)
    #Define movements of racket
    if sample[0][0] == 0.0:
        if vertcont > -200:
            vertcont -= 40
        elif vertcont < -200:
            vertcont = 200
    else:
        if vertcont > 200:
            vertcont = -200
        elif vertcont < 200:
            vertcont += 40
    RR.sety(vertcont)

# BEGIN LOOPING GAME ---------------------------------------------------------

while True:
    main()
        
    game.update()
    
    #BALL MOVEMENT
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #CHANGE DIRECTIONS ON TOP/BOTTOM
    if ball.ycor() > 250:
        ball.dy *= -1
    elif ball.ycor() < -250:
        ball.dy *= -1



    #BALL HITTING RACKET
    if  ball.xcor() > 410 and ball.ycor() > RR.ycor() - 50 and ball.ycor() < RR.ycor() + 50:
        ball.dx *= -1
    elif ball.xcor() < -410 and ball.ycor() > LR.ycor() - 50 and  ball.ycor() < LR.ycor() + 50:
        ball.dx *= -1

    # GOALS SCORING
    if ball.xcor() > 420:

    #Add one to red score
        redscore += 1

    #Clear scoreboard and update with new score
        score.clear()
        score.write("Red: {} " "Blue: {}".format(redscore, bluescore), align="center", font=("Times", 30, "bold"))

        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -420:

    #Add one to blue score
        bluescore += 1

    #Clear scoreboard and update with new score
        score.clear()
        score.write("Red: {}  Blue: {}".format(redscore, bluescore), align="center", font=("Times", 30, "bold"))

        ball.goto(0, 0)
        ball.dx *= -1

