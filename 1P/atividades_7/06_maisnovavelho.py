novo = 999
velho = 0

for i in range(1, 101):
    paciente = int(input())
    if paciente > velho:
        velho = paciente
    
    if paciente < novo:
        novo = paciente

print("mais novo:", novo)
print('mais velho:', velho)