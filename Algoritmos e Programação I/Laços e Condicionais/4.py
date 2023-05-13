organismos = int(input())
taxa = float(input())
minimo = int(input())
maximo = int(input())

while maximo > 0:

    organismos *= taxa
    maximo -= minimo

print(f"A população total será de {int(organismos)}")
