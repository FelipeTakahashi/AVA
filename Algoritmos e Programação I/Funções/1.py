def inverte(vetor):
    for i in range(int(len(vetor)/2)):
        vetor[i], vetor[(len(vetor)-1)-i] = vetor[(len(vetor)-1)-i], vetor[i]
    return vetor

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(inverte(vetor))
