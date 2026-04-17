# com for, faça um programa que leia dois números e imprima a soma de todos os números entre eles, inclusive os números digitados.

nume1 = int(input('Digite o primeiro número: '))
nume2 = int(input('Digite o segundo número: '))

num1 = min(nume1, nume2)
num2 = max(nume1, nume2)

num = list(range(num1, num2 + 1))

soma = 0
for i in num:
    soma = soma + i
print(f'A soma dos números entre {num1} e {num2} é {soma}!')
