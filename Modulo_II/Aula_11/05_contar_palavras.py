# Aula 11 | Exercício 5 | Contar palavras

frase = input("Frase? ").lower()
contagem = {}

for palavra in frase.split():
    contagem[palavra] = contagem.get(palavra, 0) + 1

for palavra, n in sorted(contagem.items(), key=lambda par: par[1], reverse=True):
    print(palavra, n)
