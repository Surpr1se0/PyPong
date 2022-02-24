import turtle
import os

window = turtle.Screen()
window.title("Pong by @surprise")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # stop the window updating

# Score
score_a = 0;
score_b = 0;

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
        pen.write("Player A: {}  Player B: {}" .format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}" .format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle Bounce
    if ball.xcor() > 340 and ball.xcor() < 350 and (
            ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() < -340 and ball.xcor() > -350 and (
            ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
