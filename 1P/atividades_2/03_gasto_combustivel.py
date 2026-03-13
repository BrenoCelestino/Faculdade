# (Problema: Gasto de combustível (URI)) Joaozinho quer calcular e mostrar a quantidade de
# litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L.
# Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o
# cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante
# a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular
# quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

temVig = 10 #Em horas
velMed = 80 #Em km/h
efiCar = 12 #Km/L

distancia = (temVig * velMed) #Em KM

print(f'São necessarios: {distancia / efiCar:.3f} Litros')
