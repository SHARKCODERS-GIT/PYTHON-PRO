# Aula 16 | Exercício 4 | Nome da cor

from tkinter import *

root = Tk()
root.title("Color Changer")
root.geometry("500x300+200+200")
root.configure(bg="#364a85")

lb = Label(root, text="Escolha uma cor", font="Arial 22 bold", fg="white", bg="#364a85")
lb.place(x=0, y=80, width=500, height=60)

def mudar(nome, cor):
    root.configure(bg=cor)
    lb.config(text=nome, bg=cor)

cores = [("Vermelho", "#C0392B"), ("Verde", "#1E8449"), ("Laranja", "#D35400"), ("Roxo", "#6C3483")]
for i, (nome, cor) in enumerate(cores):
    Button(root, text=nome, bg=cor, fg="white", font="Arial 12 bold",
           command=lambda n=nome, c=cor: mudar(n, c)).place(x=20 + i * 117, y=230, width=105, height=45)

root.mainloop()
