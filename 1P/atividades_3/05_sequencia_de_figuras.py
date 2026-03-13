figOne = 'Esquerda superior: vermelho\nDireita superior: amarelo\nEsquerda inferior: azul\nDireita inferior: verde'
figTwo = 'Esquerda superior: azul\nDireita superior: vermelho\nEsquerda inferior: verde\nDireita inferior: amarelo'
figTre = 'Esquerda superior: verde\nDireita superior: azul\nEsquerda inferior: amarelo\nDireita inferior: vermelho'
figFor = 'Esquerda superior: amarelo\nDireita superior: verde\nEsquerda inferior: vermelho\nDireita inferior: azul'

n = int(input())
if not n >= 1:
    print('O número informado é menor que 1.')
else:
    fig = n % 4
    if fig == 1:
        print(figOne)
    else:
        if fig == 2:
            print(figTwo)
        else:
            if fig == 3:
                print(figTre)
            else:
                if fig == 0:
                    print(figFor)