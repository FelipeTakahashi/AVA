d, m, a = map(int, input().split("/"))
dias = int(input())

dia_final = (d + dias) % 30 + 1
meses = (d + dias) // 30

mes_final = (meses + m) % 12
anos = (meses + m) // 12

ano_final = anos + a

print (f"Data de fim do contratro: {dia_final}/{mes_final}/{ano_final}.")
