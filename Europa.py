paises = ['França', 'Portugal', 'Espanha', 'Italia', 'Alemanha']

for x in range(3):
    escolha = input('Escolha um país da Europa: ')
    if escolha in paises:
        print('Parabens!')
        break
    else:
        print('Não há este pais na lista')