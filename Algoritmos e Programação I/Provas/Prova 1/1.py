from math import sqrt
x1, y1 = map(float, input().split(" "))
x2, y2 = map(float, input().split(" "))

dx = x2 - x1
dy = y2 - y1

dx = sqrt((dx**2))
dy = sqrt((dy**2))

p = (dx*2) + (dy*2)
a_m = dx*dy
h = a_m/10000

print(f"Serão necessários {p:.2f} metros de arame farpado.\nA fazenda possui {h:.2f} hectares.")
