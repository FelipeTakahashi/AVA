barras = int(input())
print(f"Para embalar {barras} barras de chocolate são necessárias:")

enorme = barras // 50
resto = barras % 50

grande = resto // 20
resto %= 20

media = resto // 5
resto %= 5

pequena = resto

print(f"{enorme} caixas enormes\n{grande} caixas grandes\n{media} caixas médias\n{pequena} caixas pequenas")
