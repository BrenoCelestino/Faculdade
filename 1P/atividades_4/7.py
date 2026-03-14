via = float(input())
velVeiculo = float(input())

porce = round(((velVeiculo - via) / via) * 100, 2)
if porce <= 0:
    print('0.00')
    print('0')
elif porce <= 20:
    print('85.13')
    print('4')
elif porce <= 50:
    print('127.69')
    print('5')
elif porce > 50:
    print('574.62')
    print('7')