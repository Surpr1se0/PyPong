import turtle
import os

window = turtle.Screen()
window.title("Pong by @surprise")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # stop the window updating

# Menu

menu = turtle.Turtle()
menu.speed(0)
menu.color("white")

# Creating Menu option buttons
def button(length):
    for i in range(4):
        menu.forward(length)
        menu.left(90)


def column(n, length):
    menu.left(270)
    for i in range(n):
        button(length)
        menu.forward(length)
    menu.penup()
    menu.left(90)
    menu.forward(n * length)
    menu.left(180)
    menu.pendown()

column(5, 100)

def btnclick(x,y):
    if 0 < x < 101 and 0 > y > -101:
        print("Start Game")
        print(x, y)
        turtle.clearscreen()
    elif 0 < x < 101 and -101 > y > -201:
        print("Rules")
        print(x, y)
        turtle.clearscreen()
    elif 0 < x < 101 and -201 > y > -301:
        print("Highscore")
        print(x, y)
        turtle.clearscreen()
    elif 0 < x < 101 and -301 > y > -401:
        print("Hi")
        print(x, y)
        turtle.clearscreen()
    elif 0 < x < 101 and -401 > y > -501:
        print("Hi")
        print(x, y)
        turtle.clearscreen()
    elif 0 < x < 101 and -501 > y > -601:
        print("Hi")
        print(x, y)
        turtle.clearscreen()
    else:
        print("Click One Of The Options!")
        print(x, y)
        btnclick(x, y)
turtle.onscreenclick(btnclick, 1)
turtle.listen()

turtle.done()


# Menu Options
menu.penup()
menu.goto(8, -46)
menu.write("START GAME!", font=("Arial", 12, "normal"))

menu.penup()
menu.goto(6, -145)
menu.write("RULES", font=("Arial", 12, "normal"))

menu.penup()
menu.goto(3, -248)
menu.write("HIGH SCORE", font=("Arial", 12, "normal"))

menu.penup()
menu.goto(4, -343)
menu.write("FAQ", font=("Arial", 12, "normal"))

menu.penup()
menu.goto(3, -450)
menu.write("QUIT GAME", font=("Arial", 12, "normal"))

turtle.done()

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # set the speed to the max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # set the speed to the max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # set the speed to the max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.025  # 1 px at a time
ball.dy = 0.025

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Funcs

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard
window.listen()

window.onkey(paddle_a_up, "w")  # Listening for inputs Player 1
window.onkey(paddle_a_down, "s")

window.onkey(paddle_b_up, "Up")  # Listening for inputs Player 2
window.onkey(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")  # & at the end to stop the delay

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle Bounce
    if 340 < ball.xcor() < 350 and (
            paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if -340 > ball.xcor() > -350 and (
            paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
