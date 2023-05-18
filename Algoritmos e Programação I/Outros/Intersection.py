every_x = []
every_y = []

for _ in range(int(input())):
    coordinates = [int(a) for a in input().split()]
    for i in range(len(coordinates)):
        if i % 2 == 0:
            every_x.append(coordinates[i])
        else:
            every_y.append(coordinates[i])

upper_left_x = []
upper_left_y = []

bottom_right_x = []
bottom_right_y = []

for i in range(len(every_x)):
    if i % 2 == 0:
        upper_left_x.append(every_x[i])
    else:
        bottom_right_x.append(every_x[i])

for i in range(len(every_y)):
    if i % 2 == 0:
        upper_left_y.append(every_y[i])
    else:
        bottom_right_y.append(every_y[i])

upper_x = max(upper_left_x)
upper_y = max(upper_left_y)

bottom_x = min(bottom_right_x)
bottom_y = min(bottom_right_y)

print(every_x)
print(every_y)

print(upper_x, upper_y)
print(bottom_x, bottom_y)

print(upper_left_x, upper_left_y)
print(bottom_right_x, bottom_right_y)
