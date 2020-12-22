import turtle

leo = turtle.Turtle()

print(leo)

scrn = turtle.Screen()

# change leo's shape to turtle
leo.shape('turtle')

# change pen color
leo.pencolor('seaGreen')

# put pen on canvas
leo.pendown()

# change color of turtle and pen
leo.color('Red')


# draw a square
leo.fd(100)
leo.left(90)
leo.fd(100)
leo.left(90)
leo.fd(100)
leo.left(90)
leo.fd(100)

#exite mainloop on click
scrn.exitonclick()

