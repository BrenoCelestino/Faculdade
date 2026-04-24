numero = int(input())

while numero != -1:
    
    if numero <= 1:
        print(0)
    else:
        i = 2
        eh_primo = 1
        
        while i < numero:
            if numero % i == 0:
                eh_primo = 0
                break
            i += 1
        
        print(eh_primo)
    
    numero = int(input())