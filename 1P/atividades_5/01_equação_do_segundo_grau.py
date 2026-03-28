a = float(input())
b = float(input())
c = float(input())

delta = (b**2) - (4 * a * c)

if delta < 0:
    print('NRR')
elif (a == 0) or (b == 0) or (c == 0):
    print('NEESG')
elif delta == 0:
    raiz1 = (-b + (delta ** 0.5)) / (2 * a)
    print(f'{raiz1:.2f}')
    print(f'{raiz1:.2f}')
elif delta > 0:
    raiz1 = (-b + (delta ** 0.5)) / (2 * a)
    raiz2 = (-b - (delta ** 0.5)) / (2 * a)
    print(f'{raiz1:.2f}')
    print(f'{raiz2:.2f}')