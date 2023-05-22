from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_ycoordinate = self.ycor() + 40
        self.goto(self.xcor(), new_ycoordinate)

    def go_down(self):
        new_ycoordinate = self.ycor() - 40
        self.goto(self.xcor(), new_ycoordinate)


