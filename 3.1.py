import tkinter as tk

root = tk.Tk()
root.title("Window")

label = tk.Label(root, text="Hi")
label.pack()

button = tk.Button(root, text="Click")
button.pack()

def button_click():
    print("Clicked")

button.config(command=button_click)

root.mainloop()

import turtle

a = 0

def lclick(x, y):
    global a
    a += 1
    print("Clicked at лкм", a)
def rclick(x, y):
    global a
    a += 1
    print("Clicked at пкм", a)

turtle.onscreenclick(lclick, btn=1)
turtle.onscreenclick(rclick, btn=3)
turtle.mainloop()