from turtle import Turtle, Screen, color, position

POSITION = [(0,0), (-20,0), (-40,0)]
DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] 
        

    def create_snake(self):
        for p in POSITION:
            self.add_segment(p)
        
    
    def add_segment(self, p):
        
        sq = Turtle("square")
        sq.color("white")
        sq.penup()
        sq.goto(p)
        self.segments.append(sq)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        
        for seg_num in range(len(self.segments)-1 , 0, -1):
            newx = self.segments[seg_num-1].xcor()
            newy = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(newx, newy)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    # def inc_speed(self):
    #     self.s

    
