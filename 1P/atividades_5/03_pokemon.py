poke = int(input())

inRattata = int(input())
inEevee = int(input())
inPikachu = int(input())
inBulbasaur = int(input())
inSquirtle = int(input())
inCharmander = int(input())

Rattata = 1
Eevee = 5
Pikachu = 10
Bulbasaur = 25
Squirtle = 50
Charmander = 100

capRattata = min(inRattata, poke // Rattata)
poke -= capRattata * Rattata

capEevee = min(inEevee, poke // Eevee)
poke -= capEevee * Eevee

capPikachu = min(inPikachu, poke // Pikachu)
poke -= capPikachu * Pikachu

capBulbasaur = min(inBulbasaur, poke // Bulbasaur)
poke -= capBulbasaur * Bulbasaur

capSquirtle = min(inSquirtle, poke // Squirtle)
poke -= capSquirtle * Squirtle

capCharmander = min(inCharmander, poke // Charmander)
poke -= capCharmander * Charmander

print(poke)
print(f'Rattata {capRattata}')
print(f'Eevee {capEevee}')
print(f'Pikachu {capPikachu}')
print(f'Bulbasaur {capBulbasaur}')
print(f'Squirtle {capSquirtle}')
print(f'Charmander {capCharmander}')