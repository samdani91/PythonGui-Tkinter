from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="You clicked the button!")
    myLabel.pack()


myButton = Button(root, text="Click me", command=myClick,bg="blue",fg="white")
# myButton = Button(root, text="Click me", padx=50, pady=50)
# myButton = Button(root, text="Click me", state=DISABLED)

myButton.pack()

root.mainloop()
