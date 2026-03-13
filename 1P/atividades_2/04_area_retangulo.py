# (Problema: Área do retângulo) Faça um programa que calcule a área de um retângulo a
# partir dos tamanhos de seu lado maior e de seu lado menor. Os valores estão
# necessariamente entre 1 e 1000.

while True:
    ladoMaior = int(input('Informe o lado maior: '))
    ladoMenor = int(input('Informe o lado menor: '))

    if not(1 <= ladoMaior <= 1000 and 1 <= ladoMenor <= 1000):
        print('Os valores precisam ser entre 1 e 1000')
    elif ladoMaior < ladoMenor:
        print('Lado maior não pode ser menor que o lado menor.')
    else:
        break
    
A = ladoMaior * ladoMenor

print(f'{A}Cm²')