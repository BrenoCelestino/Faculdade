naci = input().lower() # B/E
ocupacao = input().lower() # M/T/C/O
quantidade = int(input())
calibre = int(input())

if naci == 'b':
    if ((quantidade and calibre) == 0) or (ocupacao == 'm'):
        print('Liberado')
    elif (ocupacao == 'c') and (calibre <= 38) and (quantidade <= 2):
        print('Liberado')
    elif (ocupacao == 't' or 'o') and (quantidade == 1) and (calibre <= 22):
        print('Liberado')
    else:
        print('Barrado')
else:
    if quantidade > 0:
        print('Barrado')
    else:
        print('Liberado')