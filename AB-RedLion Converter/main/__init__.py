# -*- coding: utf-8 -*-
# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/    
from tkinter import *
import tkinter as tk
import tkMessageBox, tkFileDialog
import PIL.Image, PIL.ImageTk
from AB2RedLionTags import *
from fileinput import filename
from ctypes.wintypes import tagSIZE

global case
case = 0;
LARGE_FONT= ("Verdana", 12)


class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Quick Mapper v0.5")
        tk.Tk.iconbitmap(self, 'logo.ico')
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    def new_window(self):
        self.newWindow = guideGUI()
        
class guideGUI(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        
        tk.Toplevel.__init__(self, *args, **kwargs)
        tk.Toplevel.wm_title(self, "Studio 5000 ---> Crimson 3.0 Guide")
        tk.Toplevel.iconbitmap(self, 'logo.ico')
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (guidePageOne, guidePageTwo, guidePageThree, guidePageFour, guidePageFive, guidePageSix):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(guidePageOne)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.arrow = PhotoImage(file="arrow.gif")
        self.logo = PhotoImage(file="logo.gif")
        self.var1 = tk.StringVar(self)
        self.var1.set("Studio 5000")
        self.var2 = tk.StringVar(self)
        self.var2.set("Siemens Step 7")
        options = ['RSLogix 5000', 'Studio 5000', 'Siemens Step 7', 'Siemens TIA v13']
        logoLabel = tk.Label(self, pady = 20, image=self.logo).pack(side="top")
        introLabel = tk.Label(self, padx = 10, text="Select the PLC softwares to be converted between\n in the dropdown menus below", font=LARGE_FONT).pack(side="top")
        submit = tk.Button(self, text = "Next >", command=self.optionSelect).pack(side="bottom")
        drop1 = tk.OptionMenu(self,self.var1,*options).pack()
        arrowLabel = Label(self, padx = 20, pady = 40, image=self.arrow).pack()
        drop2 = tk.OptionMenu(self,self.var2,*options).pack()
        print "Start Page showing"
        
    def optionSelect(self):
            print "Button pressed"
            if(self.var1.get() == "Studio 5000" and self.var2.get() == "Siemens Step 7"):
                print self.var1.get() + " ---> " + self.var2.get()
                print "Correct Case"
                global case
                case = 1;
                newWindow = guideGUI()
                app.show_frame(PageOne)
            else:
                print self.var1.get() + " ---> " + self.var2.get()
                print "Invalid Case"
                global case
                case = 9;
                self.Error()
                
    def Error(self):  
        tkMessageBox.showinfo("Invalid option", "Functionality not ready yet")
        
class PageOne(tk.Frame):
    global filename
    def __init__(self, parent, controller):
        self.PLCentryText = StringVar()
        self.PLCentryText.set("PLC Name in Crimson (e.g PLC1)")
        self.numberentryText = StringVar()
        self.numberentryText.set("Number of Tags (e.g 200)")
        self.fileentryText = StringVar()
        self.fileentryText.set("Browse for .CSV file or type filepath here...")
        self.tagNameentryText = StringVar()
        self.tagNameentryText.set("Name of Redlion module (e.g RedlionDSP)")
        tk.Frame.__init__(self, parent)
        labelStep5 = tk.Label(self, text="Quick Mapper needs the following information.\n Use the guide to enter them correctly.").pack(pady=10,padx=10)
        fileEntry = Entry(self, textvariable=self.fileentryText, width=70).pack()
        browsebutton = Button(self, text="Browse", command=self.browsefunc).pack()
        PLCEntry = Entry(self, textvariable=self.PLCentryText, width=50).pack()
        TagSizeEntry = Entry(self, textvariable=self.numberentryText, width=50).pack()
        TagNameEntry = Entry(self, textvariable=self.tagNameentryText,width=50).pack()      
        button1 = tk.Button(self, text="Next>", command=self.checkInputs).pack(side="bottom")
        labelStep6 = tk.Label(self, text="Click 'Next' when ready").pack(side="bottom")
        
    def browsefunc(self):
        global filename
        filename = tkFileDialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("CSV files", "*.csv"),("all files", "*.*")))
        self.fileentryText.set(filename)
        
    def checkInputs(self):
        global PLCName
        global TagName
        global TagSize
        global filename
        PLCName = self.PLCentryText.get()
        TagName = self.tagNameentryText.get()
        TagSize = self.numberentryText.get()
        filename = self.fileentryText.get()
        try:
            size = int(TagSize)
            if ABRedLionTags().convert(size, PLCName) == False:
                tkMessageBox.showinfo("Invalid inputs", "Did not find any tags with that name")
            else:  
                tkMessageBox.showinfo("Validated!", "Success!")
                app.show_frame(PageTwo)
        except:
            tkMessageBox.showinfo("Invalid inputs", "TagSize not type int")
            
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Blahdeeeblaaaahhhh").pack(pady=10,padx=10)
        button2 = tk.Button(self, text="Next>",command=lambda: controller.show_frame(guidePageTwo)).pack(side="right")
        
class guidePageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.img = PhotoImage(file="AB2SiemensStep1.gif")
        label = tk.Label(self, text="Complete the following steps before continuing").pack(pady=10,padx=10)
        labelStep1 = tk.Label(self, text="Save your Studio 5000 PLC code as a .L5K file as shown below:", justify=LEFT).pack()
        imageStep1 = Label(self, image=self.img).pack()
        labelStep2 = tk.Label(self, text="Click 'Next' when ready").pack()
        button2 = tk.Button(self, text="Next>",command=lambda: controller.show_frame(guidePageTwo)).pack(side="right")

class guidePageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.img = PhotoImage(file="AB2SiemensStep2.gif")
        labelStep3 = tk.Label(self, text="Follow the steps below to create a PLC in Crimson 3.0 for .L5K import:").pack(pady=10,padx=10)
        imageStep3 = tk.Label(self, image=self.img).pack()
        labelStep4 = tk.Label(self, text="Click 'Next' when ready").pack()
        button1 = tk.Button(self, text="<Back", command=lambda: controller.show_frame(guidePageOne)).pack(side="left")
        button2 = tk.Button(self, text="Next>", command=lambda: controller.show_frame(guidePageThree)).pack(side="right")

class guidePageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.img = PhotoImage(file="AB2SiemensStep3.gif")
        labelStep5 = tk.Label(self, text="This should have created a new PLC. Rename the PLC to whatever you like\n and click 'View Tag Names...':").pack(pady=10,padx=10)
        imageStep5 = tk.Label(self, image=self.img).pack()
        labelStep6 = tk.Label(self, text="Click 'Next' when ready").pack()
        button1 = tk.Button(self, text="<Back", command=lambda: controller.show_frame(guidePageTwo)).pack(side="left")
        button2 = tk.Button(self, text="Next>", command=lambda: controller.show_frame(guidePageFour)).pack(side="right") 
        
class guidePageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.img = PhotoImage(file="AB2SiemensStep4.gif")
        labelStep5 = tk.Label(self, text="Import the .L5K file you exported earlier").pack(pady=10,padx=10)
        imageStep5 = tk.Label(self, image=self.img).pack()
        labelStep6 = tk.Label(self, text="Click 'Next' when ready").pack()
        button1 = tk.Button(self, text="<Back", command=lambda: controller.show_frame(guidePageThree)).pack(side="left")
        button2 = tk.Button(self, text="Next>", command=lambda: controller.show_frame(guidePageFive)).pack(side="right")
        
class guidePageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.img = PhotoImage(file="AB2SiemensStep5.gif")
        labelStep5 = tk.Label(self, text="Now the data tags from our program should be represented in Crimson:").pack(pady=10,padx=10)
        imageStep5 = tk.Label(self, image=self.img).pack()
        labelStep6 = tk.Label(self, text="Click 'Next' when ready").pack()
        button1 = tk.Button(self, text="<Back", command=lambda: controller.show_frame(guidePageFour)).pack(side="left")
        button2 = tk.Button(self, text="Next>", command=lambda: controller.show_frame(guidePageSix)).pack(side="right")
        
class guidePageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.img = PhotoImage(file="AB2SiemensStep6.gif")
        labelStep5 = tk.Label(self, text="Now we need to map the tags to tags within Crimson.\n Quick Mapper will do this for you.\n Export the tags as a .CSV file from Studio 5000.").pack(pady=10,padx=10)
        imageStep5 = tk.Label(self, image=self.img).pack()
        labelStep6 = tk.Label(self, text="Then go back to the first window to continue").pack()
        button1 = tk.Button(self, text="<Back", command=lambda: controller.show_frame(guidePageFive)).pack(side="left")         

app = GUI()
app.mainloop()