# CST 205
# Project2.py
# github.com/rblakeman/CST205-Project2

from PIL import Image, ImageFilter, ImageFont, ImageDraw

originalImage = Image

try:
    originalImage = Image.open("pic.png")
except:
     print ("Failed to load")

newImage = Image.new("RGB", originalImage.size, (255,255,255))
newImagedata = newImage.load()

newImage.save("meme.png")
