# CST 205
# Project2.py
# github.com/rblakeman/CST205-Project2
import PIL, sys, os, textwrap
from PIL import Image, ImageFilter, ImageFont, ImageDraw
from os import walk

class proj2:
    #definitions
    location = "pic.png"
    originalImage = PIL.Image
    newImage = Image
    red = 0
    green = 0
    blue = 0
    text1 = ""  #Top
    text2 = ""  #Bottom
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
        print(self.location)
        return

    def listImages(self):
        for dirName, subdirList, fileList in os.walk(self.rootDir):
           print("found directory: %s" % dirName)
           for fname in fileList:
               print("\t%s" % fname)

    def returnImagesList(self):
        str = ""
        for dirName, subdirList, fileList in os.walk(self.rootDir):
           #print("found directory: %s" % dirName)
           for fname in fileList:
               str += ("\n%s" % fname)

        return str

    def pickImage(self, imgStr):
        self.location = imgStr
        print(self.location)
        return

    def loadImage(self):
        # open original image
        print(self.location)
        try:
            self.originalImage = Image.open(self.location)
        except:
            print("Failed to load")
            return False

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
        return True

    def mysetText(self):
        proj2.text = str(input('Enter meme text: '))

    def setText(self, str1, str2):
        self.text1 = str1
        self.text2 = str2

    def getImg(self):
        return proj2.newImage

    def drawText(self):
        self.drawTextTop()
        self.drawTextBot()

    # pic names: pic2.png
    # meme text copypaste: This works for one and two and three lines of text but what about four lines of text?????????????????????????????
    def drawTextTop(self):
        font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
        draw = ImageDraw.Draw(self.newImage)
        ###################################################################################################
        lineCount = 1
        textWidth, textHeight = font.getsize(self.text1)  # gets the width and height of the text macro font
        if textWidth > self.pictureWidth:
            if textWidth / self.pictureWidth > 1 and textWidth / self.pictureWidth < 2:  # 2 lines of text
                lineCount = 2
                print("2 lines of text")
                nth = (len(self.text1) / 2) + 2
                temp = textwrap.wrap(self.text1, nth)
                print(temp)
                firstpart = temp[0]
                secondpart = temp[1]

            elif textWidth / self.pictureWidth >= 2 and textWidth / self.pictureWidth < 3:  # 3 lines of text
                lineCount = 3
                print("3 lines of text")
                nth = (len(self.text1) / 3) + 2
                temp = textwrap.wrap(self.text1, nth)
                print(temp)
                firstpart = temp[0]
                secondpart = temp[1]
                thirdpart = temp[2]

            elif textWidth / self.pictureWidth >= 3 and textWidth / self.pictureWidth < 4:  # 4 lines of text
                lineCount = 4
                print("4 lines of text")
                nth = len(self.text1) / 4 + 2
                temp = textwrap.wrap(self.text1, nth)
                print(temp)
                firstpart = temp[0]
                secondpart = temp[1]
                thirdpart = temp[2]
                fourthpart = temp[3]

            elif textWidth / self.pictureWidth >= 4:  # passed max
                print("Error: Text is too long")
                sys.exit()
        else:
            print("1 line of text")

        for j in range(0, lineCount):
            if (lineCount > 1):
                if j == 0:
                    textWidth, textHeight = font.getsize(firstpart)
                    self.text1 = firstpart
                elif j == 1:
                    textWidth, textHeight = font.getsize(secondpart)
                    self.text1 = secondpart
                elif j == 2:
                    textWidth, textHeight = font.getsize(thirdpart)
                    self.text1 = thirdpart
                elif j == 3:
                    textWidth, textHeight = font.getsize(fourthpart)
                    self.text1 = fourthpart
                else:
                    print("Error in linecount")

            length = textWidth / len(
                self.text1)  # takes the width of the line of text and divides by the number of characters
            length = length * (
            len(self.text1) / 2)  # takes the individual char length and multiplies it by the amount of chars on the left side
            center = self.pictureWidth / 2  # gets the center point of the picture width
            if j > 0:
                height = textHeight * j - 1
            else:
                height = 0
            draw.text((center - length, height), self.text1, (255, 255, 255), font=font)

    def drawTextBot(self):
        font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
        draw = ImageDraw.Draw(self.newImage)
        lineCount = 1
        textWidth, textHeight = font.getsize(self.text2)  # gets the width and height of the text2 macro font
        if textWidth > self.pictureWidth:
            if textWidth / self.pictureWidth > 1 and textWidth / self.pictureWidth < 2:  # 2 lines of text
                lineCount = 2
                print("2 lines of text2")
                nth = (len(self.text2) / 2) + 2
                temp2 = textwrap.wrap(self.text2, nth)
                print(temp2)
                firstpart = temp2[0]
                secondpart = temp2[1]

            elif textWidth / self.pictureWidth >= 2 and textWidth / self.pictureWidth < 3:  # 3 lines of text
                lineCount = 3
                print("3 lines of text2")
                nth = (len(self.text2) / 3) + 2
                temp2 = textwrap.wrap(self.text2, nth)
                print(temp2)
                firstpart = temp2[0]
                secondpart = temp2[1]
                thirdpart = temp2[2]

            elif textWidth / self.pictureWidth >= 3 and textWidth / self.pictureWidth < 4:  # 4 lines of text
                lineCount = 4
                print("4 lines of text2")
                nth = len(self.text2) / 4 + 2
                temp2 = textwrap.wrap(self.text2, nth)
                print(temp2)
                firstpart = temp2[0]
                secondpart = temp2[1]
                thirdpart = temp2[2]
                fourthpart = temp2[3]

            elif textWidth / self.pictureWidth >= 4:  # passed max
                print("Error: text2 is too long")
                sys.exit()
        else:
            print("1 line of text2")

        k = 1
        for h in range(lineCount, 0, -1):
            if (lineCount > 1):
                if h == 1:
                    textWidth, textHeight = font.getsize(firstpart)
                    self.text2 = firstpart
                elif h == 2:
                    textWidth, textHeight = font.getsize(secondpart)
                    self.text2 = secondpart
                elif h == 3:
                    textWidth, textHeight = font.getsize(thirdpart)
                    self.text2 = thirdpart
                elif h == 4:
                    textWidth, textHeight = font.getsize(fourthpart)
                    self.text2 = fourthpart
                else:
                    print("Error in linecount")

            length = textWidth / len(
                self.text2)  # takes the width of the line of text and divides by the number of characters
            length = length * (len(
                self.text2) / 2)  # takes the individual char length and multiplies it by the amount of chars on the left side
            center = self.pictureWidth / 2  # gets the center point of the picture width
            if h > 0:
                height = self.pictureHeight - (textHeight * k)
            else:
                height = self.pictureHeight - textHeight
            draw.text((center - length, height - 2), self.text2, (255, 255, 255), font=font)
            k = k + 1
    #save it
    def saveNewImage(self):
        try:
          proj2.newImage.save("meme.png")
        except:
            print("Failed to save")

    #Getters and Setters
    def getImagePreview(self):
        return self.newImage, self.pictureHeight, self.pictureWidth

#p2 = proj2()
#p2.loadImage()
#p2.mysetText()
#p2.drawText()
#p2.saveNewImage()