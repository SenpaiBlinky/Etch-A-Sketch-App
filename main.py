from turtle import Turtle, Screen
import random as r

# ------------------------------------- Etch A Sketch -----------------------------------------
# tu = Turtle()
# screen = Screen()

# def move_forward():
#     tu.forward(10)
    
# def move_backwards():
#     tu.backward(10)
    
# def turn_left():
#     tu.left(5)
    
# def turn_right():
#     tu.right(5)

# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=turn_right)

# ------------------------------------- Turtle Race -----------------------------------------

screen = Screen()
screen.setup(width=500, height=400)

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()

user_winner = screen.textinput(title="Important Question", prompt="Which turtle do you think is going to win?")

bundle_of_turtles = [t1, t2, t3, t4, t5]
turtle_colors = ["red", "blue", "green", "yellow", "purple"]

def setup(list):
    i = 0
    position = 0
    for turtle in list:
        turtle.shape("turtle")
        turtle.color(turtle_colors[i])
        turtle.penup()
        turtle.speed("fastest")
        i += 1
        turtle.goto(x=-240, y=position-60)
        position += 30

setup(bundle_of_turtles)

start_race = False

if user_winner:
    start_race = True
    
while start_race == True:
    for t in bundle_of_turtles:
        steps = r.randint(1, 10)
        t.forward(steps)
        if t.xcor() >= 230:
            start_race = False
            if user_winner == t.pencolor():
                print("yes correct")
                continue
            else:
                print("nope sorrey")
                continue
        


screen.exitonclick()