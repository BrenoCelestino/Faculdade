numero = float(input())
soma = 0
div = 0

while numero != -1:
    div = div + 1
    soma = soma + numero
    numero = float(input())

if div == 0:
    print(f'{soma:.2f}')
else:
    print(f'{soma/div:.2f}')
    