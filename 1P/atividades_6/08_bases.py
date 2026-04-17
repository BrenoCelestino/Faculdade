subs = float(input())

while subs != -1:
    if subs < 7:
        print('ACIDA')
    elif subs > 7:
        print('BASICA')
    elif subs == 7:
        print('NEUTRA')
    subs = float(input())