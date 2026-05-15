nCompetidores = int(input())
pParaConvidar = int(input())

convidados = 0

for i in range(nCompetidores):
    nota1 = int(input())
    nota2 = int(input())

    notaTotal = nota1 + nota2

    if nota1 == 0 or nota2 == 0:
        continue
    elif notaTotal >= pParaConvidar:
        convidados += 1

print(convidados)