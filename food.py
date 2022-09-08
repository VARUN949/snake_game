from turtle import Turtle, circle
import random
class Food:
    food=Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    food.shapesize(0.5,0.5)
    food.hideturtle()
    food.goto(random.randint(-280,280),random.randint(-280,280))
    food.showturtle()
    def new_position(self):
        x_position=random.randint(-280,280)
        y_position=random.randint(-280,280)
        self.food.goto(x_position,y_position)


