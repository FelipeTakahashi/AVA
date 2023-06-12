def encontra_maior(matriz):
    for i in range(n):
        if matriz[i][0] > matriz[i][1]: maior = matriz[i][0]
        else: maior = matriz[i][1]
        m[i] = maior
    return m

def multiplica(vetor):
    produto = 1
    for i in range(len(vetor)):
        produto *= vetor[i]
    return produto

n = int(input())

v = [0] * n
m = [0] * n

for i in range(n):
    par = [int(a) for a in input().split()]
    v[i] = par

print(encontra_maior(v))
print(multiplica(m))
