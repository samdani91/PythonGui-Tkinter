from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

myImg1 = ImageTk.PhotoImage(Image.open("images/me1.jpg"))
myImg2 = ImageTk.PhotoImage(Image.open("images/me2.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("images/me3.jpg"))
myImg4 = ImageTk.PhotoImage(Image.open("images/me4.jpg"))
myImg5 = ImageTk.PhotoImage(Image.open("images/me5.jpg"))
myImg6 = ImageTk.PhotoImage(Image.open("images/me6.jpg"))

image_list = [myImg1, myImg2, myImg3, myImg4, myImg5, myImg6]

my_label = Label(image=myImg1)
my_label.grid(row=1, column=0, columnspan=3)


def forward(img_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_number - 1])
    button_next = Button(root, text=">>", command=lambda: forward(img_number + 1), bg="green", fg="white")
    button_back = Button(root, text="<<", command=lambda: back(img_number - 1), bg="blue", fg="white")

    if img_number == len(image_list):
        button_next = Button(root, text=">>", state=DISABLED, bg="green", fg="white")

    my_label.grid(row=1, column=0, columnspan=3)

    button_back.grid(row=0, column=0)
    button_next.grid(row=0, column=2)


def back(img_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_number - 1])
    button_next = Button(root, text=">>", command=lambda: forward(img_number + 1), bg="green", fg="white")
    button_back = Button(root, text="<<", command=lambda: back(img_number - 1), bg="blue", fg="white")

    if img_number == 1:
        button_back = Button(root, text="<<", state=DISABLED, bg="blue", fg="white")

    my_label.grid(row=1, column=0, columnspan=3)

    button_back.grid(row=0, column=0)
    button_next.grid(row=0, column=2)


button_quit = Button(root, text="Exit", command=root.quit, bg="red", fg="white")
button_back = Button(root, text="<<", command=back, bg="blue", fg="white", state=DISABLED)
button_next = Button(root, text=">>", command=lambda: forward(2), bg="green", fg="white")

button_quit.grid(row=0, column=1)
button_back.grid(row=0, column=0)
button_next.grid(row=0, column=2)

root.mainloop()
