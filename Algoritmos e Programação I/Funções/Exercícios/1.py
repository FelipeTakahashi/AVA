def calcula_mdc(a, b):
    if (b == 0): return a
    a, b = max(a, b), min(a, b)
    while (b != 0):
        a, b = b, a%b
    return a

#from bib_projeto import calcula_mdc

def main():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        if (calcula_mdc(x, y) == 1): print(f"{x} {y}: primos entre si")
        else: print(f"{x} {y}: não primos entre si")
main()
