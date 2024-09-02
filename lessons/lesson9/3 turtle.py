import turtle
t = turtle.Turtle()
t.pensize(10) # pen thickness
t.color("blue")

for i in range(20):
    turtle.width(i)
    turtle.forward(60 + 20 *i)
    turtle.right(90)

turtle.mainloop()

# stosujac petle moemy stworzyc bardziej skomplikowane wzory, ktore namaluje zółw wraz z animacja