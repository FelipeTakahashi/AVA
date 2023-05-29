from random import randint as roll

times = 0

every_roll = []
for _ in range(50):
    result = roll(1, 6)
    # if (result == 6): times += 1  <-- Se não usar lista.
    every_roll.append(result)

for index in range(len(every_roll)):
    if (every_roll[index] == 6):
        times += 1

print(f"{times*2}%")
