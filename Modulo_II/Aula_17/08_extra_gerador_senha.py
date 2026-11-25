# Aula 17 | Extra 3 | Gerador de palavras-passe

from tkinter import *
import random, string

carateres = string.ascii_letters + string.digits + "!?#$%"
root = Tk()
root.title("Gerador")
root.geometry("320x150+200+200")
lb = Label(root, text="", font="Courier 16 bold"); lb.place(x=0, y=25, width=320)
Button(root, text="Gerar", command=lambda: lb.config(text="".join(random.choice(carateres) for _ in range(12)))).place(x=110, y=85, width=100)
root.mainloop()
