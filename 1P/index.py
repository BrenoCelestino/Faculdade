# while True:
#     n1 = float(input("Digite a nota 1 (0-10): "))
#     if 0 <= n1 <= 10:
#         break
#     print("Nota inválida! Digite um valor entre 0 e 10.")

# while True:
#     n2 = float(input("Digite a nota 2 (0-10): "))
#     if 0 <= n2 <= 10:
#         break
#     print("Nota inválida! Digite um valor entre 0 e 10.")

# while True:
#     n3 = float(input("Digite a nota 3 (0-10): "))
#     if 0 <= n3 <= 10:
#         break
#     print("Nota inválida! Digite um valor entre 0 e 10.")

# soma = n1 + n2 + n3
# media = soma / 3

# if media >= 7:
#     print("Aprovado. Nota final: ", round(media, 2))
# elif media >= 5:
#     print("Recuperação. Nota final: ", round(media, 2))
# else:    
#     print("Reprovado. Nota final: ", round(media, 2))

divisor = 0
dividendo = 10

if divisor == 0:
    print("0")
elif divisor < 0 or dividendo < 0:
    print("-1")
elif divisor > 0 and dividendo > 0:
    resultado = dividendo / divisor
    print("Resultado da divisão: ", resultado)