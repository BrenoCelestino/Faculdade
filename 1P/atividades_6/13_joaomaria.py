carroMaisRapido = 0
carroMaisNovo = 0
velocidadeTotal = 0
carros = 0

while True:
    rodar = input().lower()
    if rodar == 'n':
        break

    ano = int(input())
    velocidade = float(input())

    velocidadeTotal = velocidadeTotal + velocidade
    carros = carros + 1

    if velocidade > carroMaisRapido:
        carroMaisRapido = velocidade
    if ano > carroMaisNovo:
        carroMaisNovo = ano

if carroMaisNovo == 0:
    print('zero')
else:
    print(f'{carroMaisRapido:.2f}')
    print(carroMaisNovo)
    print(f'{velocidadeTotal/carros:.2f}')