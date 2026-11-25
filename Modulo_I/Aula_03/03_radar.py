# Aula 03 | Exercício 3 | Radar de velocidade

velocidade = float(input("Velocidade (km/h)? "))

if velocidade > 80:
    multa = (velocidade - 80) * 2
    print("Excesso de velocidade! Multa de", multa, "€")
else:
    print("Velocidade dentro do limite. Boa viagem!")
