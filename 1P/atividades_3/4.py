p1 = int(input())
c1 = int(input())
p2 = int(input())
c2 = int(input())

if (c2 < 10) or (c2 > 100):
    print('Restricao violada')
    exit()
if c1 < 10 or c1 > 100:
    print('Restricao violada')
    exit()
if p2 < 10 or p2 > 100:
    print('Restricao violada')
    exit()
if p1 < 10 or p1 > 100:
    print('Restricao violada')
    exit()

esquerdo = (p1 * c1)
direito = (p2 * c2)

if esquerdo == direito:
    print('Gangorra equilibrada')
elif esquerdo > direito:
    print('Gangorra desequilibrada para a esquerda')
else:
    print('Gangorra desequilibrada para a direita')