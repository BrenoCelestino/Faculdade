salario = float(input()) #1000
empreAtivo = float(input()) #200

porcEmpre = salario * (30/100) #300
dispo = porcEmpre - empreAtivo

if empreAtivo >= porcEmpre:
    print('0.00')
else:
    print(f'{dispo:.2f}')