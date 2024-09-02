import turtle
import time
from food import *
from snake import *


win = turtle.Screen()
win.title("snake Game")
width = 500
height = 500
win.setup(width=width, height=height)
win.bgcolor("green")

snake = Snake(0,0)
win.listen()
win.onkey(snake.keyUP, "Up")
win.onkey(snake.keyDown, "Down")
win.onkey(snake.keyLeft, "Left")
win.onkey(snake.keyRight, "Right")

win.onkey(snake.keyUP, "w")
win.onkey(snake.keyDown, "s")
win.onkey(snake.keyLeft, "a")
win.onkey(snake.keyRight, "d")

food= Food()

while True:
    win.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()

    if snake.checkSelfCollision() or snake.checkWallCollision(width,height):
        food.refresh()
        snake.refresh()
win.mainloop()