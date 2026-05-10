diasMetaCum = 0
totalPoupado = 0
diaAnterior = 0
depositado = 0
contador = 0

while contador < 7:
    depositado = float(input())
    totalPoupado = totalPoupado + depositado

    if contador > 0 and (depositado-diaAnterior) >= 0.5:
        diasMetaCum += 1

    diaAnterior = depositado
    contador += 1

print('R$', f"{totalPoupado:.2f}")
print(diasMetaCum)