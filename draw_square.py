import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(5)
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    angie.speed(3)

    bob  = turtle.Turtle()
    bob.shape("turtle")
    bob.color("blue")
    bob.speed(2)
    bob.forward(100)
    bob.right(135)
    bob.forward(90)
    bob.right(105)
    bob.forward(80)
    
    window.exitonclick()


draw_square()

    
