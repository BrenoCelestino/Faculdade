ano1, ano2 = map(int, input().split())

achou = False

for i in range(ano1, ano2 + 1):
    if i % 400 == 0:
        print(i)
        achou = True
    elif i % 100 == 0:
        pass
    elif i % 4 == 0:
        print(i)
        achou = True

if not achou:
    print(-1)