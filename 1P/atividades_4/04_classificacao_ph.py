pH = int(input('Digite o pH da solucao:\n'))

if (0 > pH) or (pH > 14):
    print('Valor deve estar entre 0 e 14.')
elif pH < 7:
    print('Essa solucao e acida.')
elif pH > 7:
    print('Essa solucao e basica.')
elif pH == 7:
    print('Essa solucao e neutra.')