from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard:

    def __init__(self):

        self.lives = []
        self.text = Turtle()
        self.score = 0
        self.number_lives = 0

    def write_score(self):
        # self.text = Turtle()
        self.text.penup()
        self.text.color("white")
        self.text.hideturtle()
        self.text.goto(-450, 360)
        self.text.write(f"Score: {self.score}", align="left", font=FONT)

    def draw_life(self, number, shape):
        self.number_lives = number
        x = 300
        y = 370

        for _ in range(number):
            live = Turtle()
            live.penup()
            live.shape(shape)
            live.goto(x, y)
            self.lives.append(live)
            x += 30

    def increase_score(self):
        self.score += 10
        self.text.clear()
        self.text.write(f"Score: {self.score}", align="left", font=FONT)

    def decrease_life(self):
        self.number_lives -= 1
        self.lives[self.number_lives].hideturtle()

    def game_over(self):
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.goto(0, 0)
        game_over.color("white")
        game_over.write(f"Game Over! Your score: {self.score}", align="center", font=FONT)




