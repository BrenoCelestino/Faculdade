gli = int(input())
contador = 0
soma = 0

while gli > 0:
    soma += gli
    contador = contador + 1
    gli = int(input())

media = soma / contador

if media >= 200:
    print('Glicose Muito Alta')
elif media < 110:
    print('Glicose Normal')
else:
    print('Glicose Alterada')