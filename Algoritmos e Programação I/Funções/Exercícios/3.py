def pontua_etapa(a, b):
    delta = abs(a - b)
    if (delta < 3): return 100.0
    elif (3 <= delta <= 5): return 80.0
    else: return round(80-((delta-5)/5))

#from bib_projeto import pontua_etapa

def main():
    times = {}
    valores = [int(a) for a in input().split()]
    for _ in range(valores[3]):
        total = 0
        pont_times = [int(a) for a in input().split()]
        for i in range(3):
            total += pontua_etapa(valores[i], pont_times[i+1])
        times[pont_times[0]] = total
        print(f"{pont_times[0]} {total:.1f}")
    print(f"Equipe Vencedora: {max(times, key=times.get)} - Pontuação: {max(times.values()):.1f}")
    
main()
