# (Problema: Cálculo do IMC) Faça um programa que receba as características (massa e
# altura) de uma pessoa e retorne seu IMC - Índice de Massa Corporal. A massa em Kg que
# pode estar entre 1 e 500. A altura em metros (m) que pode estar entre 1 e 2.8 O valor de
# saída deve ser arredondado usando 2 casas decimais. (Dica: imc= peso/(altura)2)

while True:

    massa = float(input("Massa: "))
    altura = float(input('Altura: '))

    if 1 < massa > 500:
        print('Massa deve ser entre 1 a 500')
    elif 1 < altura > 2.8:
        print('Altura deve estar entre 1 a 2.8 metros')
    else:
        break

imc = massa / (altura ** 2)

print(f"IMC= {imc}")