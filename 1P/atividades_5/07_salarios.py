sal = float(input())

if sal <= 280:
    print(f'{sal:.2f}')
    print('20')
    print(f'{sal * (20/100):.2f}')
    sal = sal + (sal * (20/100))
    print(f'{sal:.2f}')
    
elif sal < 700:
    print(f'{sal:.2f}')
    print('15')
    print(f'{sal * (15/100):.2f}')
    sal = sal + (sal * (15/100))
    print(f'{sal:.2f}')

elif sal < 1500:
    print(f'{sal:.2f}')
    print('10')
    print(f'{sal * (10/100):.2f}')
    sal = sal + (sal * (10/100))
    print(f'{sal:.2f}')

elif sal >= 1500:
    print(f'{sal:.2f}')
    print('5')
    print(f'{sal * (5/100):.2f}')
    sal = sal + (sal * (5/100))
    print(f'{sal:.2f}')