# Aula 07 | Exercício 1 | Explorar uma lista

cidades = ["Porto", "Braga", "Faro", "Lisboa", "Coimbra"]

print(cidades[3])
print(cidades[2:4])
print(len(cidades))

cidades.append("Viseu")
cidades.extend(["Évora", "Aveiro"])
cidades.insert(1, "Fafe")
cidades.remove("Faro")
cidades.pop(0)
cidades.sort()
print(cidades)
