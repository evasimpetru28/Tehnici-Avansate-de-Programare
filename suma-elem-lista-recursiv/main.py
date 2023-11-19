import random

def suma2(L):
    if len(L) == 0:
        return 0
    else:
        return L.pop() + suma2(L)

def suma(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + suma(L[1:])  # se copiaza  lista in memorie = se creeaza mereu lista noua

def suma_pozitive(L, ):
    if len(L) == 0:
        return 0
    else:
        aux = L.pop()
        if aux > 0:
            return aux + suma_pozitive(L)
        else:
            return suma_pozitive(L)



L = [random.randint(-10, 10) for x in range(10)]
print(L)
T = L.copy()
P = L.copy()

s = suma(L)
s2 = suma2(T)
s3 = suma_pozitive(P)
print(s, sep="\n")
print(s2, sep="\n")
print(s3, sep="\n")
