import turtle

def initials(r_turtle):
    frog.forward(120)
    frog.right(36)
    
def flowers(r_turtle):
    for i in range(1,41):
        frog.forward(50)
        frog.right(36)
        frog.forward(50)
        frog.right(144)
        frog.forward(50)
        frog.right(36)
        frog.forward(50)
        frog.right(153)
    frog.right(90)
    frog.forward(150)
    frog.right(90)
    frog.circle(10)
    


frog = turtle.Turtle()
frog.speed(15)
window = turtle.Screen()
flowers(frog)
window.exitonclick()
    
