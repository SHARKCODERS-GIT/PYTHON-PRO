# Aula 09 | Desafio | Sorteio e estatísticas

from random import randint

def sortear():
    return [randint(1, 20) for i in range(10)]

def estatisticas(lista):
    print("Números sorteados:", lista)
    print(f"Maior: {max(lista)} · Menor: {min(lista)}")
    print(f"Soma: {sum(lista)} · Média: {sum(lista) / len(lista):.1f}")

numeros = sortear()
estatisticas(numeros)
