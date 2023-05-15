from math import sqrt

num = int(input())
flag = True

while True:
    resto = num % 100
    raiz = sqrt(resto)

    num //= 10

    if raiz != int(raiz):
        flag = False
        break

    if num < 10:
        break

print("sim" if flag else "não")
