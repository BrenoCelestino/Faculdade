string = input().upper()
string = string.replace(" ", "")

if string == string[::-1]:
    print("Palidromo")
else:
    print("Não Palidromo")