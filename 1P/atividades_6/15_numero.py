pares = 0
impares = 0
positivos = 0
negativos = 0

while True:
    N = int(input())
    if N == 0:
        break

    if N > 0:
        positivos += 1
    else:
        if N < 0:
            negativos += 1

    if (N % 2) == 0:
        pares += 1
    else:
        impares += 1

print(pares, 'valores pares')

if impares == 1:
    print(impares, 'valor impar')
else:
    print(impares, 'valores impares')

if positivos == 1:
    print(positivos, 'valor positivo')
else:
    print(positivos, 'valores positivos')

if negativos == 1:
    print(negativos, 'valor negativo')
else:
    print(negativos, 'valores negativos')