soma = 0
valorArvore = int(input())

for i in range(3):
    quantidade = int(input())
    valor = float(input())
    soma += (quantidade * valor)

total = soma + valorArvore

print(f'{total:.2f}')
print(f'{total/21:.2f}')