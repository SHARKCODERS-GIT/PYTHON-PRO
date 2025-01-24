def encontrar_maior_menor(numeros):
    maior = max(numeros)
    menor = min(numeros)
    return maior, menor

numeros = list(map(int, input("Digite uma lista de números separados por espaço: ").split()))
maior, menor = encontrar_maior_menor(numeros)
print(f"O maior número é {maior} e o menor número é {menor}.")
