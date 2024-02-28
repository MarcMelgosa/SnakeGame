from turtle import Turtle

SCORE_POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
SCOREBOARD_COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as hs_file:
            self.high_score = int(hs_file.read())
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.goto(SCORE_POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_hs:
                new_hs.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
