a = int(input())
b = int(input())
c = int(input())
nulos = int(input())
votos = a + b + c + nulos

#Não arredondar porcentagens
aPor = int((a/votos) * 100)
bPor = int((b/votos) * 100)
cPor = int((c/votos) * 100)
nulosPor = int((nulos/votos) * 100)

print(f'Candidato A: {aPor}%')
print(f'Candidato B: {bPor}%')
print(f'Candidato C: {cPor}%')
print(f'Nulos: {nulosPor}%')