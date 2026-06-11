p = 0
g = 0

for i in range(7):
    quantidade = int(input())
    tipo = input().lower()

    if tipo == 'p':
        p += quantidade * 10
    else:
        g += quantidade * 16

print(p+g)
print(f'{((p+g) * 2) / 7:.0f}')
