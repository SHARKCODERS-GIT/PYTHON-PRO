# Aula 17 | Exercício 4 | Login com o ficheiro

from tkinter import *
from tkinter import messagebox
import json, hashlib

def entrar():
    with open("utilizadores.json", encoding="utf-8") as f:
        users = json.load(f)
    login = e_user.get().strip().lower()
    senha = hashlib.sha256(e_senha.get().encode()).hexdigest()
    if login in users and users[login]["senha"] == senha:
        root.withdraw()
        area = Toplevel(root)
        area.title("Área reservada")
        area.geometry("360x200+240+240")
        Label(area, text=f"Bem-vindo, {users[login]['nome']}!", font="Arial 15 bold").place(x=0, y=40, width=360)
        Button(area, text="Logout", command=root.destroy).place(x=130, y=120, width=100, height=36)
    else:
        messagebox.showerror("Login", "Credenciais inválidas.")

root = Tk()
root.title("Login")
root.geometry("360x220+200+200")
Label(root, text="Utilizador").place(x=30, y=30)
Label(root, text="Palavra-passe").place(x=30, y=75)
e_user = Entry(root)
e_user.place(x=150, y=30, width=170)
e_senha = Entry(root, show="*")
e_senha.place(x=150, y=75, width=170)
Button(root, text="Entrar", command=entrar).place(x=130, y=130, width=100, height=36)
root.mainloop()
