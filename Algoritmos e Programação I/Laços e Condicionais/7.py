a, b = map(int, input().split())
# maior = max(a, b)
# menor = min(a, b)

if a > b:
    maior = a
    menor = b

else:
    maior = b
    menor = a

etapa = 0

while menor != 0:
    etapa += 1
    resto = maior%menor


    etapa += 1
    maior = menor
    menor = resto

print(f"O MDC é: {maior}")
