N = int(input())
A = int(input())
B = int(input())

conta = 0
tem = True

for i in range (A, B + 1):
    if (N * conta) >= A and (N*conta) <= B:
        print(N*conta)
        tem = False
    conta += 1

if tem:
    print('INEXISTENTE')