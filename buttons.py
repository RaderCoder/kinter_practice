from tkinter import *

root = Tk()

def myClick():
    myLabel=Label(root, text="You clicked me!")
    myLabel.pack()

myButton = Button(root, text="Click Me", command=myClick, fg="white",bg="black")
myButton.pack()

root.mainloop()
