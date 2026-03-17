colesterol = float(input())

if colesterol < 150:
    print(f'Colesterol total {colesterol:.1f} mg/dl (DESEJAVEL)')
elif colesterol <= 170:
    print(f'Colesterol total {colesterol:.1f} mg/dl (LIMITROFE)')
elif colesterol > 170:
    print(f'Colesterol total {colesterol:.1f} mg/dl (ALTO)')