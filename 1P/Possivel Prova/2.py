# Coleta o tipo de conclusão do ensino médio
# CLD - Concluiu, CVC - Cursando, CSC - Concluirá, NCC - Não Concluiu
ensino = input() 

# Verifica se o candidato participou do Encceja (s = sim, n = não)
encceja = input()

# Coleta a nota obtida no Encceja (valores entre -1 e 800)
notaEncceja = int(input())

# Coleta o tipo de escola onde estudou
# PUB - Pública, PCB - Privada com Bolsa, PSB - Privada sem Bolsa, 
# PPS - Publica Particular sem Bolsa, PPB - Publica e Particula com Bolsa, NFE - Não Frequentou Escola
tipoEscola = input()

# Coleta a renda pessoal mensal
renda = float(input())

# Verifica se o candidato já fez o ENEM em 2018 (s = sim, n = não)
enem2018 = input()
if enem2018 == 's':
    # Se fez o ENEM 2018, verifica se a justificativa foi aceita (s = sim, n = não)
    jus = input()


# Validação: verifica se o tipo de ensino informado é válido
if ensino not in ('CLD', 'CVC', 'CSC', 'NCC'):
    print('\nInformacao sobre ensino medio invalida')
    exit()

# Validação: se fez ENEM 2018 mas a justificativa não foi aceita, não tem direito
if enem2018 == 's' and jus == 'n':
    print('\nInfelizmente voce nao tem direito a isencao')
    exit()


# Critério 1: Cursando ensino médio em escola pública
if ensino == 'CVC' and tipoEscola == 'PUB':
    print('\nVoce terah direito a isencao')
# Critério 2: Participou do Encceja e obteve nota mínima de 400
elif encceja == 's' and notaEncceja >= 400:
    print('\nVoce terah direito a isencao')
# Critério 3: Concluiu ensino médio em escola pública/bolsista e renda menor ou igual ao salário mínimo (R$ 1431)
elif ensino == 'CLD' and tipoEscola in ('PUB', 'PCB', 'PPB') and renda <= 1431:
    print('\nVoce terah direito a isencao')
# Se não atender nenhum dos critérios acima, não tem direito à isenção
else:
    print('\nInfelizmente voce nao tem direito a isencao')