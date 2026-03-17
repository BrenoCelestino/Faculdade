monica = int(input())
filho1 = int(input())
filho2 = int(input())

if monica < 40 or monica > 110:
    print('Restricão violada!')
elif filho1 < 1 or filho1 > monica:
    print('Restricão violada!')
elif filho2 < 1 or filho2 > monica:
    print('Restricão violada!')
elif not filho1 != filho2:
    print('Restricão violada!')
else:
    filho3 = monica - (filho1 + filho2)
    if filho1 > filho2 and filho1 > filho3:
        print(f'O filho mais velho tem {filho1} anos.')
    elif filho2 > filho1 and filho2 > filho3:
        print(f'O filho mais velho tem {filho2} anos.')
    elif filho3 > filho2 and filho3 > filho1:
        print(f'O filho mais velho tem {filho3} anos.')