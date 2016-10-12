import proj2class
import PIL, tkinter, sys
from PIL import Image, ImageTk, ImageFilter, ImageFont, ImageDraw
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

class myMemeGUI:
    pro2 = proj2class.proj2
    photo = ImageTk.PhotoImage
    imgLbl = ttk.Label
    picReady = FALSE

    def __init__(self):
        myMemeGUI.pro2 = proj2class.proj2()
        myMemeGUI.pro2.loadImage()
        return

    def selectPic(self):
        return

    def getPic(self):
        #image = PIL.Image.open("pic.png")
        #photo = ImageTk.PhotoImage(image)

        photo = ImageTk.PhotoImage(self.pro2.getImg())
        return photo

    def guiSetText(self,input):
        self.pro2.setText(input)
        self.pro2.drawText()
        photo = self.getPic()
        self.imgLbl.configure(image=photo)
        self.imgLbl.image = photo
        self.picReady = TRUE
        return

    def publish(self):
        if(self.picReady):
            self.pro2.saveNewImage()
        return

    def displayGUI(self):
        root = Tk()
        root.title("Meme Generator")

        #set up main frame
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        #text input variable
        inputText = StringVar()

        #Widgets
        imgFrame = ttk.Frame(mainframe, borderwidth = 5, relief = "raised", padding="1 1 2 2")
        self.photo = self.getPic()

        self.imgLbl = ttk.Label(imgFrame, image=self.photo)
        txtLbl1 = ttk.Label(mainframe, text="Enter Text")
        #inputEntry = ttk.Entry(mainframe, width=100, textvariable=inputText)
        inputEntry = tkinter.Text(mainframe, height=2, width=20)
        #ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

        #lambda abstraction needed to prevent function being called on initialization
        setTxtBtn = ttk.Button(mainframe, text="Preview", command=lambda i1="1.0",i2=END: self.guiSetText(inputEntry.get(i1,i2)))
        publishBtn = ttk.Button(mainframe, text="Publish", command=lambda :self.publish())

        #Grid Alignment
        imgFrame.grid(column=4, row=1, columnspan=5, rowspan=5)
        self.imgLbl.grid(column=1, row=1)
        txtLbl1.grid(column=1, row=1, columnspan=2, sticky=(S,W,E))
        inputEntry.grid(column=1, row=2, columnspan=2, rowspan=2, sticky=(N, W, E))
        setTxtBtn.grid(column=1, row=4, columnspan=2,sticky=(S, W, E))
        publishBtn.grid(column=1, row=5, columnspan=2, sticky=(W, E))

        # shortcut for adding padding to all frame children
        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        # automatically sets text box to active, hitting enter/return will execute set text
        inputEntry.focus()
        root.bind('<Return>', self.guiSetText)

        root.mainloop()

myGUI = myMemeGUI()
myGUI.displayGUI()
