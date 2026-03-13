# Faça um algoritmo para ler o salário de um funcionário e aumentá-lo em 15%. Após o
# aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o
# salário final.

aum = 15
imposto = 8

salIni = float(input('Informe o salário inicial: '))

salAum = ((salIni) * (aum / 100)) + salIni

salDes = salAum - ((salAum * (imposto / 100)))

print(f'\nOs valores do salario em todos os tipos é:\nSalário Inicial: {salIni:.2f}\nSalário com Aumento: {salAum:.2f}\nSalário com Desconto: {salDes:.2f}')