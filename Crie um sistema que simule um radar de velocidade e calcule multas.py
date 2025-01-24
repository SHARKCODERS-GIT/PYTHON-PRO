def verificar_velocidade(velocidade, limite):
    if velocidade <= limite:
        return "Velocidade dentro do limite."
    else:
        multa = (velocidade - limite) * 5  # Multa de 5 unidades por km acima do limite
        return f"Velocidade excedida! Multa: {multa:.2f} unidades."

limite_velocidade = float(input("Informe o limite de velocidade (km/h): "))
velocidade = float(input("Informe a velocidade do veículo (km/h): "))
resultado = verificar_velocidade(velocidade, limite_velocidade)
print(resultado)
