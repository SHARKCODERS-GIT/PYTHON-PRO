# Aula 16 | Extra 4 | Relógio de data

from tkinter import *
from datetime import date

root = Tk()
root.title("Hoje")
root.geometry("300x160+200+200")
lb = Label(root, text="", font="Arial 18 bold")
lb.place(x=0, y=30, width=300)
Button(root, text="Atualizar", command=lambda: lb.config(text=date.today().strftime("%d/%m/%Y"))).place(x=100, y=100, width=100)
root.mainloop()
