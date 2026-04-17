ensinomedio = input().lower() # CLD/CVC/CSC/NCC
if ensinomedio not in ['cld', 'cvc', 'csc', 'ncc']:
    print('Informacao sobre ensino medio invalida')
    exit()

encceja = input().lower() # S ou N
notaEncceja = int(input()) # -1 a 800
tipoEscola = input().lower()
renda = float(input())

isencao = input().lower()
if isencao == 's':
    justificou = input().lower()
    if justificou == 'n':
        print('Infelizmente voce nao tem direito a isencao')
        exit()

if ensinomedio == 'cld' and (renda <= 1431.00) and (tipoEscola in ['pub', 'pcp', 'ppb']):
    print('Voce terah direito a isencao')
elif ensinomedio == 'cvc' and tipoEscola == 'pub':
    print('Voce terah direito a isencao')
elif encceja == 's' and notaEncceja >= 400:
    print('Voce terah direito a isencao')
else:
    print('Infelizmente voce nao tem direito a isencao')