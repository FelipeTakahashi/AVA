atual = float(input())
pagamento = atual*5/100
restante = atual

print("Mês   Saldo Atual       Juros     Valor Principal        Pagamento       Saldo Restante")

for mes in range(1, 21):
    
    juros = atual/100
    principal = pagamento - juros
    restante = atual - pagamento
    
    if atual < pagamento:
        juros = 0
        restante = 0
        pagamento = atual
        principal = atual
    
    print("{0:2.0f}  {1:10.2f}     {2:10.2f}          {3:10.2f}       {4:10.2f}           {5:10.2f}".format(mes, atual, juros, principal, pagamento, restante))
    
    atual = restante
