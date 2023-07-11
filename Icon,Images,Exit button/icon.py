from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Welcome to Python Tkinter")
# root.wm_iconbitmap('/home/samdani/Desktop/pythonProject/PythonGui/Icon,Images,Exit button')

myImg = ImageTk.PhotoImage(Image.open("icon.py"))
my_label = Label(image=myImg)
my_label.pack()

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()
