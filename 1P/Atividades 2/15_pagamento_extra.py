sal = round(float(input()), 2)
horas = int(input())

extras = ((5/100) * sal)
pag = (extras * horas) + sal
print()
print(f'{pag:.2f}')