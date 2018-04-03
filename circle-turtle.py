from turtle import Turtle, Screen

def draw_square(my_turtle):
    
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)

def draw_art():

    # Turtle Brad
    brad = Turtle(shape="turtle")
    brad.color("yellow")
    brad.pensize(1.5)
    brad.speed("normal")  
    for _ in range(36):
        draw_square(brad)
        brad.right(10)
window = Screen()
window.bgcolor("black")

draw_art()

window.exitonclick()