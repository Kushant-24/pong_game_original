import turtle
import time
screen = turtle.Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game by ks.negi")
screen.tracer(0)
screen.listen()

# --------------------Paddles--------------------
l_pad = turtle.Turtle("square")
l_pad.shapesize(stretch_len=1,stretch_wid=5)
l_pad.color("white")
l_pad.penup()
l_pad.goto((-350,0))

r_pad = turtle.Turtle("square")
r_pad.shapesize(stretch_len=1,stretch_wid=5)
r_pad.color("white")
r_pad.penup()
r_pad.goto((350,0))

#-------------------Ball-------------------
ball = turtle.Turtle("circle")
ball.color("red")
ball.penup()



# Function for paddles moving.
def l_up():
    new_y = l_pad.ycor() + 40
    l_pad.sety(new_y)
def l_down():
    new_y = l_pad.ycor() - 40
    l_pad.sety(new_y)
def r_up():
    new_y = r_pad.ycor() + 40
    r_pad.sety(new_y)
def r_down():
    new_y = r_pad.ycor() - 40
    r_pad.sety(new_y)

#--------------------Ball Movement--------------------
def move():
        new_x = ball.xcor() + x_cord
        new_y = ball.ycor() + y_cord
        ball.goto((new_x,new_y))

#--------------------Score Board--------------------
def scoreboard():
    score.clear()
    score.hideturtle()
    score.penup()
    score.color("white")
    score.goto((0,280))
    score.write(f"Player 1: {l_score}    Player 2: {r_score}",move=False,align="Center",font=("Arial",15,"normal"))


#--------------------Control Keys--------------------
screen.onkey(l_up,"w")
screen.onkey(l_down,"s")
screen.onkey(r_up,"Up")
screen.onkey(r_down,"Down")

is_on = True
x_cord = 2
y_cord = 2
l_score = 0
r_score = 0
change_time = 0.01

#-------------------Score-------------------
score = turtle.Turtle()
score.hideturtle()
score.penup()
score.color("white")
score.goto((0,280))
score.write(f"Player 1: {l_score}    Player 2: {r_score}",move=False,align="Center",font=("Arial",15,"normal"))


#--------------------Main loop--------------------
while is_on:
    time.sleep(change_time)
    screen.update()
    move()
    if ball.ycor() > 290 or ball.ycor() <-290:
        y_cord *= -1
    if (ball.distance(l_pad) < 55 and ball.xcor() < -330 and ball.xcor() > -333) or (ball.distance(r_pad) < 50 and ball.xcor()>330 and ball.xcor() < 333):
        change_time -= 0.0002
        x_cord *= -1
    if (ball.distance(l_pad) < 60 and ball.distance(l_pad)>55)  or (ball.distance(r_pad) < 60 and ball.distance(r_pad) > 55):
        new_direction = 180 - ball.heading()
        ball.setheading(new_direction)
    if ball.xcor() > 410:
        r_score += 1
        scoreboard()
        ball.home()
        change_time = 0.006
    if ball.xcor() < -410:
        l_score += 1
        scoreboard()
        ball.home()
        change_time = 0.006
    if l_score == 10 or r_score == 10:
        is_on = False
        score.clear()
        score.hideturtle()
        score.penup()
        score.color("white")
        score.goto(0,0)
        if l_score == 10:
            score.write(f"Player 1 Wins!",move=False,align="Center",font=("Arial",15,"normal"))
        else:
            score.write(f"Player 2 Wins!",move=False,align="Center",font=("Arial",15,"normal"))
screen.exitonclick()