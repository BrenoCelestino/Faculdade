nome = input().lower()
tamn = len(nome)

for i in range(len(nome)):
    letra = nome[tamn-1:tamn]
    print(letra.upper(), end= "")
    tamn = tamn - 1