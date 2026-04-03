idade = int(input())

if idade < 18:
    print(f'Você precisa esperar mais {18 - idade} ano(s)!')
else:
    print("Voce ja pode tirar habilitacao!")
    print(f"Voce tem direito a habilitacao ha {idade - 18} ano(s)")