st1 = input()
st2 = input()

print(f'Tamanho de "{st1}":', len(st1))
print(f'Tamanho de "{st2}":', len(st2))

if len(st1) != len(st2):
    print('As duas strings são de tamanhos diferentes.')
    print('As duas strings possuem conteúdo diferente.')
elif st1 == st2:
    print('As duas strings são de tamanhos iguais.')
    print('As duas strings possuem conteúdo igual.')