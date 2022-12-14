# Import the Class
from turtle import Screen
from paddle import Paddle
from blocks import Block
from ball import Ball
from scoreboard import ScoreBoard


game_is_on = True
index = 1

# Screen Initialisation
screen = Screen()
screen.tracer(0)

screen.setup(width=1000, height=800)
screen.bgpic("images/bg.gif")
screen.bgcolor("black")
screen.title("Breakout")

# Add new image as turtle shape for lives
screen.register_shape("images/life.gif")

# Games Object Initialisation
paddle = Paddle()
ball = Ball()
block = Block()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(paddle.move_right, "d")
screen.onkey(paddle.move_left, "a")


# Create function to draw the line
def create_line(step):

    for _ in range(step):
        block.create_line()
        block.create_blocks()


create_line(1)

# Draw the score and lives on screen
scoreboard.write_score()
scoreboard.draw_life(3, "images/life.gif")
screen.update()

# Start Game
while game_is_on:
    ball.move()

    # Check if the ball hit a block
    for blocks in block.all_blocks:
        if blocks.distance(ball) < 30:
            ball.bounce_y()
            paddle.step *= 1.005
            blocks.hideturtle()
            block.all_blocks.remove(blocks)
            scoreboard.increase_score()

    # Check if the ball pass over the x edges
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    # Check if the ball pass over the up y edge
    if ball.ycor() > 380:
        ball.bounce_y()

    # Check if the ball collision the paddle
    if ball.ycor() < -350 and ball.distance(paddle) < 100:
        ball.bounce_y()

    # Check if the ball pass over bottom Y edge - decrease a life. Start again from home initial position.
    if ball.ycor() < -380:
        paddle.home()
        ball.home()
        scoreboard.decrease_life()

        # Check if the player spend all lives
        if scoreboard.number_lives == 0:
            game_is_on = False
            scoreboard.game_over()

    screen.update()

    # Check if the player destroy all blocks. Next Level
    if not block.all_blocks:
        index += 1
        paddle.home()
        ball.home()
        create_line(index)


screen.exitonclick()
