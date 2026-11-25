# Aula 16 | Desafio | Roleta de casino

from tkinter import *
from random import randint

VERMELHOS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
saldo = 1000

root = Tk()
root.title("Roleta SHARKCODERS")
root.geometry("520x300+200+200")
root.configure(bg="#0B5D3B")

lb_saldo = Label(root, text="Saldo: 1000 €", font="Arial 16 bold", fg="white", bg="#0B5D3B")
lb_saldo.place(x=0, y=20, width=520)
lb_res = Label(root, text="Faça a sua aposta", font="Arial 20 bold", fg="#F4D03F", bg="#0B5D3B")
lb_res.place(x=0, y=90, width=520, height=60)

def apostar(tipo):
    global saldo
    n = randint(0, 36)
    cor = "Verde" if n == 0 else ("Vermelho" if n in VERMELHOS else "Preto")
    ganhou = n != 0 and ((tipo == "Par" and n % 2 == 0) or (tipo == "Ímpar" and n % 2 == 1) or tipo == cor)
    saldo += 100 if ganhou else -100
    lb_res.config(text=f"{n} {cor} · {'Ganhou!' if ganhou else 'Perdeu'}")
    lb_saldo.config(text=f"Saldo: {saldo} €")

for i, tipo in enumerate(["Par", "Ímpar", "Vermelho", "Preto"]):
    Button(root, text=tipo, font="Arial 12 bold", command=lambda t=tipo: apostar(t)).place(x=20 + i * 125, y=220, width=110, height=45)

root.mainloop()
