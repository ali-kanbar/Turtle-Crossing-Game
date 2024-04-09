from turtle import Turtle,Screen
from random import randint
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
COLORS = ["red", "blue", "green", "yellow", "pink", "black", "orange", "purple", "brown", "gray", "cyan", "magenta", "lime", "teal", "lavender", "maroon", "navy", "olive", "silver", "gold"]
Level_1_SPEED = 3
Level_2_SPEED = 2
Level_3_SPEED = 1
SLEEP = 0.1
LEVEL_1,LEVEL_2,LEVEL_3 = True,False,False
CAR_COUNT = 20
COUNT = Level_1_SPEED
FONT = ("Courier", 30, "normal")

class Car():
    def __init__(self):
        self.cars = []
        self.fill(CAR_COUNT)
    
    def fill(self,COUNT):
        for _ in range(COUNT):
            t = Turtle("square")
            t.color(COLORS[randint(0,len(COLORS)-1)])
            t.shapesize(1.5,3.5)
            t.penup()
            t.goto(randint(-SCREEN_WIDTH//2,SCREEN_WIDTH//2),randint(-(SCREEN_HEIGHT//2-120),(SCREEN_HEIGHT//2-200)))
            self.cars += [t]
            
    def move_car(self):
        for t in self.cars:
            t.bk(10)
            
    def create_car(self):
        t = Turtle("square")
        t.color(COLORS[randint(0,len(COLORS)-1)])
        t.shapesize(1.5,3.5)
        t.penup()
        t.goto(SCREEN_WIDTH//2,randint(-(SCREEN_HEIGHT//2-75),(SCREEN_WIDTH//2-200)))
        self.cars += [t]
        
    def delete(self):
       for car in self.cars:
           car.hideturtle()
       self.cars.clear()
           
    def detect_collision(self, turtle):
        for car in self.cars:
            if car.distance(turtle) <= 30:
                return True
        return False


def move():
    screen.update()
    my_turtle.fd(20)
 
def level_up():
    global LEVEL_1,LEVEL_2,LEVEL_3,COUNT,SLEEP
    SLEEP /= 2
    level.clear()
    if LEVEL_1:LEVEL_1 = False;LEVEL_2 = True;COUNT = Level_2_SPEED;level.write("Level 2",align = "left",font = FONT)
    elif LEVEL_2:LEVEL_2 = False;LEVEL_3 = True;COUNT = Level_3_SPEED;level.write("Level 3",align = "left",font = FONT)
    my_turtle.goto(0,-(SCREEN_HEIGHT//2-20))
    
screen = Screen()
screen.listen()
screen.tracer(0)
screen.title("Turtle Crossing")
screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
level = Turtle()
level.hideturtle()
level.penup()
level.goto(x = -(SCREEN_WIDTH//2 - 50), y = SCREEN_HEIGHT//2 - 60)
level.write("Level 1",align = "left",font = FONT)
my_turtle = Turtle("turtle")
my_turtle.penup()
my_turtle.speed("fastest")
my_turtle.setheading(90)
my_turtle.goto(0,-(SCREEN_HEIGHT//2-20))
screen.onkey(move,"space")
my_cars = Car()

while True:
    screen.update()
    time.sleep(SLEEP)
    
    if COUNT == Level_1_SPEED:COUNT = 0
    elif COUNT == 0:my_cars.create_car();COUNT += 1
    else:COUNT += 1
    
    if my_cars.detect_collision(my_turtle):
        screen.clear()
        level.goto(0,0)
        level.write("OOPS,you lost",align = "center",font = ("Courier",30,"normal"))
        time.sleep(1)
        quit()
    
    if my_turtle.ycor() >= (SCREEN_HEIGHT//2 - 20):
        if not LEVEL_3:
            level_up()
            my_cars.delete()
            my_cars.fill(CAR_COUNT)
        else:
            screen.clear()
            level.goto(0,0)
            level.write("Congratulations,you won",align = "center",font = ("Courier",30,"normal"))
            time.sleep(1)
            quit()
        
    my_cars.move_car()
    