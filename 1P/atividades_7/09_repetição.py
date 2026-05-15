N = float(input())
M = int(input())
soma = N

if M == 0:
    print("1.00")
    exit()

for i in range(0, M - 1):
    soma = soma * N

print(f'{soma:.2f}')