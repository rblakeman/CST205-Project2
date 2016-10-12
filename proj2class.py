# CST 205
# Project2.py
# github.com/rblakeman/CST205-Project2
import PIL, sys, os, textwrap
from PIL import Image, ImageFilter, ImageFont, ImageDraw
from os import walk

class proj2:
    #definitions
    location = "pic2.jpg"
    originalImage = PIL.Image
    newImage = Image
    red = 0
    green = 0
    blue = 0
    text = "text"
    firstpart = "string1"
    secondpart = "string2"
    thirdpart = "string3"
    fourthpart = "string4"
    temp = "list"
    f = []
    rootDir='.'
    pictureWidth = 0
    pictureHeight = 0

    def __init__(self):
        for dirName, subdirList, fileList in os.walk(proj2.rootDir):
           print("found directory: %s" % dirName)
           for fname in fileList:
               print("\t%s" % fname)

    def loadImage(self):
        # open original image
        try:
            proj2.originalImage = Image.open(proj2.location)
        except:
            print("Failed to load")

        #create new image to copy the original into too
        proj2.newImage = PIL.Image.new("RGB", proj2.originalImage.size, (0,0,0))
        newImagedata = proj2.newImage.load()
        proj2.pictureWidth = proj2.originalImage.size[0]
        proj2.pictureHeight = proj2.originalImage.size[1]
        rgb_og = proj2.originalImage.convert('RGB') # conversion error check
        for x in range(0,proj2.pictureWidth):
            for y in range(0, proj2.pictureHeight):
                red, green, blue = rgb_og.getpixel((x,y))
                newImagedata[x,y] = (red, green, blue)

    def mysetText(self):
        proj2.text = str(input('Enter meme text: '))

    def setText(self, str):
        proj2.text = str

    def getImg(self):
        return proj2.newImage
    # pic names: pic2.png
    # meme text copypaste: This works for one and two and three lines of text but what about four lines of text?????????????????????????????
    def drawText(self):
        #meme it
        font = PIL.ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
        draw = PIL.ImageDraw.Draw(proj2.newImage)
        lineCount = 1
        textWidth, textHeight = font.getsize(proj2.text)# gets the width and height of the text macro font
        if textWidth > proj2.pictureWidth:
            if textWidth / proj2.pictureWidth > 1 and textWidth / proj2.pictureWidth < 2:       # 2 lines of text
                lineCount = 2
                print ("2 lines of text")
                #firstpart, secondpart = text[:int(len(text)/2)], text[int(len(text)/2):]
                nth = (len(proj2.text) / 2) + 1
                temp = textwrap.wrap(proj2.text, nth)
                print (temp)
                #print len(temp[0])
                #print len(temp[1])
                proj2.firstpart = temp[0]
                proj2.secondpart = temp[1]

            elif textWidth / proj2.pictureWidth >= 2 and textWidth / proj2.pictureWidth < 3:     # 3 lines of text
                lineCount = 3
                print ("3 lines of text")
                nth = (len(proj2.text) / 3) + 1
                temp = textwrap.wrap(proj2.text, nth)
                print (temp)
                #print len(temp[0])
                #print len(temp[1])
                #print len(temp[2])
                proj2.firstpart = temp[0]
                proj2.secondpart = temp[1]
                proj2.thirdpart = temp[2]

            elif textWidth / proj2.pictureWidth >= 3 and textWidth / proj2.pictureWidth < 4:     # 4 lines of text
                lineCount = 4
                print ("4 lines of text")
                nth = len(proj2.text) / 4 + 1
                temp = textwrap.wrap(proj2.text, nth)
                print(temp)
                #print len(temp[0])
                #print len(temp[1])
                #print len(temp[2])
                #print len(temp[3])
                proj2.firstpart = temp[0]
                proj2.secondpart = temp[1]
                proj2.thirdpart = temp[2]
                proj2.fourthpart = temp[3]

            elif textWidth / proj2.pictureWidth >= 4:    # passed max
                print ("Error: Text is too long")
                sys.exit()
        else:
            print("1 line of text")

        for j in range(0,lineCount):
            if (lineCount > 1):
                if j == 0:
                    proj2.textWidth, proj2.textHeight = font.getsize(proj2.firstpart)
                    proj2.text = proj2.firstpart
                elif j == 1:
                    proj2.textWidth, proj2.textHeight = font.getsize(proj2.secondpart)
                    proj2.text = proj2.secondpart
                elif j == 2:
                    proj2.textWidth, proj2.textHeight = font.getsize(proj2.thirdpart)
                    proj2.text = proj2.thirdpart
                elif j == 3:
                    proj2.textWidth, proj2.textHeight = font.getsize(proj2.fourthpart)
                    proj2.text = proj2.fourthpart
                else:
                    print ("Error in linecount")

            length = textWidth / len(proj2.text)      # takes the width of the line of text and divides by the number of characters
            length = length * (len(proj2.text)/2)     # takes the individual char length and multiplies it by the amount of chars on the left side
            center = proj2.pictureWidth / 2           # gets the center point of the picture width
            if j > 0:
                height = proj2.textHeight * j-1
            else:
                height = 0
            draw.text((center - length, height), proj2.text, (255,255,255), font=font)

    #save it
    def saveNewImage(self):
        try:
          proj2.newImage.save("meme.png")
        except:
            print("Failed to save")

    #Getters and Setters
    def getImagePreview(self):
        return proj2.newImage, proj2.pictureHeight, proj2.pictureWidth

#p2 = proj2()
#p2.loadImage()
#p2.mysetText()
#p2.drawText()
#p2.saveNewImage()