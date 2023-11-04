from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars=[]
        self.move_speed=STARTING_MOVE_DISTANCE

    def add_car(self):
        car=Turtle("square")
        car.shapesize(stretch_wid=1,stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        random_y=random.randint(-250,250)
        car.goto(300,random_y)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_speed)

    def increase_speed(self):
        self.move_speed+=MOVE_INCREMENT

