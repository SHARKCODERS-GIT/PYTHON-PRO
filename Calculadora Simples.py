import tkinter as tk
from tkinter import messagebox

def calculadora_simples():
    def clique_botao(valor):
        entrada.insert(tk.END, valor)

    def calcular():
        try:
            resultado = eval(entrada.get())
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida!")

    def limpar():
        entrada.delete(0, tk.END)

    janela = tk.Tk()
    janela.title("Calculadora Simples")

    entrada = tk.Entry(janela, width=20, font=("Arial", 18), bd=8, insertwidth=4, justify="right")
    entrada.grid(row=0, column=0, columnspan=4)

    botoes = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    for (texto, linha, coluna) in botoes:
        if texto == "=":
            botao = tk.Button(janela, text=texto, padx=20, pady=20, font=("Arial", 14),
                              command=calcular)
        elif texto == "C":
            botao = tk.Button(janela, text=texto, padx=20, pady=20, font=("Arial", 14),
                              command=limpar)
        else:
            botao = tk.Button(janela, text=texto, padx=20, pady=20, font=("Arial", 14),
                              command=lambda valor=texto: clique_botao(valor))
        botao.grid(row=linha, column=coluna)

    janela.mainloop()

calculadora_simples()
