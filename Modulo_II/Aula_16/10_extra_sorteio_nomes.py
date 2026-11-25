# Aula 16 | Extra 5 | Sorteio de nomes

from tkinter import *
from random import choice

nomes = ["Ana", "Rui", "Inês", "Tiago", "Marta"]
root = Tk()
root.title("Sorteio")
root.geometry("300x160+200+200")
lb = Label(root, text="Quem será?", font="Arial 18 bold")
lb.place(x=0, y=30, width=300)
Button(root, text="Sortear", command=lambda: lb.config(text=choice(nomes))).place(x=100, y=100, width=100)
root.mainloop()
