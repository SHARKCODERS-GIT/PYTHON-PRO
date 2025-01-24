import tkinter as tk

def troca_de_cores():
    def mudar_cor(cor):
        janela.configure(bg=cor)

    janela = tk.Tk()
    janela.title("Troca de Cores")
    janela.geometry("300x200")

    tk.Label(janela, text="Clique em uma cor:", font=("Arial", 14)).pack(pady=10)

    botoes = [
        ("Vermelho", "red"),
        ("Verde", "green"),
        ("Azul", "blue"),
        ("Amarelo", "yellow"),
    ]

    for texto, cor in botoes:
        botao = tk.Button(janela, text=texto, font=("Arial", 14), bg=cor, fg="white",
                          command=lambda c=cor: mudar_cor(c))
        botao.pack(pady=5, fill=tk.X)

    janela.mainloop()

troca_de_cores()
