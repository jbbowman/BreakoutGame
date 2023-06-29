import turtle
import tkinter.messagebox

# defining paddle
class Paddle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -250)

    # paddle movement/speed left and right
    def paddle_left(self):
        x = self.xcor()
        x -= 20
        self.setx(x)
    def paddle_right(self):
        x = self.xcor()
        x += 20
        self.setx(x)

# defining brick
class Brick(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("red")
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=1)

# defining ball
class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 7.5
        self.dy = -7.5

    # defining ball movement using fixed rate defined above
    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    # handles ball bouncing off walls
    def bounce(self):
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1
        if self.xcor() > 290:
            self.setx(290)
            self.dx *= -1
        if self.xcor() < -290:
            self.setx(-290)
            self.dx *= -1
        if self.ycor() < -290:
            tkinter.messagebox.showinfo("Game Over", "Game Over")
            turtle.done()

# handles ball collision with paddle and bricks
def check_collision(ball, paddle, bricks):
    if (ball.xcor() > paddle.xcor() - 20) and (ball.xcor() < paddle.xcor() + 20) and (
            ball.ycor() < paddle.ycor() + 20) and (ball.ycor() > paddle.ycor() - 20):
        ball.dy *= -1

    for brick in bricks:
        if (ball.xcor() > brick.xcor() - 20) and (ball.xcor() < brick.xcor() + 20) and (
                ball.ycor() < brick.ycor() + 20) and (ball.ycor() > brick.ycor() - 20):
            ball.sety(brick.ycor() - 20)
            ball.dy *= -1
            brick.hideturtle()
            bricks.remove(brick)
            break

def main():
    # window instantiation
    wn = turtle.Screen()
    wn.title("Breakout Game")
    wn.bgcolor("black")
    wn.setup(width=600, height=600)

    # custom classes being instantiated
    paddle = Paddle()
    ball = Ball()
    brick_list = []

    for i in range(-220, 220, 55):
        brick = Brick(i, 250)
        brick_list.append(brick)

    # controls
    wn.listen()
    wn.onkeypress(paddle.paddle_left, "Left")
    wn.onkeypress(paddle.paddle_right, "Right")
    wn.onkeypress(quit, "Escape")

    # listener/updating
    while True:
        wn.update()
        ball.move()
        ball.bounce()
        check_collision(ball, paddle, brick_list)
        if len(brick_list) == 0:
            tkinter.messagebox.showinfo("Congratulations!", "You won!")
            turtle.done()

if __name__ == '__main__':
    main()
