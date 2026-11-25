# Aula 01 | Extra 4 | Consumo de combustível
# Entrada: quilómetros percorridos e litros gastos
# Saída: consumo médio em litros aos 100 km

km = float(input("Quilómetros percorridos? "))
litros = float(input("Litros gastos? "))

consumo = litros / km * 100

print("Consumo médio:", round(consumo, 1), "L/100 km")
