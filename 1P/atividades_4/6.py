forma = input()

if forma == 'retangulo':
    numero = float(input())
    numeroA = float(input())
    A = numero * numeroA
    print(f'{A:.2f}')

elif forma == 'triangulo':
    numero = float(input())
    numeroA = float(input())
    A = (numero * numeroA) / 2
    print(f'{A:.2f}')

elif forma == 'trapezio':
    numero = float(input())
    numeroA = float(input())
    numeroB = float(input())
    A = ((numero + numeroA) * numeroB) / 2
    print(f'{A:.2f}')

elif forma == 'circulo':
    numero = float(input())
    A = (3.1415 * (numero ** 2))
    print(f'{A:.2f}')
else:
    print('Figura invalida.')