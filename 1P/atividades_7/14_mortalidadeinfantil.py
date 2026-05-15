criancas = int(input())

numFeminino = 0
numMasculino = 0
numMenor24 = 0

if criancas <= 0:
    print('Informe um numero positivo')
    exit()

for i in range(criancas):
    sexo = input()
    idade = int(input())

    if sexo == 'M':
        numMasculino += 1
    else:
        numFeminino += 1

    if idade <= 24:
        numMenor24 += 1

print(f'{(numFeminino/criancas)*100:.1f}%')
print(f'{(numMasculino/criancas)*100:.1f}%')
print(f'{(numMenor24/criancas)*100:.1f}%')