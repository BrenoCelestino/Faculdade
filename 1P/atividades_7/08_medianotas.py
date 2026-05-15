media = 0
soma = 0
vezes = 0

nNotas = int(input())

for i in range(nNotas):
    nota = int(input())
    vezes += 1
    soma += nota

media = soma / vezes

print(round(media, 1))