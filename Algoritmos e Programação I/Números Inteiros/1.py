num = int(input())
tamanho = 0
comparacao = num
aux2 = 0

aux = num

while aux > 0:
    aux = aux//10
    tamanho += 1 

for i in range(tamanho):
    resto = num % 10
    num //= 10
    aux2 = (10 * aux2) + resto

print("sim" if aux2 == comparacao else "não")
