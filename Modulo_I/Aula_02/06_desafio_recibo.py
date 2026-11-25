# Aula 02 | Desafio | Recibo de vencimento simplificado

nome = input("Nome do funcionário? ")
horas = float(input("Horas trabalhadas? "))
dependentes = int(input("Número de dependentes? "))

bruto = horas * 12 + dependentes * 40
seg_social = bruto * 0.11
irs = bruto * 0.15
liquido = bruto - seg_social - irs

print("Funcionário:", nome)
print("Salário bruto:", round(bruto, 2), "€")
print("Segurança Social (11%):", round(seg_social, 2), "€")
print("IRS (15%):", round(irs, 2), "€")
print("Salário líquido:", round(liquido, 2), "€")
