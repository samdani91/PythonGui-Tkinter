from tkinter import *

root = Tk()

e = Entry(root, width=30, bg="blue", fg="white", borderwidth=5)
e.pack()
# e.insert(0,"Enter your name:")

def myClick():
    hello="Hello "+e.get()
    myLabel = Label(root, text=hello)
    # myLabel = Label(root, text="Hello "+e.get())
    myLabel.pack()


myButton = Button(root, text="Enter your name", command=myClick, bg="blue", fg="white")

myButton.pack()

root.mainloop()
