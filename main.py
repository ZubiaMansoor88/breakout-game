from turtle import Screen, Turtle
from tkinter import messagebox, Tk
from paddle import Paddle
from ball_speed import Ball
from blocks import Blocks
from life import Life
from time_track import TimeTrack

# TODO: DESIGN SCREEN
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

# TODO: PADDLE MOVEMENT
paddle = Paddle((0, -250))
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

# TODO: BALL MOVEMENT
ball = Ball()

#TODO: BLOCKS
blocks = Blocks()
blocks.create_block()

# TODO: TIME AND LIFE TRACKING
life = Life()
time_track = TimeTrack()

# TODO: START GAME
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time_track.update_timer()

    # Detect collision with block
    for block in blocks.total_blocks:
        if block.ycor() - 19 <= ball.ycor() <= block.ycor() + 19 and block.xcor() - 55 <= ball.xcor() <= block.xcor() + 55:
            ball.bounce_y()
            blocks.delete_block(block)

    # Detect collision with wall
    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()
    if ball.ycor() > 270:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() > 220 or ball.distance(paddle) < 50 and ball.ycor() < -220:
        ball.bounce_y()
        
    # Detect paddle misses
    if ball.ycor() < -280:
        ball.reset_position()
        life.point()

    # Game Over
    if blocks.blocks_count == 10:
        game_is_on = False
        print("Game over! You Win")
        messagebox.showinfo("Game Over", f"Congratulations! You cleared all bricks in {time_track.update_timer():.2f} seconds")

    if life.life == 0:
        game_is_on = False
        print("Game over! You Lose")
        blocks_remain = 10 - blocks.blocks_count
        messagebox.showinfo("Game Over", f"You Lose! You did not cleared {blocks_remain} blocks")

screen.exitonclick()
