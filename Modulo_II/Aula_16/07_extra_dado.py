# Aula 16 | Extra 2 | Dado virtual

from tkinter import *
from random import randint

root = Tk()
root.title("Dado")
root.geometry("250x220+200+200")
lb = Label(root, text="?", font="Arial 60 bold")
lb.place(x=0, y=10, width=250, height=120)
Button(root, text="Lançar", font="Arial 12", command=lambda: lb.config(text=randint(1, 6))).place(x=75, y=150, width=100, height=40)

root.mainloop()
