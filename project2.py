# CST 205
# Project2.py
# github.com/rblakeman/CST205-Project2

from PIL import Image, ImageFilter, ImageFont, ImageDraw
Image.open("C:/Users/minve/Pictures/Project2Images/aliens.jpg")
originalImage = Image

try:
    originalImage = Image.open("C:/Users/minve/Pictures/Project2Images/aliens.jpg")
except:
     print ("Failed to load")

newImage = originalImage
newImagedata = newImage.load()

newImage.show()
