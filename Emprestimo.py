casa=int(input('Qual o valor do imóvel a ser financiado? '))
salario=int(input('Qual o salário do cliente? '))
anos=int(input('Em quantos anos o cliente dejesa pagar o imóvel? '))

prestacao=casa/(anos*12)
salario30=salario*0.3

print()
if prestacao>salario30:
    print('Sua prestação será de', round(prestacao),'euros por mês e 30% do seu salário é',salario30,)
    print('Sendo assim, infelizmente não podemos conceder emprestimo')
else:
    print('Sua prestação será de', round(prestacao), 'euros por mês e 30% do seu salário é', salario30, )
    print('Parabens! Nós podemos conceder emprestimo')
