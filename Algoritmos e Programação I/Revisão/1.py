'''
Peso Ideal
Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando
as seguintes fórmulas:

Para homens: (72.7 * altura) - 58
Para mulheres: (62.1 * altura - 44.7)

Peça o peso da pessoa e informa se ela está dentro, acima ou 
abaixo do peso.
'''

peso = float(input())
altura = float(input())
sexo = str(input())

if sexo == "M" or sexo == "Masculino":
    ideal = (72.7 * altura) - 58

else:
    ideal = (62.1 * altura) - 44.7

print(f"Peso ideal: {ideal:.2f}")

if peso > ideal:
    print("Acima do peso.")

elif peso < ideal:
    print("Abaixo do peso.")

else:
    print("Peso ideal.")
