
import imp
from turtle import Turtle,Screen, delay
import time
from snake import Snake
from food import Food
import score



game_in=True

ss=Screen()
ss.tracer(0)
ss.bgcolor("black")
ss.setup(600,600)
ss.title("snake game")

ff=Food() 
snak=Snake(ss)
ss.listen()
scor=score.Score()

while game_in:
    ss.update()
    time.sleep(0.1)
    snak.forw()
    ss.onkey(key="Left",fun=snak.left)
    ss.onkey(key="Right",fun=snak.right)
    ss.onkey(key="Up",fun=snak.up)
    ss.onkey(key="Down",fun=snak.down)
    ss.onkey(key="a",fun=ff.new_position)
    if snak.segments[0].distance(ff.food)<15:
        ff.new_position() 
        print("okay")
        scor.score_incre()
        snak.add_segment()
    if snak.segments[0].xcor()>300 or snak.segments[0].ycor()>300 or snak.segments[0].xcor()<-300 or snak.segments[0].ycor()<-300:
        game_in=False

    for seg in snak.segments:
        if seg==snak.segments[1]:
            pass
        elif snak.segments[1].distance(seg)<15:
            game_in=False

print(scor.score())

    
ss.exitonclick()