numero = -1
soma = 0
div = -1

while numero != 0:
    div = div + 1
    numero = int(input())
    soma = numero + soma

print(f'{soma/div:.0f}')