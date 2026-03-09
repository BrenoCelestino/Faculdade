n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

n5 = ((n3 - n4) / n3) * 100

n6 = (n1 + n2 + n3) / 3

if n5 < 20:
    print('\nBLACK FRAUDE')
elif n1 < n2 and n2 < n3:
    print('\nBLACK FRAUDE')
elif n4 > n6:
    print('\nBLACK FRAUDE')
else:
    print('\nOFERTA OK')