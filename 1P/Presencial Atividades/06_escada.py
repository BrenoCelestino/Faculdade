nome = input()

tamn = len(nome)
passo = 1

for i in range(tamn):
    print((nome[0:passo]).upper())
    passo += 1