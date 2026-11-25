# Aula 17 | Extra 2 | Celsius para Fahrenheit

from tkinter import *

root = Tk()
root.title("Temperatura")
root.geometry("300x170+200+200")
e = Entry(root, font="Arial 12"); e.place(x=50, y=20, width=200)
lb = Label(root, text="", font="Arial 14 bold"); lb.place(x=0, y=110, width=300)
Button(root, text="Converter", command=lambda: lb.config(text=f"{float(e.get()) * 1.8 + 32:.1f} °F")).place(x=100, y=60, width=100)
root.mainloop()
