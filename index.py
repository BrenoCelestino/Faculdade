# num0 = float(input())
# num1 = float(input())
# num2 = float(input())
# num3 = float(input())

# while True:
#     media = num0 + num1 + num2 + num3 / 4
#     print(media)
#     break

n = 1000
i = 0

# while i * i < n:
#     print(i * i, end=" ")
#     i += 1

while n > 0:
    if (n % 10) == 0:
        print(n)
        
    n = n - 1