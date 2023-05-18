x, y, u, v = [], [], [], []

for i in range(int(input())):
    upper_x, upper_y, lower_x, lower_y = map(int, input().split())

    x.append(upper_x)
    y.append(upper_y)
    u.append(lower_x)
    v.append(lower_y)

x = sorted(x)
y = sorted(y)
u = sorted(u)
v = sorted(v)

print((x[-1], y[0], u[0], v[-1]) if (x[-1] < u[0] and v[-1] < y[0]) else "nenhum" )
