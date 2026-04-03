pi = 3.1415

corpo = input()
calcular = input()

if corpo not in['c', 'e']:
    print("Entrada invalida! Voce deve usar 'c' (cilindro) " \
    "ou 'e' (esfera).")

elif calcular not in['a', 'v']:
    print("Entrada invalida! Entre com 'a' (area) " \
    "ou 'v' (volume).")

else:
    if corpo == 'c' and calcular == 'a': #Calcular a area de um cilindro.
        raio = float(input())
        altura = float(input())

        area = 2 * pi * raio * (raio + altura)

        print(f"A area do cilindro de raio {raio:.2f} e altura {altura:.2f} eh:\n{area:.2f}")

    elif corpo == 'c' and calcular == 'v': #Calcular o volume de um cilindro.
        raio = float(input())
        altura = float(input())

        volume = pi * (raio**2) * altura

        print(f"O volume do cilindro de raio {raio:.2f} e altura {altura:.2f} eh:\n{volume:.2f}")
        
    else:
        if corpo == 'e' and calcular == 'a': #Calcular a area de uma esfera.
            raio = float(input())

            area = 4 * pi * (raio**2)

            print(f"O volume da esfera de raio {raio:.2f} eh:\n{area:.2f}")

        elif corpo == 'e' and calcular == 'v': #Calcular a volume de uma esfera.
            raio = float(input())

            volume = (4/3) * pi * (raio**3)

            print(f"A area da esfera de raio {raio:.2f} eh:\n{volume:.2f}")