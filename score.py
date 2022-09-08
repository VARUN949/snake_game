import turtle


from turtle import Turtle

class Score():
    scoree=0
    scren=Turtle()
    def __init__(self):
        self.scren.penup()
        self.scren.goto(0,270)
        self.scren.color("white")
        self.scren.hideturtle()
        self.scren.write(f"score is: {self.scoree}",align="center",font=('Arial', 24, 'normal'))

    
    # scren.shape("none")
    
    def score_incre(self):
        self.scoree=1+self.scoree
        self.scren.clear()
        self.scren.write(f"score is: {self.scoree}",align="center",font=('Arial', 24, 'normal'))

    def score(self):
        return self.scoree