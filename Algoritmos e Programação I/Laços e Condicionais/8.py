soma = 0
valores = 0

while True:
    try:
        n = input()

        if n == '':
            break

        n = float(n)
        valores += 1
        soma += n


    except EOFError:
        break

print(f"A soma é: {soma:.2f}\nA média é: {soma / valores:.2f}")
