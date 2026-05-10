matricula = 0
cre = 0
creSoma = 0
alunos = 0

creMenorMat = ''
creMenor = 99999999

while cre != 999:
    matricula = input()
    if matricula == '999':
        break
    cre = float(input())

    creSoma = creSoma + cre
    alunos = alunos + 1

    if cre < creMenor:
        creMenor = cre
        creMenorMat = matricula


print(creMenorMat)
print(f'{creSoma/alunos:.2f}')