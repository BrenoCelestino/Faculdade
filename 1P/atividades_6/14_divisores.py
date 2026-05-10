x = int(input())
div = x

while div > 0:

    if (x % div) == 0:
        print(div)
        div = div - 1
    else:
        div = div - 1
        continue