d, h = map(float, input().split(" "))
h = int(h)
km = d/1000
v = km/h
print(f"Uma viagem que durou {h:.2f} hora(s) e percorreu {km:.2f} quilômetros.\nA viagem foi feita com velocidade média de {v:.2f} km/h.")
