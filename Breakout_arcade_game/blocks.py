from turtle import Turtle
import random


class Block:
    def __init__(self):
        self.all_blocks = []
        self.colors = ["#10A19D", "#540375", "#FF7000", "#FFBF00"]
        self.random_color = None
        self.init_x = -460
        self.init_y = 325

    def create_blocks(self):
        for _ in range(15):
            new_block = Turtle()
            new_block.shape("square")
            new_block.color(self.random_color)
            new_block.left(90)
            new_block.penup()
            new_block.shapesize(stretch_wid=3, stretch_len=1)
            new_block.goto(self.init_x, self.init_y)
            self.all_blocks.append(new_block)
            self.init_x += 65

    def create_line(self):
        self.init_y -= 25
        self.init_x = -460
        self.random_color = random.choice(self.colors)








