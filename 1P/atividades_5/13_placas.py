p1 = int(input())
p2 = int(input())
p3 = int(input())

if not 1 <= (p1 or p2 or p3) <= 100:
    print('Violacao das restricoes')
    exit()

if p1 == p2 == p3:
    print('3 trofeus e 0 placa')
elif (p1 or p3) == p2:
    print('2 trofeu e 1 placa')
elif (p1 or p2) == p3:
    print('2 trofeu e 1 placa')
elif (p2 or p3) == p1:
    print('2 trofeu e 1 placa')
else:
    print('1 trofeu e 1 placa')