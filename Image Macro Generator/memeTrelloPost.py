# CST 205
# Project2.py
# github.com/rblakeman/CST205-Project2

import trello
import PIL, sys, textwrap, os
from PIL import Image, ImageFilter, ImageFont, ImageDraw
from trello import TrelloApi
import requests

choices = input("do you want to use a selfie for your meme?").lower()
if choices == "yes":
    '''
    ##webcam takes a picture
    camera_port = 0
    ramp_frames = 30
    camera = cv2.VideoCapture(camera_port)


    def get_image():
        retval, im = camera.read()
        return im


    print("Taking image...")
    camera_capture = get_image()
    file = "selfie.jpg"
    cv2.imwrite(file, camera_capture)
    del (camera)
    print("pick selfie for image to use")
    '''

# prints all pictures in folder
f = []
rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    print("found directory: %s" % dirName)
    for fname in fileList:
        if fname.endswith(".jpg") or fname.endswith(".png"):
            print("\t%s" % fname)

# definitions
location = "pic.png"
originalImage = Image
red = 0
green = 0
blue = 0
text = "text"
text2 = "text2"
firstpart = "string1"
secondpart = "string2"
thirdpart = "string3"
fourthpart = "string4"
temp = "list"
temp2 = "list2"

location = str(input('Enter picture name: '))
# open original image
try:
    originalImage = Image.open(location)
except:
    print("Failed to load")

# create new image to copy the original into too
newImage = Image.new("RGB", originalImage.size, (0, 0, 0))
newImagedata = newImage.load()
pictureWidth = originalImage.size[0]
pictureHeight = originalImage.size[1]
rgb_og = originalImage.convert('RGB')  # conversion error check
for x in range(0, pictureWidth):
    for y in range(0, pictureHeight):
        red, green, blue = rgb_og.getpixel((x, y))
        newImagedata[x, y] = (red, green, blue)

# meme it
font = ImageFont.truetype("arial.ttf", 25)
draw = ImageDraw.Draw(newImage)
###################################################################################################
choices = input("if you took a selfie do you want to use emotion recognition? yes or no \n").lower()
if choices == "yes":
    '''
    enIm = imEn.Brightness(im)
    enhanced = enIm.enhance(1.5)
    im_array = np.array(enhanced)
    crop_loc = ind.facial_localization(im_array)
    topX = crop_loc[0]['top_left_corner'][0]
    topY = crop_loc[0]['top_left_corner'][1]
    bottomX = crop_loc[0]['bottom_right_corner'][0]
    bottomY = crop_loc[0]['bottom_right_corner'][1]
    cropped_im = enhanced.crop((topX, topY, bottomX, bottomY))
    cropped_array = np.array(cropped_im)
    emoDict = ind.fer(data)
    sortedDict = sorted(emoDict.items(), key=operator.itemgetter(1))
    '''

if choices == "no":
    text = str(input('Enter top text: '))

lineCount = 1
textWidth, textHeight = font.getsize(text)  # gets the width and height of the text macro font
if textWidth > pictureWidth:
    if textWidth / pictureWidth > 1 and textWidth / pictureWidth < 2:  # 2 lines of text
        lineCount = 2
        print("2 lines of text")
        nth = (len(text) / 2) + 2  # finds length to dissect string at
        temp = textwrap.wrap(text, nth)  # textwrap dissectes string every nth character
        print(temp)
        firstpart = temp[0]
        secondpart = temp[1]

    elif textWidth / pictureWidth >= 2 and textWidth / pictureWidth < 3:  # 3 lines of text
        lineCount = 3
        print("3 lines of text")
        nth = (len(text) / 3) + 2  # finds length to dissect string at
        temp = textwrap.wrap(text, nth)  # textwrap dissectes string every nth character
        print(temp)
        firstpart = temp[0]
        secondpart = temp[1]
        thirdpart = temp[2]

    elif textWidth / pictureWidth >= 3 and textWidth / pictureWidth < 4:  # 4 lines of text
        lineCount = 4
        print("4 lines of text")
        nth = len(text) / 4 + 2  # finds length to dissect string at
        temp = textwrap.wrap(text, nth)  # textwrap dissectes string every nth character
        print(temp)
        firstpart = temp[0]
        secondpart = temp[1]
        thirdpart = temp[2]
        fourthpart = temp[3]

    elif textWidth / pictureWidth >= 4:  # passed max
        print("Error: Text is too long")
        sys.exit()
