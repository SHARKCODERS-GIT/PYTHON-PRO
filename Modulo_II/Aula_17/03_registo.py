# Aula 17 | Exercício 3 | Registo de utilizadores

from tkinter import *
from tkinter import messagebox
import json, os, hashlib

FICHEIRO = "utilizadores.json"

def carregar():
    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, encoding="utf-8") as f:
            return json.load(f)
    return {}

def registar():
    nome, login, senha = e_nome.get().strip(), e_login.get().strip().lower(), e_senha.get()
    if not nome or not login or not senha:
        messagebox.showwarning("Registo", "Preencha todos os campos.")
        return
    users = carregar()
    if login in users:
        messagebox.showerror("Registo", "Esse utilizador já existe.")
        return
    users[login] = {"nome": nome, "senha": hashlib.sha256(senha.encode()).hexdigest()}
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4, ensure_ascii=False)
    messagebox.showinfo("Registo", f"Utilizador {login} registado.")

root = Tk()
root.title("Registo")
root.geometry("360x260+200+200")
campos = []
for i, rotulo in enumerate(["Nome", "Utilizador", "Palavra-passe"]):
    Label(root, text=rotulo).place(x=30, y=30 + i * 45)
    e = Entry(root, show="*" if i == 2 else "")
    e.place(x=150, y=30 + i * 45, width=170)
    campos.append(e)
e_nome, e_login, e_senha = campos
Button(root, text="Registar", command=registar).place(x=130, y=180, width=100, height=36)
root.mainloop()
