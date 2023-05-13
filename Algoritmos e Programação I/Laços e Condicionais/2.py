a = int(input())
b = int(input())
c = int(input())

lados = [a, b, c]
#lados.sort()

for i in range(len(lados)):
    for j in range(i + 1, len(lados)):
        if lados[i] > lados[j]:
            lados[i], lados[j] = lados[j], lados[i]

print("O triângulo é retângulo." if (lados[0]**2 + lados[1]**2 == lados[2]**2) else "O triângulo não é retângulo.")
