n = int(input())
soma = n

if n <= 0:
    print(1)
    exit()

for i in range(n, 1, -1):
    soma = soma * (i-1)

print(soma)