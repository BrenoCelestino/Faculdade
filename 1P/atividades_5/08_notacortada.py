B = int(input())
A = int(input())

AreaBA = ((B + A) * 70) / 2

C = 160 - B
D = 160 - A

AreaCD = ((C + D) * 70) / 2

if AreaBA == AreaCD:
    print('0')
elif AreaBA > AreaCD:
    print('1')
elif AreaBA < AreaCD:
    print('2')