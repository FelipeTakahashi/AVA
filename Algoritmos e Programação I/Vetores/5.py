def insertionSort(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

every_integer = [int(a) for a in input().split()]

only_positives = []
for index in range(len(every_integer)):
    if (every_integer[index] > 0):
        only_positives.append(every_integer[index])

# print(set(only_positives))

insertionSort(only_positives)

divergent_values = []
for index in range(0, len(only_positives) - 1):
    if (only_positives[index] != only_positives[index+1]):
        divergent_values.append(only_positives[index])

divergent_values.append(only_positives[-1])

print(divergent_values)
