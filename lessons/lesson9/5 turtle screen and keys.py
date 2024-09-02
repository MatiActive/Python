import turtle
import time

t = turtle.Turtle()

win = turtle.Screen()

win.title("application")

win.bgcolor("yellow")
win.setup(width=550, height=550)

t.forward(100)
print("x",t.xcor())
print("y",t.ycor())

def keyPressedw():
    print("w clicked")
    t.fd(20)
def keyPresseds():
    print("s clicked")
    t.bk(20)
def keyPresseda():
    print("a clicked")
    t.lt(20)
def keyPressedd():
    print("d clicked")
    t.rt(20)
win.listen()
win.onkey(keyPressedw,"w")
win.onkey(keyPresseds,"s")
win.onkey(keyPresseda,"a")
win.onkey(keyPressedd,"d")

win.tracer(0)

while True:
    win.update()
    time.sleep(0.1)

win.mainloop()