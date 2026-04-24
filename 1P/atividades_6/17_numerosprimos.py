valores = int(input())
while valores > 12 or valores < 2:
    print('Informe um valor entre 2 e 12!')
    valores = int(input())

listaNum = []
contador = 0
while contador != valores:
    valor = [int(input())]
    listaNum = listaNum + valor
    contador += 1

primos = []

while listaNum != []:
    
    if listaNum[0] <= 1:
        del listaNum[0]
    else:
        i = 2
        eh_primo = 1
        
        while i < listaNum[0]:
            if listaNum[0] % i == 0:
                eh_primo = 0
                break
            i += 1

        if eh_primo == 1:
            primos = primos + [listaNum[0]]
        else:
            del listaNum[0]

print(primos)