import imp
import time
from turtle import Turtle,Screen
from turtle import Turtle,Screen, pos
up=90
down=270
left=180
right=0
class Snake:
    ss=Screen()
    
    def __init__(self,ss):
        self.ss=ss
        pass
    starting_position=[(0,0),(-20,0),(-40,0)]
    segments=[]
    for i in starting_position:
        new_segment=Turtle()
        new_segment.color("white")
        new_segment.penup()
        new_segment.shape("square")
        new_segment.goto(i)
        segments.append(new_segment)

    def forw(self):
        
        for i in range(len(self.segments)-1,0,-1):
            new_p_x=self.segments[i-1].xcor()
            new_p_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_p_x,new_p_y)
        self.segments[0].forward(20)
    
    def left(self):
        if self.segments[0].heading != left:
            self.segments[0].setheading(left)
        self.forw()
        
        

    def right(self):
        if self.segments[0].heading !=right:
            self.segments[0].setheading(right)
            self.forw()
        
    
    def up(self):
        if self.segments[0].heading != up:
            self.segments[0].setheading(up)
            self.forw()
        

    def down(self):
        if self.segments[0].heading !=down:
            self.segments[0].setheading(down)
            self.forw()
    
    def add_segment(self):
        new_segment=Turtle()
        new_segment.color("white")
        new_segment.penup()
        new_segment.shape("square")
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
        
        
        
        
    


