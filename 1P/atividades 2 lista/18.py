days = int(input())
km = float(input())
diaria = 30
kmP = 0.01

pagar =  ((diaria * days) + (kmP * km)) - (10 / 100 * ((diaria * days) + (kmP * km)))
print(f'{pagar:.2f}')