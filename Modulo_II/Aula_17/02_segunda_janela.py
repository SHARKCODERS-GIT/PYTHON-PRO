# Aula 17 | Exercício 2 | Segunda janela

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("360x220+200+200")
Label(root, text="Utilizador").place(x=30, y=30)
Label(root, text="Palavra-passe").place(x=30, y=75)
e_user = Entry(root)
e_user.place(x=150, y=30, width=170)
e_senha = Entry(root, show="*")
e_senha.place(x=150, y=75, width=170)

def abrir_area():
    area = Toplevel(root)
    area.title("Área reservada")
    area.geometry("360x200+240+240")
    Label(area, text=f"Bem-vindo, {e_user.get()}!", font="Arial 16 bold").place(x=0, y=40, width=360)
    Button(area, text="Logout", command=area.destroy).place(x=130, y=120, width=100, height=36)

def entrar():
    if e_user.get() == "admin" and e_senha.get() == "admin":
        abrir_area()
    else:
        messagebox.showerror("Login", "Utilizador ou palavra-passe errados.")

Button(root, text="Entrar", command=entrar).place(x=130, y=130, width=100, height=36)
root.mainloop()
