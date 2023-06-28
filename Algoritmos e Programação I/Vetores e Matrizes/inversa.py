# Imprimir em ordem inversa
n = int(input())
lista = [0] * n

for i in range(n):
    lista[i] = int(input())

print(lista[::-1])
