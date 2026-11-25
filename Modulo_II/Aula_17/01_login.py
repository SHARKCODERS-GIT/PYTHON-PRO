# Aula 17 | Exercício 1 | Login simples

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login")
root.geometry("360x220+200+200")

Label(root, text="Utilizador", font="Arial 11").place(x=30, y=30)
Label(root, text="Palavra-passe", font="Arial 11").place(x=30, y=75)
e_user = Entry(root, font="Arial 11")
e_user.place(x=150, y=30, width=170)
e_senha = Entry(root, font="Arial 11", show="*")
e_senha.place(x=150, y=75, width=170)

def entrar():
    if e_user.get() == "admin" and e_senha.get() == "admin":
        messagebox.showinfo("Login", "Login efetuado com sucesso!")
    else:
        messagebox.showerror("Login", "Utilizador ou palavra-passe errados.")

Button(root, text="Entrar", font="Arial 11 bold", command=entrar).place(x=130, y=130, width=100, height=36)
root.mainloop()
