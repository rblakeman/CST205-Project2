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
############Main####################
def Main():
    folder = os.path.dirname(os.path.realpath('__file__'))
    fileName = os.path.join(folder, '../MemeGenerator/Memes/')
    fileName = os.path.abspath(os.path.realpath(fileName))
    title = 'Meme Generator'
    ##insert more memes
    choices =['aliens','sap']
    #User selects the image of choice
    memeSelection = memeBuilder ('Select Meme', title, choices)
    if(memeSelection == "Create Your Own Meme"): #Allows user to select their own picture to meme
        memePath = fileopenbox()
    else:
        memePath =  fileName + "\\" + memeSelection + ".jpg"


    meme = Image.open(memePath)
    meme.show() #Shows the desired image
    meme.save("copy.jpg") #Saves for further use
    meme = Image.open("copy.jpg") #Allows the new meme to be used

    text()
    confirmation()
################end main#############################

def memeBuilder('select Meme' title, choices):   
    #create new image to copy the original into too
    newImage = Image.new("RGB", originalImage.size(), (0,0,0))
    newImagedata = newImage.load()
    pictureWidth = originalImage.size[0]
    pictureHeight = originalImage.size[1]
    for x in range(0,pictureWidth):
        for y in range(0, pictureHeight):
            rgb_og = originalImage.convert('RGB')
            red, green, blue = rgb_og.getpixel((x,y))
            newImagedata[x,y] = (red, green, blue)

def textAdd(newImage):
    font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
    draw = ImageDraw.Draw(newImage)

    text = "Test Meme"
    length = len(text) / 2
    center = pictureWidth / 2
    draw.text((center - length,0), text, (255,255,255), font=font)

