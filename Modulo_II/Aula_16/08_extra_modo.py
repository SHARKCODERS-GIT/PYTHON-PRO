# Aula 16 | Extra 3 | Modo claro e escuro

from tkinter import *

root = Tk()
root.title("Modo")
root.geometry("300x180+200+200")
escuro = False
lb = Label(root, text="Modo claro", font="Arial 16 bold")
lb.place(x=0, y=30, width=300)

def alternar():
    global escuro
    escuro = not escuro
    fundo, texto = ("black", "white") if escuro else ("white", "black")
    root.configure(bg=fundo)
    lb.config(bg=fundo, fg=texto, text="Modo escuro" if escuro else "Modo claro")

Button(root, text="Alternar", command=alternar).place(x=100, y=110, width=100)
root.configure(bg="white"); lb.config(bg="white")
root.mainloop()
