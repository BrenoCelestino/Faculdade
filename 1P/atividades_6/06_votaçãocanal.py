canal = int(input())
canal9 = 0
canal5 = 0
canal4 = 0

while canal != 0:
    if canal == 9:
        canal9 = canal9 + 1
    elif canal == 5:
        canal5 = canal5 + 1
    elif canal == 4:
        canal4 = canal4 + 1
    canal = int(input())

if canal9 > canal5 and canal5 > canal4:  # 9 > 5 > 4
    print('canal 9:', canal9)
    print('canal 5:', canal5)
    print('canal 4:', canal4)

elif canal9 > canal4 and canal4 > canal5:  # 9 > 4 > 5
    print('canal 9:', canal9)
    print('canal 4:', canal4)
    print('canal 5:', canal5)

elif canal5 > canal9 and canal9 > canal4:  # 5 > 9 > 4
    print('canal 5:', canal5)
    print('canal 9:', canal9)
    print('canal 4:', canal4)

elif canal5 > canal4 and canal4 > canal9:  # 5 > 4 > 9
    print('canal 5:', canal5)
    print('canal 4:', canal4)
    print('canal 9:', canal9)

elif canal4 > canal9 and canal9 > canal5:  # 4 > 9 > 5
    print('canal 4:', canal4)
    print('canal 9:', canal9)
    print('canal 5:', canal5)

elif canal4 > canal5 and canal5 > canal9:  # 4 > 5 > 9
    print('canal 4:', canal4)
    print('canal 5:', canal5)
    print('canal 9:', canal9)