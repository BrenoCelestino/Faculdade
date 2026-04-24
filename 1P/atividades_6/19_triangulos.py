def tipo_triangulo(l1, l2, l3):
    if (l1 + l2 <= l3) or (l1 + l3 <= l2) or (l2 + l3 <= l1):
        return 'INVALIDO'
    elif l1 == l2 == l3:
        return 'EQUILATERO'
    elif l1 == l2 or l2 == l3 or l1 == l3:
        return 'ISOSCELES'
    else:
        return 'ESCALENO'

numeros = input().split()

while 'FIM' not in numeros:
    numeros = list(map(int, numeros))
    triangulo = tipo_triangulo(numeros[0], numeros[1], numeros[2])
    print(triangulo)

    numeros = input().split()