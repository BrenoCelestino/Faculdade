idade = int(input())

if idade >= 0 and idade < 10:
    print('crianca')
else:
    if idade >= 10 and idade < 18:
        print('adolescente')
    else:
        if idade >= 18:
            print('adulto')