espaco = input()
porta = input()
valCar = float(input())
motor = float(input())
cambio = input()

if espaco != 'A' or porta != 'G':
    print('Não compre!')
else:
    desejaveis = [
        valCar < 100000.00,
        motor >= 1.5,
        cambio == 'A'
    ]

    if sum(desejaveis) == 3:
        print("Pode comprar!")
    elif sum(desejaveis) == 2:
        print("Boa compra.")
    else:
        print("Avalie melhor.")