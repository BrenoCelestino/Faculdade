litros = float(input())
tipo = input()

if tipo == 'A':
    valor = litros * 1.90
    if litros <= 20:
        valorDes = valor - (valor * (3/100))
        print(f'R$ {valorDes:.2f}')
    elif litros > 20:
        valorDes = valor - (valor * (5/100))
        print(f'R$ {valorDes:.2f}')

elif tipo == 'G':
    valor = litros * 2.50
    if litros <= 20:
        valorDes = valor - (valor * (4/100))
        print(f'R$ {valorDes:.2f}')
    elif litros > 20:
        valorDes = valor - (valor * (6/100))
        print(f'R$ {valorDes:.2f}')

elif tipo == 'D':
    valor = litros * 1.66
    if litros <= 25:
        print(f'R$ {valor:.2f}')
    elif litros > 25:
        valorDes = valor - (valor * (4/100))
        print(f'R$ {valorDes:.2f}')