# Aula 16 | Exercício 2 | Quatro botões

from tkinter import *

root = Tk()
root.title("Color Changer")
root.geometry("500x300+200+200")
root.configure(bg="#364a85")

BUT = {"font": "Arial 12 bold", "fg": "white"}
Button(root, text="Vermelho", bg="#C0392B", **BUT).place(x=20, y=230, width=105, height=45)
Button(root, text="Verde", bg="#1E8449", **BUT).place(x=137, y=230, width=105, height=45)
Button(root, text="Laranja", bg="#D35400", **BUT).place(x=254, y=230, width=105, height=45)
Button(root, text="Roxo", bg="#6C3483", **BUT).place(x=371, y=230, width=105, height=45)

root.mainloop()
