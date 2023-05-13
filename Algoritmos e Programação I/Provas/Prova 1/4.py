h, m, s = map(int, input().split(":"))
duracao = int(input())

hb = h
mb = m
sb = s

m = m + duracao

aux = m//60
m = m%60

h = (h+aux)%24

print("Horário de partida: %i:%i:%i" %(hb,mb,sb))
print("Duração prevista: %i minutos"%duracao)
print("Previsão de chegada: %i:%i:%i" %(h,m,s))
