salario = float(input())
tarifaFixa = float(input())
tarifaQuilometro = float(input())
disPerco = float(input())
fimSemana = int(input())

trintaPorcento = salario * (30/100)

if fimSemana == 1:
    tarifa = tarifaFixa + (tarifaQuilometro * disPerco)
    tarifa = tarifa + (tarifa * (10/100))
elif fimSemana == 0:
    tarifa = tarifaFixa + (tarifaQuilometro * disPerco)

if tarifa > trintaPorcento:
    print('Não vai poder viajar.')
    print(f'{tarifa - trintaPorcento:.2f}')
elif tarifa < trintaPorcento:
    print('Vai poder viajar.')
    print(f'{tarifa:.2f}')
    print(f'{trintaPorcento - tarifa:.2f}')
