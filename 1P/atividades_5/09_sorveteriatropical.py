Sabor = input().lower()
bolas = int(input())

if Sabor in ['morango', 'cereja']:
    Valor = 4.50 * bolas
elif Sabor in ['damasco', 'siriguela']:
    Valor = 3.80 * bolas
else:
    Valor = 2.75 * bolas

if bolas > 2:
    print(f'{Valor:.2f}')
    print('COM CALDA')
else:
    print(f'{Valor:.2f}')
    print('SEM CALDA')