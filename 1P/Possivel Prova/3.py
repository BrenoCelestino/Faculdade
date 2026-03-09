patri = float(input('Qual seu Patrimônio total?\nDigite: '))
extDecla = int(input('Quanto de Patrimônio no exterior você declarou a receita?\nDigite: '))
patriExt = float(input('Patrimônio total no exterior.\nDigite: '))
multa = input('Ja pagou multa a receita?\nDigite: ')

if patriExt > ((20 * patri) / 100):
    imposto = 's' # 15% de imposto
else:
    isenta = 's'

if patri >= 1000000:
    if multa == 's' and (((extDecla - patriExt) / extDecla) * 100) < 10:
        multa = 's'
        imposto = 's'
        crime = 's'
        
    elif (((extDecla - patriExt) / extDecla) * 100) < 10:
        multa = 's'
        imposto = 's'
    
if patri <= 1000000 and (((extDecla - patriExt) / extDecla) * 100) < 10:
    imposto = 's'