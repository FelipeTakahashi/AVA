"""
Vetores Intercalados
Faça um programa que lê dois vetores com 10 elementos cada. Gere um terceiro vetor de
20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos
dois outros vetores.
"""

vetor_um = [int(a) for a in input().split()]
vetor_dois = [int(a) for a in input().split()]

vetor_intercalado = []

for i in range(10):
    vetor_intercalado.append(vetor_um[i])
    vetor_intercalado.append(vetor_dois[i])
 
print(f"\nOs valores intercalados são: {vetor_intercalado}")
