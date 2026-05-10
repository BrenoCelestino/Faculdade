port = 0
mat = 0
reda = 0

aprovados = 0

while port >= 0:
    port = int(input())
    if port < 0:
        break
    mat = int(input())
    reda = float(input())

    portN = (port / 50) * 100
    matN = (mat / 35) * 100
    if (portN >= 80) and (matN >= 60) and (reda >= 7):
        aprovados = aprovados + 1
print(aprovados)