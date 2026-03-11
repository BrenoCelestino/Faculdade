KWhVal = 0.75
taxaLum = 5

con = float(input())

conta = con * KWhVal
contaTaxa = ((taxaLum / 100) * conta)

print(f'Valor do consumo: R$ {conta}')
print(f'Valor taxa iluminacao: R$ {contaTaxa}')
print(f'Valor total a pagar: R$ {contaTaxa + conta}')