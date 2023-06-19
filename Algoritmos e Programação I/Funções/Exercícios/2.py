def distancia(x, y, u, v):
    return ((u-x)**2+(v-y)**2)**(1/2)
    
def estah_dentro(x, y, u, v, r):
    if (distancia(x, y, u, v) <= r): return True
    return False

#from bib_projeto import estah_dentro

def main():
    while True:
        cont = 0 
        r, x, y, n = map(float, input().split())
        if not r: exit()
        for _ in range(int(n)):
            u, v = map(float, input().split())
            if (estah_dentro(x, y, u, v, r)): cont += 1
        print(f"Existem {cont} focos nesta região.")
    
main()
