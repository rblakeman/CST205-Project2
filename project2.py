#import PIL, sys
from PIL import Image, ImageFilter, ImageFont, ImageDraw

def main():
    image1 = Image.open("C:/Users/minve/Desktop/Memes/Awakward Moment Seal.jpg")
    image1.load()
    image2 = Image.open("C:/Users/minve/Desktop/Memes/Bad Luck Brian.jpg")
    image2.load()
    image3 = Image.open("C:/Users/minve/Desktop/Memes/Condescending Wonka.jpg")
    image3.load()
    image4 = Image.open("C:/Users/minve/Desktop/Memes/Futurama Fry.jpg")
    image4.load()
    image5 = Image.open("C:/Users/minve/Desktop/Memes/Desk Flip.jpg")
    image5.load()
    picture=[image1, image2, image3, image4, image5]
    choices = ('1 Awakward Moment Seal, 2 Bad Luck Brian, 3 Condescending Wonka, 4 Futurama Fry, 5 Desk Flip')
    print(choices)
    output =('select meme: ')
    print(output)
    number = input('select meme: ')
    image=picture[number]
    text= input('input text to be overlayed: ')
    memeGenerator(image,text)


def memeGenerator(image,text):
    #definitions
    originalImage = image
    red = 0
    green = 0
    blue = 0
    firstpart = "string1"
    secondpart = "string2"
    thirdpart = "string3"
    fourthpart = "string4"

    #open original image
   # try:
    #    originalImage = Image.open("pic.png")
    #except:
     #    print ("Failed to load")

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
    text = line
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
    newImage.show
