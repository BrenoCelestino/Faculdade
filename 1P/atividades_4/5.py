salario = float(input())

bonus = salario * (75/100)

if bonus < 2000:
    print('ARGENTINA')
elif bonus < 3000:
    print('ESPANHA')
elif bonus > 3000:
    print('ALEMANHA')