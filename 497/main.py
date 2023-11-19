n = int(input())
lista = [int(x) for x in input().split()]

posibil_castigator = None
avantaj = 0

for elem in lista:
    if avantaj == 0:
        posibil_castigator = elem
        avantaj = 1
    elif elem == posibil_castigator:
        avantaj += 1
    else:
        avantaj -= 1

if avantaj == 0:
    print("NU")
else:
    if lista.count(posibil_castigator) > n // 2:
        print("DA " + str(posibil_castigator))
    else:
        print("NU")