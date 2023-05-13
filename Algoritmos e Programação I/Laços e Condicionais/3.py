altura = float(input())
indice = float(input())
quiques = int(input())

distancia = altura

for quique in range(quiques):
    altura *= indice
    distancia += 2*altura

print(f"A distância total aproximada percorrida pela bola é de: {distancia-altura:.2f} unidades.")
