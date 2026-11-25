# Aula 09 | Extra 4 | Contar vogais

def contar_vogais(texto):
    return len([c for c in texto.lower() if c in "aeiouáéíóúâêôãõ"])

frase = input("Frase? ")
print("Vogais:", contar_vogais(frase))
