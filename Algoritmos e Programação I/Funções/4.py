def soma_matriz(m, v):
    c = []
    for row in range(len(m)):
        aux = []
        for col in range(len(m[0])):
            value = m[row][col] + v[row][col]
            aux.append(value)
        c.append(aux)
    return c

def multiplica_matriz(m, v):
    c = []
    assert len(m[0]) == len(v)
    for row in range(len(m)):
        c.append([])
        for col in range(len(v[0])):
            c[row].append(0)
            for k in range(len(m[0])):
                c[row][col] += m[row][k] * v[k][col]
    return c

m, n = map(int, input().split()) # Exercício 16/06/23
a = []

for i in range(m):
    valores = [int(a) for a in input().split()]
    a.append(valores)

b = [int(a) for a in input().split()]

c = [0] * m

for i in range(m):
    for j in range(n):
        c[i] += a[i][j] * b[j]

print(c)
