raio = float(input(''))
angulo = float(input(''))
pi = 3.14

comArco = (raio * pi * angulo) / 180
areaSetor = (pi * (raio ** 2) * angulo) / 360

print(f'{comArco:.2f}\n{areaSetor:.2f}')