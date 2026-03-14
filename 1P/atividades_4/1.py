nota = float(input())

if (0 > nota) or (nota > 10):
    print(f'Nota digitada: {nota}')
    print(f'A nota nao esta no intervalo [0,10]')
else:
    print(f'Nota digitada: {nota}')