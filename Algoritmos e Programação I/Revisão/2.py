"""
Pescador
Um regulamento de pesca do estado de São Paulo estabelece
que uma multa de R$ 4,00 deve ser paga para cada quilo 
excedente do padrão (50 quilos).

Leia a variável peso e verifique se há excesso. Se houver,
grave na variável excesso e na variável multa o valor da 
multa que joão deverá pagar. Caso contrário, mostre tais
variáveis com o conteúdo zero.
"""

peso = float(input())

excesso = peso - 50

if excesso <= 0: 
    excesso = 0
    multa = 0

else:
    multa = excesso*4

print(f"\nMulta: {multa:.2f}\n\nExcesso em kg: {excesso:.2f}")
