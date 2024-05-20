from turtle import Turtle

class Life(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.life = 3
        self.update_life()

    def update_life(self):
        self.clear()
        self.goto(200, 200)
        self.write(f"Life: {self.life}", align="center", font=("Courier", 40, "normal"))
    

    def point(self):
        self.life -= 1
        self.update_life()

  