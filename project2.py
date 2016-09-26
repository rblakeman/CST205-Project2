# CST 205
# Project2.py
# github.com/rblakeman/CST205-Project2
import PIL, sys
from PIL import Image, ImageFilter, ImageFont, ImageDraw

#definitions
originalImage = Image
red = 0
green = 0
blue = 0
firstpart = "string1"
secondpart = "string2"
thirdpart = "string3"
fourthpart = "string4"

#open original image
try:
    originalImage = Image.open("pic.png")
except:
     print ("Failed to load")

#create new image to copy the original into too
newImage = Image.new("RGB", originalImage.size, (0,0,0))
newImagedata = newImage.load()
pictureWidth = originalImage.size[0]
pictureHeight = originalImage.size[1]
rgb_og = originalImage.convert('RGB') # conversion error check
for x in range(0,pictureWidth):
    for y in range(0, pictureHeight):
        red, green, blue = rgb_og.getpixel((x,y))
        newImagedata[x,y] = (red, green, blue)

#meme it
font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
draw = ImageDraw.Draw(newImage)
text = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27"
lineCount = 1
textWidth, textHeight = font.getsize(text)# gets the width and height of the text macro font
if textWidth > pictureWidth:
    if textWidth / pictureWidth > 1:       # 2 lines of text
        firstpart, secondpart = text[:int(len(text)/2)], text[int(len(text)/2):]
        lineCount = 2
    elif textWidth / 2*pictureWidth > 1:     # 3 lines of text
        firstpart, secondpart, thirdpart = string[:len(text)/3], string[len(text)/3], string[len(text)/3:]
        lineCount = 3
    elif textWidth / 3*pictureWidth > 1:     # 4 lines of text
        lineCount = 4
    else:
        print ("Error: Text is too long")
        sys.exit()

for j in range(0,lineCount):
    if (lineCount > 1):
        if j == 0:
            textWidth, textHeight = font.getsize(firstpart)
            text = firstpart
        elif j == 1:
            textWidth, textHeight = font.getsize(secondpart)
            text = secondpart
        elif j == 2:
            textWidth, textHeight = font.getsize(thirdpart)
            text = thirdpart
        elif j == 3:
            textWidth, textHeight = font.getsize(fifthhpart)
            text = fourthpart
        else:
            print ("Error in linecount")

    length = textWidth / len(text)      # takes the width of the line of text and divides by the number of characters
    length = length * (len(text)/2)     # takes the individual char length and multiplies it by the amount of chars on the left side
    center = pictureWidth / 2           # gets the center point of the picture width
    if j > 0:
        height = textHeight * j-1
    else:
        height = 0
    draw.text((center - length, height), text, (255,255,255), font=font)

#save it
newImage.save("meme.png")
