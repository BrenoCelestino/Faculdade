N = int(input())
anterior = 0
soma = 1
x = 0

for i in range(0, N):
    print(anterior)
    x = soma
    soma = anterior + soma
    anterior = x