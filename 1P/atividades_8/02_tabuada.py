inicio = int(input())

while inicio < 1 or inicio > 9:
    print('Insira um número inicial entre 1 e 9')
    inicio = int(input())

fim = int(input())

while fim < 1 or fim > 9:
    print('Insira um número final entre 1 e 9')
    fim = int(input())

if inicio > fim:
    print('Nenhuma tabuada nesse intervalo')
    exit()

for i in range(inicio, fim + 1):
    for x in range(1, 10):
        print(i, 'x', x, '=', i*x)
    print()