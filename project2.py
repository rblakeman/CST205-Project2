# CST 205
# Project2.py
# github.com/rblakeman/CST205-Project2
import PIL, sys, textwrap
from PIL import Image, ImageFilter, ImageFont, ImageDraw

#definitions
location = "pic.png"
originalImage = Image
red = 0
green = 0
blue = 0
text = "text"
firstpart = "string1"
secondpart = "string2"
thirdpart = "string3"
fourthpart = "string4"
temp = "list"

location = str(input('Enter picture name: '))
#open original image
try:
    originalImage = Image.open(location)
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

# pic names: pic2.png
# meme text copypaste: This works for one and two and three lines of text but what about four lines of text?????????????????????????????

#meme it
font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
draw = ImageDraw.Draw(newImage)
text = str(input('Enter meme text: '))
lineCount = 1
textWidth, textHeight = font.getsize(text)# gets the width and height of the text macro font
if textWidth > pictureWidth:
    if textWidth / pictureWidth > 1 and textWidth / pictureWidth < 2:       # 2 lines of text
        lineCount = 2
        print ("2 lines of text")
        #firstpart, secondpart = text[:int(len(text)/2)], text[int(len(text)/2):]
        nth = (len(text) / 2) + 1
        temp = textwrap.wrap(text, nth)
        print (temp)
        #print len(temp[0])
        #print len(temp[1])
        firstpart = temp[0]
        secondpart = temp[1]

    elif textWidth / pictureWidth >= 2 and textWidth / pictureWidth < 3:     # 3 lines of text
        lineCount = 3
        print ("3 lines of text")
        nth = (len(text) / 3) + 1
        temp = textwrap.wrap(text, nth)
        print (temp)
        #print len(temp[0])
        #print len(temp[1])
        #print len(temp[2])
        firstpart = temp[0]
        secondpart = temp[1]
        thirdpart = temp[2]

    elif textWidth / pictureWidth >= 3 and textWidth / pictureWidth < 4:     # 4 lines of text
        lineCount = 4
        print ("4 lines of text")
        nth = len(text) / 4 + 1
        temp = textwrap.wrap(text, nth)
        print(temp)
        #print len(temp[0])
        #print len(temp[1])
        #print len(temp[2])
        #print len(temp[3])
        firstpart = temp[0]
        secondpart = temp[1]
        thirdpart = temp[2]
        fourthpart = temp[3]

    elif textWidth / pictureWidth >= 4:    # passed max
        print ("Error: Text is too long")
        sys.exit()
else:
    print("1 line of text")

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
            textWidth, textHeight = font.getsize(fourthpart)
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
