# Aula 17 | Extra 1 | Calculadora de IMC

from tkinter import *

root = Tk()
root.title("IMC")
root.geometry("300x200+200+200")
Label(root, text="Peso (kg)").place(x=20, y=20)
Label(root, text="Altura (m)").place(x=20, y=55)
e_p = Entry(root); e_p.place(x=110, y=20, width=150)
e_a = Entry(root); e_a.place(x=110, y=55, width=150)
lb = Label(root, text="", font="Arial 14 bold"); lb.place(x=0, y=140, width=300)

def calcular():
    imc = float(e_p.get()) / float(e_a.get()) ** 2
    lb.config(text=f"IMC: {imc:.1f}")

Button(root, text="Calcular", command=calcular).place(x=100, y=95, width=100)
root.mainloop()
