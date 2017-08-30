from AB2RedLionTags import *  
from Tkinter import *
import tkMessageBox
import PIL.Image, PIL.ImageTk
window = Tk()
global case
case = 0;
var1 = StringVar(window)
var1.set("RSLogix 5000")
var2 = StringVar(window)
var2.set("Siemens Step 7")

def firstWindow():   
    window.wm_title("Quick Mapper v0.5")
    window.iconbitmap('logo.ico')
    options = ['RSLogix 5000', 'Studio 5000', 'Siemens Step 7', 'Siemens TIA v13']
    introLabel = Label(window, padx = 10, text="Select the PLC types to be converted\n in the dropdown menus below").pack(side="top")
    arrow = PIL.ImageTk.PhotoImage(PIL.Image.open("arrow.png"))
    drop1 = OptionMenu(window,var1,*options).pack(side="left")
    arrowLabel = Label(window, padx = 20, image=arrow).pack(side="left")
    drop2 = OptionMenu(window,var2,*options).pack(side="left")
    submit = Button(window, text = "Next >", command=optionSelect).pack(side="bottom")
    mainloop()
def Error():  
    tkMessageBox.showinfo("Invalid option", "Functionality not ready yet")
def AB2RL():
    tkMessageBox.showinfo("Converting", "Converting...")
    tags = ABRedLionTags()
    tags.convert(200)
def optionSelect():
    print "Button pressed"
    if(var1.get() == "RSLogix 5000" and var2.get() == "Siemens Step 7"):
        print var1.get() + " ---> " +var2.get()
        print "Correct Case"
        global case
        case = 1;
        window.destroy()
    else:
        print var1.get() + " ---> " +var2.get()
        print "Invalid Case"
        global case
        case = 9;
        window.destroy()

firstWindow()
if case == 1:
    AB2RL()
else:
    Error()
