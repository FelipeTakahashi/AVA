gabarito = str(input())
aluno, cartao = map(str, input().split())

contador = 0
for i in range(30):
    if (cartao[i] == gabarito[i]):
        contador += 1

print(f"O aluno {aluno} acertou {contador} questões.")
