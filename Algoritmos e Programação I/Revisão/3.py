"""
Intervalo
Faça um programa que leia uma quantidade indeterminada de
números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada
deverá terminar quando for lido um número negativo.
"""

numbers = []
zero_twenty = 0
twenty_fifty = 0
fifty_seventy = 0
seventy_hundred = 0
out = 0

while True:
    num = int(input())

    if num < 0: 
        break

    numbers.append(num)

for number in numbers:
    if number in range(0, 26):
        zero_twenty += 1

    elif number in range(26, 51):
        twenty_fifty += 1

    elif number in range(51, 77):
        fifty_seventy += 1

    elif number in range(77, 101):
        seventy_hundred += 1

    else:
        out += 1

print(f"\nIntervalo [0-25]: {zero_twenty:3}\n\nIntervalo [26-50]: {twenty_fifty:2}\n\nIntervalo [51-76]: {fifty_seventy:2}\n\nIntervalo [77-100]: {seventy_hundred:1}\n\nFora de intervalo: {out:2}")
