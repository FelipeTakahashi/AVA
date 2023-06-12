produtos =  [
            ['A', "Refrigerante     ", "R$ 5,00"],
            ['B', "Casquinha Simples", "R$ 5,50"],
            ['C', "Casquinha Dupla  ", "R$ 8,00"],
            ['D', "Sundae           ", "R$ 10,50"],
            ['E', "Banana Split     ", "R$ 12,00"],
            ]

def menu(produtos):
    for i in range(5):
        print()
        for j in range(3):
            print(produtos[i][j], end='  ')

def pagar():
    valor = (refri * 5) + (casquinha_s * 5.50) + (casquinha_d * 8) + (sundae * 10.50) + (banana_s * 12.00)
    return valor

def relatorio():
    print("= = = = = =\nRELATÓRIO\n")

    print(f"Total de Refrigerante(s):       {t_refri}")
    print(f"Total de Casquinha(s) Simples:  {t_simples}")
    print(f"Total de Casquinha(s) Dupla(s): {t_dupla}")
    print(f"Total de Sundae(s):             {t_sundae}")
    print(f"Total de Banana Split(s):       {t_banana}\n")
    
    print("Total por produto:")
    print(f"Refrigerante:      R$ {t_refri * 5:.2f}")
    print(f"Casquinha simples: R$ {t_simples * 5.50:.2f}")
    print(f"Casquinha dupla:   R$ {t_dupla * 8:.2f}")
    print(f"Sundae:            R$ {t_sundae * 10.50:.2f}")
    print(f"Banana Split:      R$ {t_banana * 12.00:.2f}\n")

    print(f"Total arrecadado: R$ {total:.2f}")
    print(f"Valor médio de cada compra: R$ {total/clientes:.2f}\n= = = = = =")

t_refri, t_simples, t_dupla, t_sundae, t_banana = 0, 0, 0, 0, 0
clientes, total = 0, 0
venda = ''

while(True):

    refri, casquinha_s, casquinha_d, sundae, banana_s = 0, 0, 0, 0, 0
    menu(produtos)

    venda = [str(a) for a in input("\nCódigos: ").split()]
    if (venda == ['0']): break

    for i in range(len(venda)):
        if   (venda[i] == 'A'): 
            refri += 1
            t_refri += 1
        elif (venda[i] == 'B'): 
            casquinha_s += 1
            t_simples += 1
        elif (venda[i] == 'C'): 
            casquinha_d += 1
            t_dupla += 1
        elif (venda[i] == 'D'): 
            sundae += 1
            t_sundae += 1 
        elif (venda[i] == 'E'): 
            banana_s += 1
            t_banana += 1
    
    clientes += 1
    print(f"Valor a pagar: {pagar():.2f}")
    total += pagar()

relatorio()
