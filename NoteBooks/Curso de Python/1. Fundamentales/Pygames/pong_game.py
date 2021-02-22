import turtle


# "Hacemos la pantalla"

wn = turtle.Screen()
wn.title("Pong hecho por Miguel y Alejandro")
wn.bgcolor("black")
wn.setup(width=800, height=500)
wn.tracer(0)
print(wn)

#  Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
print(paddle_a)


#  Paddle Bb

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

input()