try:
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    r = n1/n2

except (ValueError, TypeError):
    print('Problemas com os dados de entrada')

except ZeroDivisionError:
    print('Não divisivel por Zero')

except KeyboardInterrupt:
    print('O programa foi interrompido')

else:
    print(f'O resultado é {r: .1f}')

finally:
    print()
    print('Volte sempre!')