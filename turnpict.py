from PIL import Image, ImageDraw, ImageFont

# Define the word to convert to an image
word = "Hello"

# Create a new image with a white background
img = Image.new("RGB", (200, 100), (255, 255, 255))

# Get a drawing context for the image
draw = ImageDraw.Draw(img)

# Define the font to use for the word
font = ImageFont.truetype("arial.ttf", 48)

# Draw the word on the image using the specified font and color
draw.text((20, 20), word, (0, 0, 0), font=font)

# Save the image to a file
img.save("word.png")