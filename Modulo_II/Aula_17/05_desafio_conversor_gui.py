# Aula 17 | Desafio | Conversor de moedas com interface

from tkinter import *
from tkinter import messagebox
import requests

def converter(moeda):
    try:
        valor = float(e_valor.get().replace(",", "."))
    except ValueError:
        messagebox.showwarning("Conversor", "Escreva um valor válido.")
        return
    url = "https://api.frankfurter.dev/v1/latest"
    taxa = requests.get(url, params={"from": "EUR", "to": moeda}, timeout=10).json()["rates"][moeda]
    lb.config(text=f"{valor:.2f} € = {valor * taxa:.2f} {moeda}")

root = Tk()
root.title("Conversor de moedas")
root.geometry("380x220+200+200")
Label(root, text="Valor em euros:", font="Arial 11").place(x=30, y=25)
e_valor = Entry(root, font="Arial 12")
e_valor.place(x=160, y=25, width=180)
for i, moeda in enumerate(["USD", "GBP", "BRL"]):
    Button(root, text=moeda, font="Arial 11 bold", command=lambda m=moeda: converter(m)).place(x=40 + i * 105, y=75, width=90, height=36)
lb = Label(root, text="", font="Arial 15 bold", fg="#1E1C4E")
lb.place(x=0, y=140, width=380)
root.mainloop()
