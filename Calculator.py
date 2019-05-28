#Calculator
import tkinter as tk
mainWindow = tk.Tk()
mainWindow.title("Calculator")
heading_label = tk.Label(mainWindow,text="Calculator")

heading_label2 = tk.Label(mainWindow,text="Enter first number",padx=(10),pady=(10))
heading_label2.pack()
lbl = tk.Label(mainWindow,text=" ")
lbl.pack()

name_field2 = tk.Entry(mainWindow)
name_field2.pack()


heading_label3 = tk.Label(mainWindow,text="Enter second number")
heading_label3.pack()

name_field3 = tk.Entry(mainWindow)
name_field3.pack()

# def takeValueInput():
#     first = name_field2.get()
#     second = name_field3.get()

def addition():
    first = int(name_field2.get())
    second = int(name_field3.get())
    lbl.config(text="" + str(first+second))
    lbl.pack()
def subtraction():
    first = int(name_field2.get())
    second = int(name_field3.get())
    lbl.config(text="" + str(first-second))
    lbl.pack()
def mul():
    first = int(name_field2.get())
    second = int(name_field3.get())
    lbl.config(text="" + str(first*second))
    lbl.pack()
def div():
    first = int(name_field2.get())
    second = int(name_field3.get())
    lbl.config(text="" + str(first/second))
    lbl.pack()


button1 = tk.Button(mainWindow, text="+", command=lambda: addition())
button1.pack()                                  #agar lambda function use nahi kia toh bina button pe click kare automatically function call ho jaega

button2 = tk.Button(mainWindow, text="-", command=lambda: subtraction())
button2.pack()

button3 = tk.Button(mainWindow, text="*", command=lambda: mul())
button3.pack()

button4 = tk.Button(mainWindow, text="/", command=lambda: div())
button4.pack()


mainWindow.mainloop()