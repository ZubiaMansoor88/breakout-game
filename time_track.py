from turtle import Turtle
import time

class TimeTrack(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.start_time = time.time()
        self.update_timer()

    def start_time_taken(self):
        self.start_time = time.time()

    def time_taken(self):
        self.end_time = time.time()
        self.total_time = self.end_time - self.start_time


    def update_timer(self):
        self.elapsed_time = time.time() - self.start_time
        self.clear()
        self.goto(-200, 200)
        self.write(f"Time: {self.elapsed_time:.2f}", align="center", font=("Courier", 40, "normal"))
        return self.elapsed_time
    