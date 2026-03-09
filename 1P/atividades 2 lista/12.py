total = float(input())

des = total - ((10/100) * total)
parc = (total / 3)
comVista = ((5/100) * des)
comPrazo = ((5/100) * total)

print()
print(f'A vista com desconto de 10%: {des:.2f}')
print(f'Valor da parcela em 3x sem juros: {parc:.2f}')
print(f'Comissao do vendedor a vista: {comVista:.2f}')
print(f'Comissao do vendedor a prazo: {comPrazo:.2f}')