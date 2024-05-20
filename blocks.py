from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
BLOCK_DISTANCE = 150
STARTING_X = -300

class Blocks():

    def __init__(self):
        super().__init__()
        self.total_blocks = []
        self.blocks_count = 0

    def create_block(self):
        new_x1 = STARTING_X 
        new_x2 = STARTING_X 
        for _ in range(0, 5):
            new_block = Turtle("square")
            new_block.penup()
            new_block.shapesize(3, 7)
            new_block.color(random.choice(COLORS))
            new_block.goto(new_x1, 170)
            new_x1 += BLOCK_DISTANCE
            self.total_blocks.append(new_block)
        for _ in range(0, 5):
            new_block = Turtle("square")
            new_block.penup()
            new_block.shapesize(3, 7)
            new_block.color(random.choice(COLORS))
            new_block.goto(new_x2, 100)
            new_x2 += BLOCK_DISTANCE
            self.total_blocks.append(new_block)

    def delete_block(self, block):
        block.clear()
        block.hideturtle()
        self.total_blocks.remove(block)
        self.blocks_count += 1


        

