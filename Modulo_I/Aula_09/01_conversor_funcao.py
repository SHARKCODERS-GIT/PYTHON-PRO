# Aula 09 | Exercício 1 | Conversor de temperatura

def celsius_para_fahrenheit(c):
    return c * 1.8 + 32

temp = float(input("Temperatura em °C? "))
f = celsius_para_fahrenheit(temp)
print(f"{temp} °C = {f:.1f} °F")
