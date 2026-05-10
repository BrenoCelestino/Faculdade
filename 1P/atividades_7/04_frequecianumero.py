x, y = map(int, input().split())
soma = 0

for i in range(1, x + 1):
    num = int(input())
    if num == y:
        soma += 1
    
print(soma)