def log_de_erros():
    with open("erros.log", "a") as log:
        while True:
            entrada = input("Digite um número (ou 'sair' para terminar): ")
            if entrada.lower() == "sair":
                break
            try:
                numero = int(entrada)
                print(f"Você inseriu o número: {numero}")
            except ValueError as e:
                log.write(f"Erro: {str(e)} - Entrada: '{entrada}'\n")
                print("Erro! Por favor, insira um número válido.")

log_de_erros()
