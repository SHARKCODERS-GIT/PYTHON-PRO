# Aula 17 | Extra 5 | Lista de tarefas

from tkinter import *

root = Tk()
root.title("Tarefas")
root.geometry("320x170+200+200")
e = Entry(root); e.place(x=20, y=20, width=180)
lista = Listbox(root); lista.place(x=20, y=60, width=280, height=90)

def adicionar():
    lista.insert(END, e.get())
    e.delete(0, END)

Button(root, text="Adicionar", command=adicionar).place(x=210, y=17, width=90)
root.mainloop()
