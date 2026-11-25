# Aula 06 | Extra 5 | Conversor de moeda seguro

try:
    euros = float(input("Valor em euros? "))
    taxa = float(input("Taxa de câmbio? "))
    if taxa <= 0:
        print("A taxa tem de ser positiva.")
    else:
        print(f"{euros:.2f} € = {euros * taxa:.2f} $")
except ValueError:
    print("Valores inválidos.")
