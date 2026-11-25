# Aula 17 | Extra 4 | Contador de caracteres

from tkinter import *

root = Tk()
root.title("Contador")
root.geometry("340x160+200+200")
e = Entry(root, font="Arial 11"); e.place(x=20, y=20, width=300)
lb = Label(root, text="", font="Arial 12"); lb.place(x=0, y=105, width=340)
Button(root, text="Contar", command=lambda: lb.config(text=f"{len(e.get())} caracteres · {len(e.get().split())} palavras")).place(x=120, y=60, width=100)
root.mainloop()
