# Turtle - kreska i kolor 

import turtle
t= turtle.Turtle()
# x to the right
# y is going up 
# moving turtle 
t.pensize(10) # pen thinckness
t.color("red")
t.goto(0,100) # x, y
t.goto(0,0)

t.color("green")
t.goto(100, 0)
t.goto(0,0)

t.color("blue")
t.goto(0, -100)
t.goto(0,0)

t.color("yellow")
t.goto(-100,0)
t.goto(0,0)
turtle.mainloop()

# Funkcja goTo(x,y) w wygodny sposob przesuwa zółwia w ukladzie współrzednych gdzie pocątkowym punktem jest 0,0 na osi x i y w centrum ekranu horyontalnie i wertykalnie 

#pensize(width) - zmienia grubosc lini

#color() - zmienia kolor