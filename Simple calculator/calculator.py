import math
import re
from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=30, borderwidth=2, font=("Arial", 12))
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear_Entry():
    e.delete(0, END)


def button_clear_last():
    current = e.get()
    new = current[:-1]
    e.delete(0, END)
    e.insert(0, new)


def button_add():
    first_number = e.get()
    global f_num
    global op
    op = "add"
    f_num = float(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global op
    op = "sub"
    f_num = float(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global op
    op = "mul"
    f_num = float(first_number)
    e.delete(0, END)


def button_deci():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + ".")
    global op
    op = "decimal"


def button_div():
    first_number = e.get()
    global f_num
    global op
    op = "div"
    f_num = float(first_number)
    e.delete(0, END)


def button_sqrt():
    e.insert(0, "√")
    global op
    op = "root"


def button_percent():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "%")
    global op
    op = "percentage"


def button_eq():
    second_number = e.get()
    match_root = re.search(r'√(\d+)', second_number)
    match_percent = re.search(r'(\d+)%', second_number)
    if match_root:
        second_number = float(match_root.group(1))
    elif match_percent:
        second_number = float(match_percent.group(1))
    else:
        second_number = float(second_number)
    e.delete(0, END)
    if op == "add":
        e.insert(0, str(f_num + second_number))
    elif op == "sub":
        e.insert(0, str(f_num - second_number))
    elif op == "mul":
        e.insert(0, str(f_num * second_number))
    elif op == "div":
        if second_number == 0:
            e.insert(0, "∞")
        else:
            e.insert(0, str(f_num / second_number))
    elif op == "root":
        e.insert(0, str(math.sqrt(second_number)))
    elif op == "percentage":
        e.insert(0, str(second_number * 0.01))


# creating buttons

button_1 = Button(root, text="1", padx=25, pady=20, borderwidth=3, command=lambda: button_click(1), bg="#A9A9A9")
button_2 = Button(root, text="2", padx=25, pady=20, borderwidth=3, command=lambda: button_click(2), bg="#A9A9A9")
button_3 = Button(root, text="3", padx=25, pady=20, borderwidth=3, command=lambda: button_click(3), bg="#A9A9A9")
button_4 = Button(root, text="4", padx=25, pady=20, borderwidth=3, command=lambda: button_click(4), bg="#A9A9A9")
button_5 = Button(root, text="5", padx=25, pady=20, borderwidth=3, command=lambda: button_click(5), bg="#A9A9A9")
button_6 = Button(root, text="6", padx=25, pady=20, borderwidth=3, command=lambda: button_click(6), bg="#A9A9A9")
button_7 = Button(root, text="7", padx=25, pady=20, borderwidth=3, command=lambda: button_click(7), bg="#A9A9A9")
button_8 = Button(root, text="8", padx=25, pady=20, borderwidth=3, command=lambda: button_click(8), bg="#A9A9A9")
button_9 = Button(root, text="9", padx=25, pady=20, borderwidth=3, command=lambda: button_click(9), bg="#A9A9A9")
button_0 = Button(root, text="0", padx=25, pady=20, borderwidth=3, command=lambda: button_click(0), bg="#A9A9A9")
button_plus = Button(root, text="+", padx=25, pady=20, borderwidth=3, command=button_add, bg="#7F7FFF")
button_minus = Button(root, text="–", padx=27, pady=20, borderwidth=3, command=button_sub, bg="#7F7FFF")
button_multiply = Button(root, text="*", padx=27, pady=20, borderwidth=3, command=button_mul, bg="#7F7FFF")
button_divide = Button(root, text="÷", padx=25, pady=20, borderwidth=3, command=button_div, bg="#7F7FFF")
button_percentage = Button(root, text="%", padx=22, pady=20, borderwidth=3, command=button_percent, bg="#7F7FFF")
button_root = Button(root, text="√", padx=22, pady=20, borderwidth=3, command=button_sqrt, bg="#7F7FFF")
button_decimal = Button(root, text=".", padx=29, pady=20, borderwidth=3, command=button_deci, bg="#7F7FFF", )
button_equal = Button(root, text="=", padx=20, pady=56, borderwidth=3, command=button_eq, bg="orange")
button_clear = Button(root, text="C", padx=20, pady=20, borderwidth=3, command=button_clear_Entry, bg="red")
button_back = Button(root, text="←", padx=19, pady=20, borderwidth=3, command=button_clear_last, bg="red")

# buttons on the screen

button_back.grid(row=1, column=4)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_divide.grid(row=2, column=3)
button_clear.grid(row=2, column=4)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)
button_root.grid(row=3, column=4)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_minus.grid(row=4, column=3)
button_equal.grid(row=4, column=4, rowspan=2)

button_0.grid(row=5, column=0)
button_decimal.grid(row=5, column=1)
button_percentage.grid(row=5, column=2)
button_plus.grid(row=5, column=3)

root.mainloop()
