from turtle import Turtle, position
STARTING_POINTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# values for heading()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    #create a 3 segment snake to start
    def create_snake(self):
        for pos in STARTING_POINTS:
            self.add_segment(pos)
    # creat anew segment and add it to the snake
    def add_segment(self, position):
        seg = Turtle(shape='square')
        seg.color('white')
        seg.penup()
        seg.setpos(position)
        self.segments.append(seg)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        # start at end of list decrementing by -1 until reaching 0.
        # For loop tells each segment to go to the position of the segment in front of it
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            # make last seg goto position of 2nd to last
            self.segments[seg_number].goto(new_x, new_y)

            # move first segment forwards, so other segs will follow on next iteration
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
        	self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
        	self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
