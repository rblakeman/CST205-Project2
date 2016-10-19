import proj2class
import PIL, tkinter, sys
import re
from PIL import ImageTk, ImageFilter, ImageFont, ImageDraw
import PIL.Image
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

class myMemeGUI:
    pro2 = proj2class.proj2
    photo = ImageTk.PhotoImage
    imgLbl = ttk.Label
    picReady = FALSE

    #Top Widgets
    root = Tk
    mainframe = ttk.Frame

    #Selection Widgets
    selectFrame = ttk.Frame
    fileList = ttk.Label
    selectImg = tkinter.Text
    exitSelect = ttk.Button

    #Editor Widgets
    editorFrame = ttk.Frame
    imgFrame = ttk.Frame
    txtLable1 = ttk.Label
    txtLable2 = ttk.Label
    txtLable3 = ttk.Label
    input1Entry = tkinter.Text
    input2Entry = tkinter.Text
    setTxtBtn = ttk.Button
    publishBtn = ttk.Button

    def __init__(self):
        self.pro2 = proj2class.proj2()

        self.root = Tk()
        self.root.title("Meme Generator")
        # set up main frame
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.grid(columnspan=10, rowspan=5)

        # Widgets
        self.selectFrame = ttk.Frame(self.mainframe, height=10, width=10, padding="1 1 1 1")
        self.fileList = ttk.Label(self.selectFrame, text="Enter Text")
        self.selectImg = tkinter.Text(self.selectFrame, height=2, width=20)
        self.exitSelect = ttk.Button(self.selectFrame, text="Load Image", command=lambda : self.gotoEditor())

        self.editorFrame = ttk.Frame(self.mainframe, padding="1 1 1 1")
        self.imgFrame = ttk.Frame(self.editorFrame, borderwidth=5, relief="raised", padding="1 1 2 2")

        self.imgLbl = ttk.Label(self.imgFrame)
        self.txtLbl1 = ttk.Label(self.editorFrame, text="Enter Text")
        # input1Entry = ttk.Entry(self.mainframe, width=100, textvariable=input1Text)
        self.input1Entry = tkinter.Text(self.editorFrame, height=2, width=20)
        self.input2Entry = tkinter.Text(self.editorFrame, height=2, width=20)
        # ttk.Label(self.mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

        # lambda abstraction needed to prevent function being called on initialization
        self.setTxtBtn = ttk.Button(self.editorFrame, text="Preview",
                                    command=lambda i1="1.0", i2=END: self.guiSetText(self.input1Entry.get(i1, i2),
                                                                          self.input2Entry.get(i1, i2)))
        self.publishBtn = ttk.Button(self.editorFrame, text="Publish", command=lambda: self.publish())

        return

    #Retrieves the Photo being edited by proj2 and creates a TK image to be displayed
    def getPic(self):
        #image = PIL.Image.open("pic.png")
        #photo = ImageTk.PhotoImage(image)

        photo = ImageTk.PhotoImage(self.pro2.getImg())
        return photo

    def getFileList(self):
        return self.pro2.returnImagesList()

    #Runs the proj2 code to add meme text to the photo
    def guiSetText(self,input1,input2):
        self.pro2.setText(input1,input2)
        self.pro2.drawText()
        photo = self.getPic()
        self.imgLbl.configure(image=photo)
        self.imgLbl.image = photo
        self.picReady = TRUE
        return

    #Save the Created Meme Picture if completed
    def publish(self):
        if(self.picReady):
            self.pro2.saveNewImage()
        return

    def gotoEditor(self):
        picstr = self.selectImg.get("1.0", END)
        picstr = re.sub('[\n\t\r ]', '', picstr)
        self.pro2.pickImage(picstr)
        outcome = self.pro2.loadImage()
        print("find: "+picstr+" "+str(outcome))
        if(not outcome):
            print("No Pic")
            return

        self.removeSelectGUI()
        self.displayEditGUI()
        return

    def displaySelectGUI(self):
        displaystr = "Found in Directory:\n" + self.getFileList()
        self.fileList['text'] = displaystr

        self.selectFrame.grid(columnspan=10, rowspan=5)
        self.fileList.grid(column=4, row=1, columnspan=5, rowspan=5)
        self.selectImg.grid(column=1, row=1)
        self.exitSelect.grid(column=1, row=2, columnspan=2,sticky=(N, W, E))

        self.input1Entry.focus()
        self.root.bind('<Return>', lambda x: self.gotoEditor())
        self.root.mainloop()
        return

    # remove Selection frame
    def removeSelectGUI(self):
        self.selectFrame.grid_forget()
        self.fileList.grid_forget()
        self.selectImg.grid_forget()
        self.exitSelect.grid_forget()
        return

    # show Editor frame
    def displayEditGUI(self):

        #text input1 variable
        input1Text = StringVar()

        self.photo = self.getPic()
        self.imgLbl.configure(image=self.photo)

        #Grid Alignment
        self.editorFrame.grid(columnspan=10, rowspan=5)
        self.imgFrame.grid(column=4, row=1, columnspan=5, rowspan=5)
        self.imgLbl.grid(column=1, row=1)
        self.txtLbl1.grid(column=1, row=1, columnspan=2, sticky=(S,W,E))
        self.input1Entry.grid(column=1, row=2, columnspan=2, rowspan=2, sticky=(N, W, E))
        self.input2Entry.grid(column=1, row=3, columnspan=2, rowspan=2, sticky=(N, W, E))
        self.setTxtBtn.grid(column=1, row=4, columnspan=2,sticky=(S, W, E))
        self.publishBtn.grid(column=1, row=5, columnspan=2, sticky=(W, E))

        # shortcut for adding padding to all frame children
        for child in self.editorFrame.winfo_children(): child.grid_configure(padx=4, pady=4)

        # automatically sets text box to active, hitting enter/return will execute set text
        self.input1Entry.focus()
        self.root.bind('<Return>', lambda i1="1.0",i2=END: self.guiSetText(self.input1Entry.get(i1,i2),self.input2Entry.get(i1,i2)))

        self.root.mainloop()

myGUI = myMemeGUI()
myGUI.displaySelectGUI()