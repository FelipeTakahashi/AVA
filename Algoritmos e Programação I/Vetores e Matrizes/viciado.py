n = int(input())
resultados = {
             1 : 0,
             2 : 0,
             3 : 0,
             4 : 0,
             5 : 0,
             6 : 0
            }

for i in range(n):
    resultados[int(input())] += 1

for key, value in resultados.items():
    print(f"O lado {key} repetiu-se {value} vezes.")
