from turtle import Screen
import time
from scoreboard import Scoreboard

from snake import Snake
from food import Food

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()  
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key= "Up", fun = snake.up)
screen.onkey(key= "Down", fun = snake.down)
screen.onkey(key= "Left", fun = snake.left)
screen.onkey(key= "Right", fun = snake.right)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()    
    if food.distance(snake.head) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update()

    if snake.head.xcor()>280 or snake.head.ycor()>290 or snake.head.xcor()<-280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        game_on = False
    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<10:
            game_on = False
            scoreboard.game_over()
        

        


    


screen.exitonclick()

