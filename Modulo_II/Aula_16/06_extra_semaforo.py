# Aula 16 | Extra 1 | Semáforo

from tkinter import *

root = Tk()
root.title("Semáforo")
root.geometry("300x220+200+200")
lb = Label(root, text="", font="Arial 18 bold", bg="grey", fg="white")
lb.place(x=50, y=20, width=200, height=100)

def luz(cor, texto):
    lb.config(bg=cor, text=texto)

Button(root, text="Vermelho", command=lambda: luz("#C0392B", "Pare")).place(x=10, y=150, width=90)
Button(root, text="Amarelo", command=lambda: luz("#D4AC0D", "Atenção")).place(x=105, y=150, width=90)
Button(root, text="Verde", command=lambda: luz("#1E8449", "Avance")).place(x=200, y=150, width=90)

root.mainloop()