else:
    print("1 line of text")  # debug

for j in range(0, lineCount):
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
            print("Error in linecount")

    length = textWidth / len(text)  # takes the width of the line of text and divides by the number of characters
    length = length * (
    len(text) / 2)  # takes the individual char length and multiplies it by the amount of chars on the left side
    center = pictureWidth / 2  # gets the center point of the picture width
    if j > 0:
        height = textHeight * j - 1
    else:
        height = 0
    draw.text((center - length, height), text, (255, 255, 255), font=font)

###################################################################################################
text2 = str(input('Enter bottom text: '))
lineCount = 1
textWidth, textHeight = font.getsize(text2)  # gets the width and height of the text2 macro font
if textWidth > pictureWidth:
    if textWidth / pictureWidth > 1 and textWidth / pictureWidth < 2:  # 2 lines of text
        lineCount = 2
        print("2 lines of text2")
        nth = (len(text2) / 2) + 2  # finds length to dissect string at
        temp2 = textwrap.wrap(text2, nth)  # textwrap dissectes string every nth character
        print(temp2)
        firstpart = temp2[0]
        secondpart = temp2[1]

    elif textWidth / pictureWidth >= 2 and textWidth / pictureWidth < 3:  # 3 lines of text
        lineCount = 3
        print("3 lines of text2")
        nth = (len(text2) / 3) + 2  # finds length to dissect string at
        temp2 = textwrap.wrap(text2, nth)  # textwrap dissectes string every nth character
        print(temp2)
        firstpart = temp2[0]
        secondpart = temp2[1]
        thirdpart = temp2[2]

    elif textWidth / pictureWidth >= 3 and textWidth / pictureWidth < 4:  # 4 lines of text
        lineCount = 4
        print("4 lines of text2")
        nth = len(text2) / 4 + 2  # finds length to dissect string at
        temp2 = textwrap.wrap(text2, nth)  # textwrap dissectes string every nth character
        print(temp2)
        firstpart = temp2[0]
        secondpart = temp2[1]
        thirdpart = temp2[2]
        fourthpart = temp2[3]

    elif textWidth / pictureWidth >= 4:  # passed max
        print("Error: text2 is too long")
        sys.exit()
else:
    print("1 line of text2")  # debug

k = 1
for h in range(lineCount, 0, -1):
    if (lineCount > 1):
        if h == 1:
            textWidth, textHeight = font.getsize(firstpart)
            text2 = firstpart
        elif h == 2:
            textWidth, textHeight = font.getsize(secondpart)
            text2 = secondpart
        elif h == 3:
            textWidth, textHeight = font.getsize(thirdpart)
            text2 = thirdpart
        elif h == 4:
            textWidth, textHeight = font.getsize(fourthpart)
            text2 = fourthpart
        else:
            print("Error in linecount")

    length = textWidth / len(text2)  # takes the width of the line of text and divides by the number of characters
    length = length * (
    len(text2) / 2)  # takes the individual char length and multiplies it by the amount of chars on the left side
    center = pictureWidth / 2  # gets the center point of the picture width
    if h > 0:
        height = pictureHeight - (textHeight * k)
    else:
        height = pictureHeight - textHeight
    draw.text((center - length, height - 2), text2, (255, 255, 255), font=font)
    k = k + 1

# save it
newImage.save("meme.png")
print("Congratulations! Your new meme is saved as 'meme.png' in the folder.")
choices = input("do you want to post your meme?").lower()

if choices == "yes":

    TRELLO_APP_KEY = "710496170f05f20abac12d53d925156b";
    TRELLO_TOKEN = "cbc3c740c90ff176fe8e6d599e3f955d2c61b44692ab6fc8582e57c3112c6c51";
    trello = TrelloApi(TRELLO_APP_KEY, TRELLO_TOKEN)
    trello.get_token_url('My App', expires='30days', write_access=True)
    'https://trello.com/1/authorize?key=710496170f05f20abac12d53d925156b&name=My+App&expiration=30days&response_type=token&scope=read,write'
    trello.lists.new_card(2,"name","Test Card")
