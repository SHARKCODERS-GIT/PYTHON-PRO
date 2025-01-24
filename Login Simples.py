import tkinter as tk
from tkinter import messagebox

def login_simples():
    def verificar_credenciais():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        # Credenciais pré-definidas
        if usuario == "admin" and senha == "1234":
            messagebox.showinfo("Login", "Bem-vindo!")
        else:
            messagebox.showerror("Erro", "Credenciais inválidas!")

    janela = tk.Tk()
    janela.title("Login Simples")

    tk.Label(janela, text="Usuário:", font=("Arial", 14)).grid(row=0, column=0, pady=10, padx=10)
    entrada_usuario = tk.Entry(janela, font=("Arial", 14))
    entrada_usuario.grid(row=0, column=1, pady=10, padx=10)

    tk.Label(janela, text="Senha:", font=("Arial", 14)).grid(row=1, column=0, pady=10, padx=10)
    entrada_senha = tk.Entry(janela, font=("Arial", 14), show="*")
    entrada_senha.grid(row=1, column=1, pady=10, padx=10)

    botao_login = tk.Button(janela, text="Entrar", font=("Arial", 14), command=verificar_credenciais)
    botao_login.grid(row=2, column=0, columnspan=2, pady=10)

    janela.mainloop()

login_simples()
