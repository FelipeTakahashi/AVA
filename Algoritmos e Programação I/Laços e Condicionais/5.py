rep = int(input())
soma = 0

for n in range(rep):
    aux = (-1)**n / (2*n+1)
    soma += aux

print(f"A aproximação de pi é {soma*4}\nCompare isso com a estimativa do computador: 3.141592653589793")
