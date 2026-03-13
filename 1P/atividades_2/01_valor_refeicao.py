# Na cantina do IFPB se cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo que
# leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que
# a balança já desconte o peso do prato.

valorRefeicao = 12.00

peso = float(input("Informe a quantidade de quilos, em KGs: "))

valorTotal = valorRefeicao * peso

print(f'O valor total de sua refeição é: {valorTotal}')