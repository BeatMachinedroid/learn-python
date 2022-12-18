from turtle import Screen, Turtle

# Create a new turtle and a screen
t = Turtle()
screen = Screen()

# Load the image using the Image module
from PIL import Image
img = Image.open("download.jpeg")

# Define a function to draw a pixel at the current turtle position
def draw_pixel(r, g, b):
    # Set the turtle's color to the RGB values of the pixel
    t.color((r/255, g/255, b/255))
    # Draw a filled square at the current turtle position
    t.begin_fill()
    for i in range(4):
        t.forward(1)
        t.left(90)
    t.end_fill()
    # Move the turtle one pixel to the right
    t.forward(1)

# Define a function to draw a row of pixels at the current turtle position
def draw_row(row):
    for r, g, b in row:
        draw_pixel(r, g, b)

# Define a function to draw the image at the current turtle position
def draw_image(img):
    # Iterate over the rows of the image
    for y in range(img.size[1]):
        # Move the turtle to the start of the current row
        t.penup()
        t.goto(-img.size[0]//2, img.size[1]//2 - y)
        t.pendown()
        # Get the pixels in the current row
        row = img.getdata(0, y, img.size[0], 1)
        # Draw the row of pixels
        draw_row(row)

# Draw the image
draw_image(img)

# Hide the turtle and keep the screen open
t.hideturtle()
screen.mainloop()
