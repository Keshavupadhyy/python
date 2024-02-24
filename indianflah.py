import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Indian Flag")
screen.setup(width=900, height=600)

# Set the background color to white
screen.bgcolor("white")

# Create a turtle object
flag_turtle = turtle.Turtle()
flag_turtle.speed(2)

# Function to draw a rectangle with specified color
def draw_rectangle(color, width, height):
    flag_turtle.begin_fill()
    flag_turtle.fillcolor(color)
    for _ in range(2):
        flag_turtle.forward(width)
        flag_turtle.right(90)
        flag_turtle.forward(height)
        flag_turtle.right(90)
    flag_turtle.end_fill()

# Function to draw a star
def draw_star(x, y, color, size):
    flag_turtle.penup()
    flag_turtle.goto(x, y)
    flag_turtle.pendown()
    flag_turtle.begin_fill()
    flag_turtle.fillcolor(color)
    for _ in range(5):
        flag_turtle.forward(size)
        flag_turtle.right(144)
    flag_turtle.end_fill()

# Draw the green rectangle for the bottom part of the flag
draw_rectangle("#138808", 900, 200)

# Draw the white rectangle for the middle part of the flag
draw_rectangle("white", 900, 200)

# Draw the saffron rectangle for the top part of the flag
draw_rectangle("#FF9933", 900, 200)

# Draw the navy blue Ashoka Chakra
flag_turtle.penup()
flag_turtle.goto(-50, 50)
flag_turtle.pendown()
flag_turtle.circle(45, 360)

# Draw 24 spikes of the Ashoka Chakra
for _ in range(24):
    flag_turtle.penup()
    flag_turtle.goto(flag_turtle.xcor(), flag_turtle.ycor())
    flag_turtle.pendown()
    flag_turtle.forward(50)
    flag_turtle.backward(50)
    flag_turtle.right(15)

# Display the flag
turtle.done()
