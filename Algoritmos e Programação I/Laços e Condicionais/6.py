salario = float(input())
aumento = int(input())
anos = int(input())

print("Ano   Salário\n--------------")

for i in range(1, anos+1):
    print(f"{i:2} {salario:11.2f}")
    salario += ((aumento/100) * salario) 
