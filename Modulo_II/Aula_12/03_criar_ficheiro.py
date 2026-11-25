# Aula 12 | Exercício 3 | Criar um ficheiro

def criar_ficheiro():
    nome = input("Nome do novo ficheiro (sem .txt)? ").strip()
    with open(nome + ".txt", "w", encoding="utf-8") as f:
        pass
    print(f"Ficheiro {nome}.txt criado com sucesso.")

criar_ficheiro()
