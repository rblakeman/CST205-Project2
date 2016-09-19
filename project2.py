# CST 205
# Project2.py
# github.com/rblakeman/CST205-Project2
import PIL
from PIL import Image, ImageFilter, ImageFont, ImageDraw

#definitions
originalImage = Image
red = 0
green = 0
blue = 0

#open original image
try:
    originalImage = Image.open("pic2.jpg")
except:
     print ("Failed to load")

#create new image to copy the original into too
newImage = Image.new("RGB", originalImage.size, (0,0,0))
newImagedata = newImage.load()
pictureWidth = originalImage.size[0]
pictureHeight = originalImage.size[1]
for x in range(0,pictureWidth):
    for y in range(0, pictureHeight):
        rgb_og = originalImage.convert('RGB')
        red, green, blue = rgb_og.getpixel((x,y))
        newImagedata[x,y] = (red, green, blue)

#meme it
font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
draw = ImageDraw.Draw(newImage)

text = "Test Meme"
length = len(text) / 2
center = pictureWidth / 2
draw.text((center - length,0), text, (255,255,255), font=font)

#save it
newImage.save("meme.png")
