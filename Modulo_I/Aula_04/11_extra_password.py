# Aula 04 | Extra 3 | Palavra-passe com 3 tentativas

tentativas = 0

while tentativas < 3:
    senha = input("Palavra-passe? ")
    tentativas = tentativas + 1
    if senha == "shark2026":
        print("Acesso permitido.")
        break
    else:
        print("Errada. Restam", 3 - tentativas, "tentativas.")

if senha != "shark2026":
    print("Conta bloqueada.")
