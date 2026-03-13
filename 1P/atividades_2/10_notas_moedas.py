N = int(input('Digite o valor inteiro:\n'))

n100 = N // 100
nR100 = N % 100

n50 = nR100 // 50
nR50 = nR100 % 50

n20 = nR50 // 20
nR20 = nR50 % 20

n10 = nR20 // 10
nR10 = nR20 % 10

n5 = nR10 // 5
nR5 = nR10 % 5

n2 = nR5 // 2
nR2 = nR5 % 2

n1 = nR2 // 1
nR1 = nR2 % 1

print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} moeda(s) de R$ 1,00')