import turtle

# Function to draw a rectangle with rounded corners
def draw_rounded_rectangle(width, height, radius):
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width - 2 * radius)
        turtle.circle(radius, 90)
        turtle.forward(height - 2 * radius)
        turtle.circle(radius, 90)
    turtle.end_fill()

# Function to draw the WhatsApp icon
def draw_whatsapp_icon():
    turtle.color("#25d366")  # WhatsApp green color
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()

    # Draw the main body of the icon
    draw_rounded_rectangle(100, 100, 20)

    # Draw the phone receiver
    turtle.penup()
    turtle.goto(-30, 10)
    turtle.pendown()
    turtle.circle(10)

    turtle.hideturtle()
    turtle.done()

# Set up the Turtle window
turtle.speed(2)
turtle.bgcolor("#ffffff")  # White background color

# Draw the WhatsApp icon
draw_whatsapp_icon()
