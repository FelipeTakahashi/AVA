vetorA = [int(a) for a in input().split()]
vetorB = [int(b) for b in input().split()]

produto = [0] * 3
for i in range(3):
    produto[i] = vetorA[i] * vetorB[i]

print(sum(produto))
