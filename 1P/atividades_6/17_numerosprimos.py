def eh_primo(numero):
	if numero <= 1:
		return False

	divisor = 2
	while divisor < numero:
		if numero % divisor == 0:
			return False
		divisor += 1
	return True


quantidade = int(input())

while quantidade < 2 or quantidade > 12:
	print('Informe um valor entre 2 e 12!')
	quantidade = int(input())

primos = []

while len(primos) < quantidade:
	numero = int(input())
	if eh_primo(numero):
		primos.append(numero)

saida = ''
for i in range(len(primos)):
	if i == 0:
		saida = str(primos[i])
	else:
		saida = saida + ' ' + str(primos[i])

print(saida)
