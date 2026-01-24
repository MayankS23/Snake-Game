from food import Food
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.write(f"score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", font=("Ariel", 40, "normal"), align="center")