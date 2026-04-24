pessoasMais50 = 0
soma10e20 = 0

pessoas10e20 = 0

pessoas = 0
pessoas40quilos = 0

idade = 0

while True:
    idade = int(input('Digite sua idade:\n'))
    if idade < 0:
        break

    altura = float(input('Digite sua altura em metros:\n'))
    peso = float(input('Digite seu peso em kg:\n'))

    if idade >= 50:
        pessoasMais50 += 1
    
    if 10 <= idade <= 20:
        soma10e20 += altura
        pessoas10e20 += 1

    if peso < 40:
        pessoas40quilos += 1

    pessoas += 1

print('Quantidade de pessoas com idade superior a 50 anos:', pessoasMais50)
print('Media das alturas das pessoas com idade entre 10 e 20 anos:', f"{soma10e20/pessoas10e20:.2f}")
print('Porcentagem de pessoas com peso inferior a 40 quilos:', f'{((pessoas40quilos/pessoas) * 100):.1f}', '%') 