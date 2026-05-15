string = input()
string2 = input()

gan = 0

if len(string) > len(string2):
    tamn = len(string)
    gan = 1
else:
    tamn = len(string2)
    gan = 2

pos = 0

for i in range(tamn):
    if string[pos:pos +1] ==