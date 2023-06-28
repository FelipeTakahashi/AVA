n = int(input())
resultados = {i : 0 for i in range(37)}

for i in range(n):
    resultados[int(input())] += 1

for key, value in resultados.items():
    print(f"O número {key} repetiu-se {value} vezes.")
