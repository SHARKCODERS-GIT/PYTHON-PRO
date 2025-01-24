soma = 0
vezes = 0

n = int(input('Entre com um número: '))

while n != 0:
    try:
        n = int(input('Entre com um número: '))
        soma += n
        vezes += 1

    except (ValueError, TypeError):
        print('Problemas com os dados de entrada')

    except KeyboardInterrupt:
        print('O programa foi interrompido')

print()
media = round(soma/vezes)
print(f'Foram digitados {vezes} números e a soma de todos resultou em {soma}')
print(f'A média ficou em {media}')