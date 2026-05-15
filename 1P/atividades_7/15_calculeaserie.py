N = int(input())
S = 0
A = 1
B = 3

for i in range(N):
    S += (A/B)
    if i != (N-1):
        print(f'{A}/{B} + ', end= "")
    else:
        print(f'{A}/{B}')
    A = A + 1
    B = B + 3
    
print(f'{S:.2f}')