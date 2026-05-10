N = int(input())
n1 = 2
n2 = 4
S = 0

while N != 0:
    S = (N / (n1 * n2)) + S
    N = N - 1
    n1 = n1 + 4
    n2 = n2 + 4
print(f'{S:.4f}')