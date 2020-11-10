import turtle

wn = turtle.Screen()
wn.title("Pong by ya boi senpai shadow!!!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# paddle b
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -0.5
ball.dy = 0.5

# function
def paddle_up():
    y = paddle.ycor()
    y += 30
    paddle.sety(y)
def paddle_down():
    y_neg = paddle.ycor()
    y_neg -= 30
    paddle.sety(y_neg)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_up, "w")
wn.onkeypress(paddle_down, "s")

# Main game loop
while True:
    wn.update()

    # ball moves
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    # paddle collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle.ycor() + 50 and ball.ycor() > paddle.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
